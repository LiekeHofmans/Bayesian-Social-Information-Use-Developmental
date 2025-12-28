# Compare social information use between adolescents and adults in the BEAST
# to see if this is in the same direction as for the mushroom task. 

# Clear working directory
rm(list = ls())

library("tidyverse")
library("dplyr")
library("lmerTest")
library("viridis")
library("parameters")

# Set directories
DIR_analysis_adolescents <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis"
DIR_data_adolescents <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/derivatives/beh/"
DIR_analysis_adults <- "P:/fMRI Projects/fMRI Project Mushroom/analysis"
DIR_data_adults <- "P:/fMRI Projects/fMRI Project Mushroom/bids/derivatives/beh/"

source(file.path(DIR_analysis_adolescents, "summary_function.R"))
source(file.path(DIR_analysis_adolescents, "raincloud_plots.R"))

# Load mushroom data
df_mushroom_adolescents <- read.csv(file.path(DIR_data_adolescents, "mushroom/group_task-mushroom_preproc-trialwise.csv"))
df_mushroom_adults <- read.csv(file.path(DIR_data_adults, "mushroom/group_task-mushroom_preproc-trialwise.csv"))
df_mushroom <- rbind(df_mushroom_adolescents, df_mushroom_adults)
df_mushroom$group <- ifelse(df_mushroom$sID < 200, "adults", "adolescents")

df_mushroom$confidence_peer_c <- df_mushroom$confidence_peer-2 # set medium confidence to 0
df_mushroom$nTotal_ind <- as.numeric(ifelse(df_mushroom$nTotal==5, -0.5, 0.5)) # change to: uncertain = -0.5; certain = 0.5
df_mushroom$group_ind <- as.numeric(ifelse(df_mushroom$group=="adults", -0.5, 0.5)) # change to: adults = -0.5; adolescents = 0.5

# Load BEAST data
df_BEAST_adolescents <- read.csv(file.path(DIR_data_adolescents, "BEAST/group_task-BEAST_preproc-trialwise.csv"))
df_BEAST_adults <- read.csv(file.path(DIR_data_adults, "BEAST/group_task-BEAST_preproc-trialwise.csv"))
df_BEAST <- rbind(df_BEAST_adolescents, df_BEAST_adults)
df_BEAST <- df_BEAST %>% filter(sID %in% df_mushroom$sID)
df_BEAST$group <- ifelse(df_BEAST$sID < 200, "adults", "adolescents")

df_BEAST$group_ind <- as.numeric(ifelse(df_BEAST$group=="adults", -0.5, 0.5)) # change to: adults = -0.5; adolescents = 0.5

# Group differences in social information use in the mushroom task
# ------------------------------------------------------------------------------
summ_mushroom <- summarySE(df_mushroom, measurevar="s", groupvars=c("sID", "group")); mean(summ_mushroom$s) # mean s = 0.38
t.test(summ_mushroom$s ~ summ_mushroom$group) # adolescents: 0.36, adults: 0.39, t(129.1)=-1.37, p = 0.172

fit_mushroom <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c*group_ind + 
                            (1 + nTotal_ind*confidence_peer_c| sID),
                          data=df_mushroom, 
                          control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_mushroom) 
standardize_parameters(fit_mushroom) # standardized betas

# Group differences in social information use in the BEAST
# ------------------------------------------------------------------------------
summ_BEAST <- summarySE(df_BEAST, measurevar="s", groupvars=c("sID", "group")); mean(summ_BEAST$s) # mean s = 0.35
t.test(summ_BEAST$s ~ summ_BEAST$group) # adolescents: 0.38, adults: 0.31, t(126.05)=3.00, p = 0.003

fit_BEAST <- lmerTest::lmer(s ~ group_ind + (1 | sID),
                               data=df_BEAST, 
                               control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_BEAST) 
standardize_parameters(fit_BEAST) # standardized betas

# Plot results
# ------------------------------------------------------------------------------
summ_mushroom$task <- "1"
summ_BEAST$task <- "2"
summ_all <- rbind(summ_mushroom, summ_BEAST)
summ_group <- summarySE(summ_all, measurevar="s", groupvars=c("task", "group"))

ggplot(data = summ_all, aes(x = task, y = s, color = group)) +
  geom_flat_violin(aes(fill = group), alpha = 0.4, position = position_nudge(x = 0.1))+
  geom_line(aes(group = sID, color = group), alpha = 0.5) +
  geom_point(position = position_jitter(width = .05, height = 0), size = 2.5, shape = 20, alpha=0.2)+
  geom_line(data = summ_group, aes(x = task, y = s, color = group, group = group), size = 1.2, position = position_nudge(x = 0.1)) +
  geom_errorbar(data = summ_group, aes(x = task, ymin=s-se, ymax=s+se, color = group), width=0.2, size = 1.5, position = position_nudge(x = 0.1)) +
  geom_point(data = summ_group, aes(x = task, y = s, color = group), size=2.5, position = position_nudge(x = 0.1)) +
  theme_classic(base_size = 30) +
  ylab("social information use") +
  scale_x_discrete(name = "task", labels = c("1"="Mushroom", "2"="BEAST")) +
  theme(legend.position = "none")


# Correlation between social information use in the Mushroom and BEAST tasks
# ------------------------------------------------------------------------------

summ_BEAST <- summ_BEAST %>% dplyr::rename(s_BEAST = s) 
summ_all <- summ_mushroom %>% left_join(summ_BEAST, by = "sID")
cor.test(summ_all$s, summ_all$s_BEAST, use = "complete_obs", method = "pearson") # r = 0.23, p = 0.010


# Variance or noisiness in s in both tasks
# ==============================================================================
mushroom_variances <- df_mushroom %>%
  dplyr::group_by(sID, group_ind, nTotal_ind, confidence_peer_c) %>%
  dplyr::summarise(var_si = var(s, na.rm = TRUE), .groups = "drop")
summary(lm(log(var_si + 0.0000001) ~ group_ind*nTotal_ind*confidence_peer_c, data = mushroom_variances)) # add small error to s to avoid log(0)

BEAST_variances <- df_BEAST %>%
  dplyr::group_by(sID, group) %>%
  dplyr::summarise(var_BEAST = var(s, na.rm = TRUE), .groups = "drop")
summary(lm(log(var_BEAST + 0.0000001) ~ group, data = BEAST_variances)) 


