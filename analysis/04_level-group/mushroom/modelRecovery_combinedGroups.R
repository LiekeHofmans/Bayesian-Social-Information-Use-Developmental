
## =============================================================================
## Set up script
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
if(!require(snowfall,quietly = T)) install.packages('reshape2')
if(!require(snowfall,quietly = T)) install.packages('ggdist')
require(snowfall)
require(tidyverse)
require(viridis)
require(grid)
require(gridExtra)
require(ggpubr)
require(Hmisc)
require(reshape2)
require(ggdist)

# Set directories
DIR_analysis_main <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis"
DIR_this_analysis <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis/04_level-group/mushroom"
DIR_data <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/derivatives/beh/mushroom"
DIR_adult_analysis_main <- "P:/fMRI Projects/fMRI Project Mushroom/analysis"
DIR_adult_analysis <- "P:/fMRI Projects/fMRI Project Mushroom/analysis/04_level-group/mushroom"
DIR_adult_data <- "P:/fMRI Projects/fMRI Project Mushroom/bids/derivatives/beh/mushroom"
fit.folder <- 'results_fit_sample'
prediction.folder <- 'results_pred' 
simulation.folder <- 'results_sim'

source(file.path(DIR_analysis_main, "summary_function.R"))

# Load data
df_mushroom_adolescents <- read.csv(file.path(DIR_data, "group_task-mushroom_preproc-trialwise.csv"))
df_mushroom_adults <- read.csv(file.path(DIR_adult_data, "group_task-mushroom_preproc-trialwise.csv"))
d <- rbind(df_mushroom_adults, df_mushroom_adolescents)

## =============================================================================
## Models
##     Define models and limits
## =============================================================================

# Load models
source(file.path(DIR_this_analysis, "model_specification.R"))

# Load helper functions
source(file.path(DIR_this_analysis, "helper_functions.R"))

## =============================================================================
## Model recovery. 
## =============================================================================

# ------------------------------------------------------------------------------
# Generate individual parameter values: uniform between real min and max
# ------------------------------------------------------------------------------

set.seed(123)
for(m in ms[c(2:10)]){
  param_values <- rbind(
    read.table(file.path(DIR_adult_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T), # adults
    read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_', m, '_fitE2.txt')), sep = " ", header=T) # adolescents
  )
  
  simulated_param_values <- list()
  
  for (col in 2:(ncol(param_values) - 1)) {
    x <- param_values[[col]]
    
    # Remove NA just in case
    x_clean <- x[!is.na(x)]
    
    # Identify and remove outliers (±3 SD from the mean)
    mu <- mean(x_clean)
    stdev <- sd(x_clean)
    x_no_outliers <- x_clean[x_clean >= (mu - 3*stdev) & x_clean <= (mu + 3*stdev)]
    
    # Get min and max after outlier removal
    min_val <- min(x_no_outliers)
    max_val <- max(x_no_outliers)
    
    # Generate uniform distribution: same length as number of subjects and values uniformly distributed from min to max after outlier removal
    simulated_param_values[[colnames(param_values)[col]]] <- runif(length(unique(d$sID)), min = min_val, max = max_val)
  }
  
  # Change name of dataset according to model
  assign(paste0("simulated_param_values_", m), simulated_param_values)
}

# ------------------------------------------------------------------------------
# Create subjective task parameters based on individual parameter values
# ------------------------------------------------------------------------------

set.seed(123)
dI <- split(d,d$sID)
for(m in ms[c(2:10)]){
  simulated_param_values <- get(paste0('simulated_param_values_', m))
  
  results <- data.frame()
  for (sub in 1:length(dI)){
    dat <- dI[[sub]] # split by subject
    params <- as.numeric(sapply(simulated_param_values, `[`, sub))
    results_sub <- eval(call(m, par=params, d=dat, c="ll", mfit = F)) # run model for each subject with given parameters
    results <- rbind(results, results_sub)
  }
  write.table(results, file.path(DIR_this_analysis,simulation.folder,paste0('sim_generatedFrom',m,'.txt')))
}

# ------------------------------------------------------------------------------
# Create simulated behavior based on predicted subjective task parameters
# ------------------------------------------------------------------------------

# Helper function to load and process simulation data
process_model_data <- function(model_name, d, prob_stay_model = FALSE) {
  # Load prediction data
  simulated_data <- read.table(file.path(DIR_this_analysis, simulation.folder, paste0('sim_generatedFrom', model_name, '.txt')), sep = " ", header = TRUE)
  
  # Calculate E1 and E2
  simulated_data$E1 <- round((simulated_data$blue_self - 1) / (simulated_data$blue_self + simulated_data$red_self - 2), 2) * 100
  simulated_data$E2 <- NA
  
  for (i in 1:nrow(simulated_data)) {
    if (prob_stay_model) {
      if (runif(1) < simulated_data$prob_stay[i]) { # randomly decide to stay or go, depending on prob_stay
        simulated_data$E2[i] <- simulated_data$E1[i]
      } else {
        simulated_data$E2[i] <- round((simulated_data$blue_post[i] - 1) / (simulated_data$blue_post[i] + simulated_data$red_post[i] - 2), 2) * 100
      }
    } else {
      simulated_data$E2[i] <- round((simulated_data$blue_post[i] - 1) / (simulated_data$blue_post[i] + simulated_data$red_post[i] - 2), 2) * 100
    }
    
    # Bound E2 between E1 and peer estimate
    lower <- min(simulated_data$E1[i], d$estimate_peer[i])
    upper <- max(simulated_data$E1[i], d$estimate_peer[i])
    simulated_data$E2[i] <- min(max(simulated_data$E2[i], lower), upper)
  }
  
  # Create simulation dataframe
  dSim <- d
  dSim$estimate2 <- simulated_data$E2
  dSim$s <- (dSim$estimate2 - dSim$estimate1) / (dSim$estimate_peer - dSim$estimate1)
  dSim$s <- ifelse(as.integer(dSim$estimate1) == as.integer(dSim$estimate2), 0, dSim$s)
  
  return(dSim)
}

# List of models with prob_stay flag
model_list <- list(
  M1a = FALSE,
  M1b = FALSE,
  M2a = FALSE,
  M2b = FALSE,
  M2c = FALSE,
  M3a = TRUE,
  M3b = TRUE,
  M3c = TRUE,
  M3d = TRUE  
)

# Generate simulated data from all models
set.seed(123)
for (model in ms[c(2:10)]) {
  assign(paste0("dSim_", model), process_model_data(model, d, prob_stay_model = model_list[[model]]))
}

# ------------------------------------------------------------------------------
# Run fitting procedure: each model is fitted by each model (9x9)
# ------------------------------------------------------------------------------

# Loop through each data-generating model
set.seed(123)
for (gen_model in ms[2:10]) {
  
  dSim <- get(paste0("dSim_", gen_model))
  dI <- split(dSim, dSim$sID)
  
  # Loop over each model used to fit the data
  for (m in ms[2:10]) {
    print(Sys.time())
    t <- proc.time()[3]
    sfInit(TRUE, 7)
    sfExportAll()
    
    fitOn <- "E2"
    r <- sfClusterApplyLB(dI, run)  
    r <- do.call(rbind, r)
    
    print(r)
    print(m)
    sfStop()
    
    # Output file
    output_file <- file.path(DIR_this_analysis, simulation.folder,
                             paste0("combinedExperiments_fit_", m, "_dataGeneratedFrom", gen_model, ".txt"))
    write.table(r, output_file)
    
    cat(round(proc.time()[3] - t, 0), "s to complete ", m, "\n", sep = "")
  }
}


# ------------------------------------------------------------------------------
# Model identifiability based on BIC: confusion matrix
# ------------------------------------------------------------------------------

# Initialize an empty 9x9 confusion matrix
model_names <- ms[c(2:10)] 
confusion_matrix <- matrix(0, nrow = length(model_names), ncol = length(model_names))
colnames(confusion_matrix) <- model_names
rownames(confusion_matrix) <- model_names

# Compute the number of trials per subject
n_trials <- d %>%
  dplyr::count(sID) %>%
  arrange(sID)  # ensures subjects are ordered from 1 to n

# Loop over each generating model (2 through 10)
for (gen_model in model_names) {
  
  # Initialize a matrix to store BIC values for each subject (rows) and fitting model (columns)
  bic_matrix <- matrix(NA, nrow = nrow(n_trials), ncol = length(model_names))
  
  # Loop over each fitting model (2 through 10)
  for (fit_model in model_names) { 
    
    # read the file
    file_path <- file.path(
      DIR_this_analysis, 
      simulation.folder, 
      paste0('combinedExperiments_fit_', fit_model, '_dataGeneratedFrom', gen_model, '.txt')
    )
    r <- read.table(file_path, header=T)
    cost <- r[, 1]  # already -2 * LL
    
    # Compute BIC: BIC = -2LL + k * log(n_trials)
    k <- ncol(r)-2  # n params for fitting model
    bic <- cost + k * log(n_trials$n)
    
    # Store the BIC values in the matrix for the current fitting model and generating model
    bic_matrix[, which(model_names == fit_model)] <- bic
  }
  
  # find the best-fitting model for each subject (the one with the lowest BIC)
  best_models <- apply(bic_matrix, 1, function(row) {
    model_names[which.min(row)]  # Get the model name corresponding to the min BIC
  })
  
  # Count how many times each model was selected
  for (selected_model in model_names) {
    confusion_matrix[gen_model, selected_model] <- sum(best_models == selected_model)
  }
}

# Normalize the confusion matrix to proportions
confusion_matrix_norm <- round(confusion_matrix / rowSums(confusion_matrix), digits = 2)

# Plot results
conf_df <- melt(confusion_matrix_norm)
colnames(conf_df) <- c("GeneratingModel", "RecoveredModel", "Proportion")


conf_df$TextColor <- ifelse(conf_df$Proportion > 0.5, "white", "black") # Create a column for text color based on proportion threshold
ggplot(conf_df, aes(x = factor(RecoveredModel), y = factor(GeneratingModel), fill = Proportion)) +
  geom_tile(color = "white") +
  geom_text(aes(label = sprintf("%.2f", Proportion), color = TextColor), size = 4) +
  scale_color_identity() + 
  scale_fill_viridis_c(option = "D", direction = -1, guide = "none") +
  scale_x_discrete(position = "top") +
  scale_y_discrete(limits = rev) +
  labs(x = "Recovered Model", y = "Generating Model") +
  theme_minimal() +
  theme(axis.text=element_text(size=12), axis.title=element_text(size=14,face="bold"))  


## =============================================================================
## Parameter recovery of winning model: M3d
## =============================================================================

# ------------------------------------------------------------------------------
# Check if data looks ok for winning model M3d
# ------------------------------------------------------------------------------

# SI use as a function of peer confidence and certainty level
summ_sub <- summarySE(dSim_M3d, measurevar="s", groupvars=c("confidence_peer", "nTotal", "sID")) 
summ_group <- summarySE(summ_sub, measurevar="s", groupvars=c("confidence_peer", "nTotal"))
ggplot(data = summ_group, aes(x = as.factor(confidence_peer), y = s, color = as.factor(nTotal))) +
  geom_point(data = summ_sub, size=2, alpha=0.3, position=position_jitterdodge(jitter.width = 0.1, jitter.height=0.01, dodge.width=0.3)) +
  geom_point(size = 2, position=position_dodge(0.3)) + 
  geom_errorbar(aes(ymin=s-se, ymax=s+se), size=1, width = 0.3, position=position_dodge(0.3)) +
  theme_classic(base_size = 16) +
  scale_color_manual(labels=c("low", "high"),name="own certainty",values = c('#453781FF',"#95D840FF" )) + 
  ylab("social information use") + 
  xlab("peer confidence")



# ------------------------------------------------------------------------------
# Correlate generated vs fitted parameters for winning model M3d
# ------------------------------------------------------------------------------

param_names <- c("alpha5", "alpha45", "theta_IC", "theta_slope", "stay_bias")
# Retrieve simulated ("true") parameter values
simulated_values <- as.data.frame(simulated_param_values_M3d)
# Retrieve fitted parameter values based on simulated data
param_values <- as.data.frame(read.table(file.path(DIR_this_analysis, simulation.folder, 'combinedExperiments_fit_M3d_dataGeneratedFromM3d.txt'), sep = " ", header=T))
param_values <- param_values[,2:(ncol(param_values)-1)]


list_plots <- lapply(c(1:(ncol(param_values))), function(i_param) { 
  colname_fit <- colnames(param_values[i_param])
  colname_true <- paste0(colnames(simulated_values[i_param]), "_true")
  df_fitted_true <- as.data.frame(cbind(param_values[i_param], simulated_values[i_param]))
  colnames(df_fitted_true) <- c(colname_fit, colname_true)
  
  p <- ggplot(data=df_fitted_true, aes(x=get(colname_true), y=get(colname_fit))) + geom_jitter(position="jitter", alpha=0.5) + geom_smooth(method="lm") +
    geom_abline(intercept = 0, slope = 1) +
    theme_classic(base_size = 16) +
    stat_cor(method = "pearson", size=4, p.accuracy = 0.001, r.accuracy = 0.01) + 
    xlab("true") + ylab("fitted") + ggtitle(param_names[i_param])
})
grid.arrange(grobs = list_plots, ncol = length(param_names), top = textGrob("M3d"))


# ------------------------------------------------------------------------------
# Correlate generated vs fitted parameters for all models
# ------------------------------------------------------------------------------

for (i_model in model_names) {
  simulated_values <- as.data.frame(get(paste0('simulated_param_values_', i_model)))
  param_values <- as.data.frame(read.table(file.path(DIR_this_analysis, simulation.folder, paste0('combinedExperiments_fit_', i_model,'_dataGeneratedFrom', i_model, '.txt')), sep = " ", header=T))
  param_values <- param_values[,2:(ncol(param_values)-1), drop = FALSE]
  
  print(i_model)
  correlations <- mapply(function(x, y) cor.test(x, y), param_values, simulated_values, SIMPLIFY = TRUE)
  print(correlations)
  cat("\n\n\n")
}


# ------------------------------------------------------------------------------
# Correlations estimated parameters with each other
# ------------------------------------------------------------------------------

params_1 <- as.data.frame(read.table(file.path(DIR_adult_analysis, fit.folder, paste0('subject_M3d_fitE2.txt')), sep = " ", header=T))
params_2 <- as.data.frame(read.table(file.path(DIR_this_analysis, fit.folder, paste0('subject_M3d_fitE2.txt')), sep = " ", header=T))
estimated_params <- rbind(params_1, params_2)

x <- as.matrix(estimated_params[,c(2:6)])
rcorr(x, type="pearson")
