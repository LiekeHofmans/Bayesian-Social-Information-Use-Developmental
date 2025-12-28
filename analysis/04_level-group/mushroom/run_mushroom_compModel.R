###########################################################################
#
#  Wouter van den Bos and Lieke Hofmans
#
#  Analysis code for mushroom behavioral data.
#                                                                                           
#  Contains:
#  0 Set up                           - Preparatory steps  
#  1 Data                             - Load and transform data
#  2 Models                           - Define models and model related variables
#  3 Fitting                          - Fit parameters based on real data
#  4 Goodness of fit                  - Determine raw cost and BIC by comparing predicted and observed behavior
#  5 Model-based certainty            - Calculate and plot model based certainty and confidence (subjective number of mushrooms)
#  6 Posterior predictives            - Calculate predicted data based on fitted parameters
#  7 Plot parameter distribution      - Plot the distribution of all parameters of winning model
#  8 Plot model vs behavior           - Plot predicted behavior vs observed behavior

## =============================================================================
## 0 Set up script
## =============================================================================

# Clear working directory
rm(list = ls())

# Load packages
if(!require(snowfall,quietly = T)) install.packages('snowfall')
if(!require(snowfall,quietly = T)) install.packages('tidyverse')
if(!require(snowfall,quietly = T)) install.packages('viridis')
if(!require(snowfall,quietly = T)) install.packages('grid')
if(!require(snowfall,quietly = T)) install.packages('gridExtra')
if(!require(snowfall,quietly = T)) install.packages('ggpubr')
if(!require(snowfall,quietly = T)) install.packages('Hmisc')
require(snowfall)
require(tidyverse)
require(viridis)
require(grid)
require(gridExtra)
require(ggpubr)
require(Hmisc)

# Set directories
DIR_analysis_main <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis"
DIR_this_analysis <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis/04_level-group/mushroom"
DIR_data <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/derivatives/beh/mushroom"

# Create folder in which the results will be stored
fit.folder <- 'results_fit_sample' ; dir.create(file.path(DIR_this_analysis,fit.folder),showWarnings = T)
# Create folder in which the predicted results will be stored
prediction.folder <- 'results_pred' ; dir.create(file.path(DIR_this_analysis,prediction.folder),showWarnings = T)
# Create folder in which the simulated results will be stored
simulation.folder <- 'results_sim' ; dir.create(file.path(DIR_this_analysis,simulation.folder),showWarnings = T)

source(file.path(DIR_analysis_main, "summary_function.R"))

## =============================================================================
##  1  Load and transform data
## =============================================================================

# load the data
d <- read.csv(file.path(DIR_data, 'group_task-mushroom_preproc-trialwise-ranefs.csv'))
# split by ID for model fitting later on
dI <- split(d,d$sID)


## =============================================================================
## 2 Models
##     Define models and limits
## =============================================================================

# Load models
source(file.path(DIR_this_analysis, "model_specification.R"))

# Load helper functions
source(file.path(DIR_this_analysis, "helper_functions.R"))


## =============================================================================
## 3 Fit parameters
## =============================================================================

## MODEL FITTING
# Actual analysis fitting data
# Executes for all models ms the run function in parallel
# Writes results to harddrive
for(m in ms[c(1:10)]){ # model M0 has no parameters to fit
  print(Sys.time())
  t = proc.time()[3]
  sfInit(TRUE, 7)
  sfExportAll()
  fitOn <- "E2" # E1E2 gives a larger penalty for more complex models, without giving them any advantage since all paramters only come into play at E2.
  r <- sfClusterApplyLB(dI,run) # check run function for variable settings; apply run function to dI (dI == dfit)
  r = do.call(rbind,r)
  print(r)
  print(m)
  sfStop()
  write.table(r,file.path(DIR_this_analysis,fit.folder,paste0('subject_',m,'_fitE2.txt')))
  cat(round(proc.time()[3] - t, 0),'s to complete ',m,'\n',sep='')
}


## =============================================================================
## 4 Goodness of fit
## =============================================================================

# ------------------------------------------------------------------------------
# Compare raw costs (unpenalized)
# ------------------------------------------------------------------------------
cost_data <- as.data.frame(matrix(nrow = length(ms[c(1:10)]), ncol = 2))
colnames(cost_data) <- c("model", "mean_cost")
i_model <- 1
for (m in ms[c(1:10)]){
  r <- read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T)
  cost_data$model[i_model] <- m
  cost_data$mean_cost[i_model] <- mean(r[,1])
  i_model <- i_model + 1
}
cost_table <- tableGrob(cost_data); grid.arrange(cost_table)

# ------------------------------------------------------------------------------
# BIC
# We fit several regression models to the same dataset and choose the model 
# with the lowest BIC value as the model that best fits the data.
# ------------------------------------------------------------------------------

BIC_data <- as.data.frame(matrix(nrow = length(unique(d$sID)), ncol = length(ms[c(1:10)])))
i_model <- 1
for (m in ms[c(1:10)]){
  r <- read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T)
  for (isub in c(1:nrow(r))) {
    r_trunc <- r[-isub,] # Leave one out
    k <- (ncol(r)-2) * (length(unique(d$sID))-1) # k = nparams * nsub
    if (m == ms[1]) {
      k <- 0
    }
    n <- (nrow(d) - nrow(d[d$sID==(unique(d$sID)[isub]),])) * 1 # all trials * 1 estimate
    BIC_data[isub,i_model] <- sum(r_trunc[,1]) + k * log(n) # -2*sumLL + k*log(n); 
    
  }
  i_model <- i_model + 1
}

BIC_summ <- as.data.frame(matrix(nrow = length(ms[c(1:10)]), ncol = 3))
colnames(BIC_summ) <- c("model", "mean_BIC", "sd_BIC")
i_model <- 1
for (m in ms[c(1:10)]){
  BIC_summ$model[i_model] <- m
  BIC_summ$mean_BIC[i_model] <- mean(BIC_data[,i_model])
  BIC_summ$sd_BIC[i_model] <- sd(BIC_data[,i_model])
  i_model <- i_model + 1
}
BIC_summ$model <- factor(BIC_summ$model, levels = ms[c(1:10)])
BIC_summ$mean_BIC - BIC_summ$mean_BIC[10]

# plot bargraph
ggplot(BIC_summ) +
  geom_bar( aes(x=forcats::fct_rev(model), y=mean_BIC), stat="identity", fill="skyblue", alpha=0.7) +
  geom_errorbar( aes(x=forcats::fct_rev(model), ymin=mean_BIC-sd_BIC, ymax=mean_BIC+sd_BIC), width=0.4, colour="orange", alpha=0.9, size=1.3) +
  coord_flip(ylim = c(min(BIC_summ$mean_BIC), max(BIC_summ$mean_BIC)+200)) +
  labs(y = "BIC", x = "model") + 
  scale_x_discrete(labels = rev(ms[c(1:10)])) +
  theme_gray(base_size = 24) +
  ggtitle("k = nParam * nSub\nn = nTrials")

# ------------------------------------------------------------------------------
# Check which model best fits de data for each participant.
# ------------------------------------------------------------------------------

individual_cost_data <- as.data.frame(matrix(nrow = length(dI), ncol = length(ms)+1))
colnames(individual_cost_data) <- c("sID", ms)
for (m in ms[c(1:10)]){
  r <- read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T)
  individual_cost_data$sID <- r[,ncol(r)]
  individual_cost_data[,m] <- r[,1]
}

## ALL MODELS
# which models win for how many pp? (unpenalized)
lowest_cost <- c()
for (iSub in c(1:length(dI))) {
  lowest_cost[iSub] <- ms[which.min(individual_cost_data[iSub,2:(length(ms)+1)])]
}
lowest_cost <- as.data.frame(lowest_cost)
ggplot(lowest_cost, aes(x = lowest_cost)) +
  geom_bar()

# penalized (BIC)
individual_BIC_data <- individual_cost_data
params_per_model <- c(0,1,2,3,4,5,5,6,5,5)
for (iSub in c(1:length(dI))) {
  individual_BIC_data$nTrials[iSub] <- length(dI[[iSub]][[1]]) # nTrials needed to calculate BIC
  for (iModel in c(2:(length(ms)+1))) {
    individual_BIC_data[iSub,iModel] <- individual_BIC_data[iSub,iModel] + params_per_model[iModel-1] * log(individual_BIC_data[iSub,"nTrials"])
  }
}
lowest_BIC <- c()
for (iSub in c(1:length(dI))) {
  #lowest_BIC[iSub] <- ms[which.min(individual_BIC_data[iSub,2:(length(ms)+1)])] # compare all models
  lowest_BIC[iSub] <- which.min(individual_BIC_data[iSub,c(5,10)]) # compare selected models
}
lowest_BIC <- ms[c(5,10)][lowest_BIC] # only when comparing selected models
lowest_BIC <- as.data.frame(lowest_BIC)
ggplot(lowest_BIC, aes(x = lowest_BIC)) +
  geom_bar()


# # ------------------------------------------------------------------------------
# # Correlations and differences parameter estimates winning model M3d
# # ------------------------------------------------------------------------------
# 
# r <- read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_M3d_fitE2.txt')), sep = " ", header=T)
# 
# # Correlations between all parameters
# x <- as.matrix(r[,c(2:6)])
# rcorr(x, type="pearson")
# 
# # Difference between alpha 5 and alpha 45
# t.test(r[,2], r[,3], paired = TRUE); mean(r[,2]); mean(r[,3])
# # Difference between n5 * alpha5 and n45 * alpha45
# t.test((r[,2]*5), (r[,3]*45), paired = TRUE); mean(r[,2]*5); mean(r[,3]*45)



## =============================================================================
## 6 Posterior predictives
##    Runs a model with given parameters and returns predicted behavior 
## =============================================================================

# loop over models 
for(m in ms[c(1:10)]){
  dI <- split(d,d$sID)
  ps <- read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T)
  ps <- as.data.frame(ps[,c(-1,-(ncol(ps)))]) # remove first (cost values) and last (sID) column
  
  results <- data.frame()
  for (sub in 1:length(dI)){
    dat <- dI[[sub]] # split by subject
    param <- as.numeric(ps[sub,]) # get subjects params
    results_sub <- eval(call(m, par=param, d=dat, c="ll", mfit = F)) # run model for each subject with given parameters
    results <- rbind(results, results_sub)
  }
  write.table(results, file.path(DIR_this_analysis,prediction.folder,paste0('pred_',m,'_fitE2.txt')))
}


## =============================================================================
## 7 Plot parameter distribution
## =============================================================================

param_names <- c("alpha", "alpha_5", "alpha_45", "theta", "theta_IC", "theta_slope", "theta_low", "theta_med", "theta_high", "stay_bias", "stay_bias_5", "stay_bias_45")
params_in_model <- list(c(), 
                        c(1),
                        c(2,3), 
                        c(2,3,4), 
                        c(2,3,5,6), 
                        c(2,3,7,8,9), 
                        c(2,3,5,6,10),
                        c(2,3,5,6,11,12), 
                        c(2,3,5,6,10),
                        c(2,3,5,6,10))

x_limits <- c(100, 40, 450, 500, 1.00)
y_limits <- c(0.020, 0.18, 0.009, 0.0075, 2.4)
for(i_model in c(10)){
  m <- ms[i_model]
  param_values <- as.data.frame(read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T))
  list_plots <- lapply(c(2:(ncol(param_values)-1)), function(i_param) {
    colname <- colnames(param_values[i_param])
    p <- ggplot(data=param_values, aes(x=get(colname))) + 
      geom_density(fill="grey") + 
      theme_classic(base_size = 16) +
      xlim(0, x_limits[i_param-1]) + ylim(0, y_limits[i_param-1]) + 
      xlab(param_names[params_in_model[[i_model]][i_param-1]]) +
      ylab("density")
  })
  grid.arrange(grobs = list_plots, ncol = (ncol(param_values)-1), top = textGrob(ms[i_model]))
} 


## =============================================================================
## 8 Plot model vs behavior
## =============================================================================

# Correlations predicted vs observed behavior
corr_data <- as.data.frame(matrix(nrow = length(ms[c(1:10)]), ncol = 7))
colnames(corr_data) <- c("model", "E1_r", "E2_r", "S_r", "S_p", "stay_r", "stay_p")
# loop over models 
imodel <- 1
for(m in ms[c(1:10)]){
  output <- read.table(file.path(DIR_this_analysis, prediction.folder, paste0('pred_', m, '_fitE2.txt')), sep = " ", header=T)
  output <- as.data.frame(output)
  # calculate most likely responses for E1 and E2
  for (i in 1:nrow(output)) {
    output$E1[i] <- round((output$blue_self[i]-1)/(output$blue_self[i]+output$red_self[i]-2), digits=2) 
    if("prob_stay" %in% colnames(output)){
      if(runif(1,0,1) < output$prob_stay[i]){ # randomly decide to stay or go, depending on prob_stay
        output$E2[i] <- output$E1[i] 
      } else{
        output$E2[i] <- round((output$blue_post[i]-1)/(output$blue_post[i]+output$red_post[i]-2), digits=2)
      }
    } else {
      output$E2[i] <- round((output$blue_post[i]-1)/(output$blue_post[i]+output$red_post[i]-2), digits=2)
    }
    output$E2[i] <- ifelse(output$E2[i]<0, 0, output$E2[i])
    output$E2[i] <- ifelse(output$E2[i]>1, 1, output$E2[i])
  }
  output$s <- ((round(output$E2,2)*100)-(round(output$E1,2)*100)) / (output$si-(round(output$E1,2)*100))
  
  
  # compare simulations with observed data (first filter out all s == Inf/-Inf and <0 or >1)
  output$s_obs <- d$s
  output$E1_obs <- d$estimate1
  output$E2_obs <- d$estimate2
  output$sID <- d$sID
  output$seen_ratio <- d$seen_ratio
  output$nTotal <- d$nTotal
  assign(paste0("output_",m), output)
  
  #output   <- subset(output,output$s<1)
  #output   <- subset(output,output$s>=0)
  corr_data$model[imodel] <- m
  corr_data$E1_r[imodel] <- cor.test(output$E1_obs,output$E1)$estimate
  # filter out s == 0, because they were randomly drawn and cannot be compared to observed data.
  corr_data$E2_r[imodel] <- cor.test(output$E2_obs[output$s > 0 & output$s_obs > 0], output$E2[output$s > 0 & output$s_obs > 0])$estimate
  
  # use mean data for S and prob stay
  output   <- subset(output,!is.nan(output$s))
  output_agg_s <- output%>%
    dplyr::select(sID, s)%>%
    group_by(sID)%>%
    dplyr::summarise(freq_stay = sum(s==0)/n())
  output_agg_s_obs <- output%>%
    dplyr::select(sID, s_obs)%>%
    group_by(sID)%>%
    dplyr::summarise(freq_stay = sum(s_obs==0)/n())
  if("prob_stay" %in% colnames(output)){
    corr_data$stay_r[imodel] <- cor.test(output_agg_s_obs$freq_stay, output_agg_s$freq_stay)$estimate
    corr_data$stay_p[imodel] <- cor.test(output_agg_s_obs$freq_stay, output_agg_s$freq_stay)$p.value
  }
  
  output   <- subset(output,output$s>0)
  corr_data$S_r[imodel] <- cor.test(as.vector(aggregate(output$s_obs, list(output$sID), FUN=mean)[,2]) , as.vector(aggregate(output$s, list(output$sID), FUN=mean)[,2]))$estimate
  corr_data$S_p[imodel] <- cor.test(as.vector(aggregate(output$s_obs, list(output$sID), FUN=mean)[,2]) , as.vector(aggregate(output$s, list(output$sID), FUN=mean)[,2]))$p.value
  
  imodel <- imodel + 1
}


# Plot predicted vs observed behavior
for(i_model in c(10)){
  m <- ms[i_model]
  df <- get(paste0("output_",m))
  
  
  # ----------------------------------------------------------------------------
  # s across all trials
  # ----------------------------------------------------------------------------
  
  df   <- subset(df,!is.nan(df$s))
  p1 <- 
    ggplot() +
    geom_histogram(data = df, aes(x=s_obs), fill="blue", color = "black", alpha=0.5, binwidth = 0.05) +
    geom_histogram(data = df, aes(x=s), fill="red", color = "black", alpha=0.5, binwidth = 0.05) +
    theme_classic(base_size = 30) +
    coord_cartesian(xlim = c(0, 1)) +
    xlab("social information use") +
    ylab("count") +
    #ggtitle("overall") +
    annotate(geom="text", x=0.5, y=800, label="observed", color="blue") +
    annotate(geom="text", x=0.5, y=750, label="predicted", color="red")
  
  # ----------------------------------------------------------------------------
  # social information use as a function of nTotal and peer confidence
  # ----------------------------------------------------------------------------
  
  df_pred <- df
  summ_pred_i <- summarySE(df_pred, measurevar="s", groupvars=c("nTotal", "conf", "sID"))
  summ_pred <- summarySE(summ_pred_i, measurevar="s", groupvars=c("nTotal", "conf"))
  
  df_obs <- df
  summ_obs_i <- summarySE(df_obs, measurevar="s_obs", groupvars=c("nTotal", "conf", "sID")) 
  summ_obs <- summarySE(summ_obs_i, measurevar="s_obs", groupvars=c("nTotal", "conf")) 
  
  p2 <- 
    # observed
    ggplot(data = summ_obs, aes(x = conf, y = s_obs, color = as.factor(nTotal))) +
    geom_point(size = 2) + 
    geom_errorbar(aes(ymin=s_obs-se, ymax=s_obs+se), size=1, width = 0.3) +
    geom_line(size=1.2) +
    # predicted
    #geom_smooth(data=summ_pred_i[summ_pred_i$conf<3,], method="lm", linetype = 0, aes(x = conf, y = s, fill = as.factor(nTotal))) +
    #geom_smooth(data=summ_pred_i[summ_pred_i$conf>1,], method="lm", linetype = 0, aes(x = conf, y = s, fill = as.factor(nTotal))) +
    geom_point(data=summ_pred, aes(y = s), size = 2) + 
    geom_errorbar(data=summ_pred, aes(y = s, ymin=s-se, ymax=s+se), size=1, width = 0.3) +
    geom_line(data=summ_pred, aes(y = s), size=1.2, linetype = "twodash") +
    theme_classic(base_size = 30) +
    #scale_fill_manual(labels=c("low", "high"),name="own certainty",values = c('#453781FF',"#95D840FF" )) +
    scale_color_manual(labels=c("low", "high"),name="own certainty",values = c('#453781FF',"#95D840FF" )) + 
    coord_cartesian(ylim = c(0,1)) +
    ylab("social information use") + 
    xlab("peer confidence") +
    theme(legend.position = 'none')
  
  
  grid.arrange(p1, p2, ncol = 2, top = textGrob(ms[i_model]))
}


