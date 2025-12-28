# Short script to combine all behavioral mushroom data with computational parameters and
# parameter-based variables. 
#
# Input:
# - mushroom data with almost all trials for fMRI: group_task-mushroom_preproc-trialwise_allTrials.csv
# - computational parameter values per participant: subject_M3c_fitE2.txt
# - List with participants to exclude: participants_to_exclude.csv
#
# Output:
# - Dataset with mushroom data, parameter values and model-based individual variables: 
# group_task-mushroom_preproc-trialwise-params_forfMRI.csv
#
# These new model-based variables can be used to correlate with fMRI BOLD signal.
#
# Written by Lieke Hofmans, July 2024

# ==============================================================================
# User input
# ==============================================================================
# directories
setwd("P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis")
analysis_wd <- getwd()
beh_dir <- file.path("P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/derivatives/beh/mushroom")
# ------------------------------------------------------------------------------


# ==============================================================================
# packages (no idea which ones are actually necessary) 
# ==============================================================================
library("tidyr")
library("readr")
library("dplyr")
library("tidyverse")
library("ggpubr")
library("philentropy")
# ------------------------------------------------------------------------------


# ==============================================================================
# load data
# ==============================================================================
df_mushroom <- read.csv(file.path(beh_dir, "group_task-mushroom_preproc-trialwise_allTrials.csv"))
df_mushroom_compparams <- read_delim(file.path(analysis_wd, "04_level-group/mushroom/results_fit_sample/subject_M3d_fitE2.txt"), delim = " ")
participants_to_exclude <- read.csv(file.path(analysis_wd, "participants_to_exclude.csv"))

# Define parameter names
df_mushroom_compparams <- df_mushroom_compparams[,-1] %>%
  separate(V7, into = c("x", "y"), sep = " ")
colnames(df_mushroom_compparams) <- c("cost", "alpha_5", "alpha_45", "theta_IC", "theta_slope", "staybias", "sID")
df_mushroom_compparams$staybias <- as.numeric(df_mushroom_compparams$staybias)
# ------------------------------------------------------------------------------


# ==============================================================================
# Compute parameter-based variables 
# ==============================================================================

# First, define perceived red and blue mushrooms, according to parameter values (model-based alternative for certainty/confidence condition)
df_mushroom <- merge(df_mushroom, df_mushroom_compparams[,c("sID", "alpha_5", "alpha_45", "theta_IC", "theta_slope", "staybias")])
for (i in 1:nrow(df_mushroom)) {
  if (df_mushroom$nTotal[i] == 5){
    df_mushroom$perceived_blue[i] <- df_mushroom$estimate1[i]/100 * df_mushroom$nTotal[i] * df_mushroom$alpha_5[i]
    df_mushroom$perceived_red[i] <- (1-df_mushroom$estimate1[i]/100) * df_mushroom$nTotal[i] * df_mushroom$alpha_5[i]
  } else {
    df_mushroom$perceived_blue[i] <- df_mushroom$estimate1[i]/100 * df_mushroom$nTotal[i] * df_mushroom$alpha_45[i]
    df_mushroom$perceived_red[i] <- (1-df_mushroom$estimate1[i]/100) * df_mushroom$nTotal[i] * df_mushroom$alpha_45[i]
  }
}
df_mushroom$other_blue <- df_mushroom$estimate_peer/100 * (df_mushroom$theta_IC + df_mushroom$theta_slope * (df_mushroom$confidence_peer-1))
df_mushroom$other_red <-  (1-df_mushroom$estimate_peer/100) * (df_mushroom$theta_IC + df_mushroom$theta_slope * (df_mushroom$confidence_peer-1))


# ------------------------------------------------------------------------------

# ==============================================================================
# Save new dataframe
# ==============================================================================
df_mushroom <- df_mushroom[!df_mushroom$sID %in% participants_to_exclude$exclude_fmri,]
write_csv(df_mushroom, file.path(beh_dir, "group_task-mushroom_preproc-trialwise-params_forfMRI_allTrials.csv"))
# ------------------------------------------------------------------------------
