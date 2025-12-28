# This script combines the fMRI timingfiles with participants' individual behavioral/computational parameters. 
# These parameters can then be used as parametric regressors for the BOLD analysis.
# 
# INPUT: 
# - One timingfile per participant per fMRI run (= 3 files per participant).
# - One file with all behavioral/computational information. 
#
# OUTPUT: 
# - Output files per participant per fMRI run that specifies the condition, convolved with their individual parameter information.
#
# Written by Lieke Hofmans, July 2024

# ==============================================================================
# USER INPUT
# ==============================================================================
# Define directories and filenames
parameter_dir <- "/home/lhofman/fmg-research-mount/mushroom_highschool/bids/derivatives/beh/mushroom/group_task-mushroom_preproc-trialwise-params_forfMRI_allTrials.csv" # individual behavioral/computational parameters
bids_dir <- "/home/lhofman/fmg-research-mount/mushroom_highschool/bids"  # directory where one folder per subject can be found with fMRI timing files
# ==============================================================================


# Load required packages
# ==============================================================================
library("readr")


# Load data and combine datasets
# ==============================================================================

df_params <- read.csv(parameter_dir)
df_params$perceived_certainty <- df_params$perceived_blue + df_params$perceived_red
df_params$perceived_confidence <- df_params$other_blue + df_params$other_red

for (iSubject in unique(df_params$sID)) {
  iSub <- paste("sub-", sprintf("%03d", iSubject), sep="")
  
  for (iRun in c(1,2,3)) {
    if (file.exists(file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_events.tsv", sep="")))) {
      df_params_thisRun <- df_params[df_params$sID==iSubject & df_params$run==iRun,]
      df_timing <- read_delim(file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_events.tsv", sep="")), delim="\t", show_col_types = FALSE)
      df_timing <- df_timing[df_timing$trial_number %in% df_params_thisRun$trial_number,]
      
      # Select relevant columns
      # 1. Own certainty at first estimate (E1) 
      lowCertaintyE1 <- cbind(df_timing$onset_estimate1[startsWith(df_timing$trial_type, "low_")], 0.5, "1")
      highCertaintyE1 <- cbind(df_timing$onset_estimate1[startsWith(df_timing$trial_type, "high_")], 0.5, "1")
      # 1b. Own certainty at social information (SI) 
      lowCertaintySI <- cbind(df_timing$onset_SI[startsWith(df_timing$trial_type, "low_")], df_timing$duration_SI[startsWith(df_timing$trial_type, "low_")], "1")
      highCertaintySI <- cbind(df_timing$onset_SI[startsWith(df_timing$trial_type, "high_")], df_timing$duration_SI[startsWith(df_timing$trial_type, "high_")], "1")
      
      # 2. Peer confidence at SI
      parametricConfidenceSI <- cbind(df_timing$onset_SI[df_timing$filler_trial==0], df_timing$duration_SI[df_timing$filler_trial==0], df_timing$trial_type[df_timing$filler_trial==0])
      parametricConfidenceSI[,3] <- setNames(c("-1", "-1", "0", "0", "1", "1"), c("low_low", "high_low", "low_medium", "high_medium", "low_high", "high_high"))[parametricConfidenceSI[,3]]


      # 3. Select computational parameters
      params_perceivedCertainty <- cbind(df_timing$onset_estimate1, 0.5, scale(df_params_thisRun$perceived_certainty, scale=F))
      params_perceivedCertaintySI <- cbind(df_timing$onset_SI, df_timing$duration_SI, scale(df_params_thisRun$perceived_certainty, scale=F))
      params_perceivedConfidence <- cbind(df_timing$onset_SI[df_timing$filler_trial==0], df_timing$duration_SI[df_timing$filler_trial==0], scale(df_params_thisRun$perceived_confidence[df_params_thisRun$filler_trial==0], scale=F))
      
        
      # ========================================================================
      # save files
      write.table(lowCertaintyE1, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_condition-lowCertaintyE1_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      write.table(highCertaintyE1, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_condition-highCertaintyE1_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      write.table(lowCertaintySI, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_condition-lowCertaintySI_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      write.table(highCertaintySI, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_condition-highCertaintySI_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      
      write.table(parametricConfidenceSI, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_condition-parametricConfidenceSI_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      

      write.table(params_perceivedCertainty, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_params-perceivedCertainty_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      write.table(params_perceivedCertaintySI, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_params-perceivedCertaintySI_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")
      write.table(params_perceivedConfidence, file=file.path(bids_dir, iSub, "func", paste(iSub, "_task-mushroom_run-", iRun, "_params-perceivedConfidence_events.txt", sep="")), sep=" ", col.names=FALSE, row.names=FALSE, quote=FALSE, na="")

    }
  }
}
