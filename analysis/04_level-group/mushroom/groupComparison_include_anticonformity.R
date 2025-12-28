
# Clear working directory
rm(list = ls())

library("tidyverse")
library("dplyr")
library("lmerTest")
library("viridis")
library("emmeans")
library("ggeffects")
library("car")

# Set directories
DIR_root_adolescents <- "P:/fMRI Projects/fMRI Project Mushroom Highschool"
DIR_analysis_main <- file.path(DIR_root_adolescents, "analysis")
DIR_this_analysis <- file.path(DIR_analysis_main, "04_level-group/mushroom")
DIR_data <- file.path(DIR_root_adolescents, "bids/derivatives/beh/mushroom")

DIR_root_adults <- "P:/fMRI Projects/fMRI Project Mushroom" # (ADAPT)                     
DIR_adult_analysis_main <- file.path(DIR_root_adults, "analysis")
DIR_adult_analysis <- file.path(DIR_adult_analysis_main, "04_level-group/mushroom")
DIR_adult_data <- file.path(DIR_root_adults, "bids/derivatives/beh/mushroom")

# Load behavioral data: task
df_mushroom_adolescents <- read.csv(file.path(DIR_data, "group_task-mushroom_preproc-trialwise_include_anticonformity.csv"))
df_mushroom_adults <- read.csv(file.path(DIR_adult_data, "group_task-mushroom_preproc-trialwise_include_anticonformity.csv"))
df_all <- rbind(df_mushroom_adolescents, df_mushroom_adults)
df_all$group <- ifelse(df_all$sID < 200, "adults", "adolescents")

# Load demographics
df_age_adolescents <- read.csv(file.path(DIR_root_adolescents, "bids/derivatives/qnr/demographics/group_demographics.csv"))
df_age_adults <- read.csv(file.path(DIR_root_adults, "bids/derivatives/qnr/demographics/group_demographics.csv"))
df_age <- rbind(df_age_adolescents, df_age_adults)

# Combine behavioral and demographic data
df_all <- left_join(df_all, df_age, by = "sID")


## =============================================================================
## Compare model free behavior adolescents with adults
## =============================================================================

df_all$confidence_peer_c <- df_all$confidence_peer-2 # set medium confidence to 0
df_all$nTotal_ind <- as.numeric(ifelse(df_all$nTotal==5, -0.5, 0.5)) # change to: uncertain = -0.5; certain = 0.5
df_all$group_ind <- as.numeric(ifelse(df_all$group=="adults", -0.5, 0.5)) # change to: adults = -0.5; adolescents = 0.5
df_all$deviance <- abs(df_all$true_ratio*100 - df_all$estimate1)


# Effects on social information use
# =================================
# LMER group comparison
fit_age <- lmerTest::lmer(s ~ nTotal_ind*confidence_peer_c*group_ind + 
                                    (1 + nTotal_ind*confidence_peer_c| sID),
                                  data=df_all, 
                                  control = lmerControl(optimizer = "nloptwrap", optCtrl=list(maxfun=2e5)))
summary(fit_age) 

