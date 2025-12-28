# This script moves raw behavioral data to the bids folder and structure. 
#
# INPUT: 
# Raw data files for the mushroom, spatial working memory and reversal learning task. 
# 
# OUTPUT: 
# Bidsified data files.  
#
# Written Lieke Hofmans, October 2022



# LOAD REQUIRED PACKAGES -------------------------------------------------------
rm(list = ls())
list.of.packages <- c("tidyverse", "dplyr", "readr", "data.table", "naniar")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(tidyverse)
library(dplyr)
library(readr)
# ------------------------------------------------------------------------------


# SET DIRECTORIES --------------------------------------------------------
project_wd <- "P:/fMRI Projects/fMRI Project Mushroom Highschool"
setwd(project_wd)

rawdata_dir <- file.path(project_wd, "raw_data")
bids_dir <- file.path(project_wd, "bids")

# ------------------------------------------------------------------------------


# CREATE FUNCTION TO MOVE DATA -------------------------------------------------

copy_file <- function(from, to) {
  todir <- dirname(to)
  if (!isTRUE(file.info(todir)$isdir)) dir.create(todir, recursive=TRUE)
  file.copy(from = from, to = to)
}


# ------------------------------------------------------------------------------


### MOVE DATA FOR EACH PARTICIPANT ---------------------------------------------

list_subjects <- list.dirs(path = rawdata_dir, full.names = FALSE, recursive = FALSE)
list_subjects <- list_subjects[grepl("sub-[2-8][0-9]{2}", list_subjects)]
for (iSubject in list_subjects){
  # mushroom behavioral data
  list_rounds <- list.files(path = file.path(rawdata_dir, iSubject, "mushroom"), pattern = "sub-.*_task-mushroom_run-.*_beh.*.csv", full.names = TRUE)
  for (iRound in list_rounds) {
    if (length(iRound)>0){
      to_file <- basename(iRound)
      copy_file(iRound, file.path(bids_dir, iSubject, "beh", to_file))
    }
  }
  # mushroom events data
  list_rounds <- list.files(path = file.path(rawdata_dir, iSubject, "mushroom"), pattern = "sub-.*_task-mushroom_run-.*_events.*.tsv", full.names = TRUE)
  for (iRound in list_rounds) {
    if (length(iRound)>0){
      to_file <- basename(iRound)
      copy_file(iRound, file.path(bids_dir, iSubject, "func", to_file))
    }
  }
  # spatial working memory
  from_file <- list.files(path = file.path(rawdata_dir, iSubject, "spatialWM"), pattern = "sub-.*_task-spatialWM_beh.*.csv", full.names = TRUE)
  if (length(from_file)>0){
    to_file <- basename(from_file)
    copy_file(from_file, file.path(bids_dir, iSubject, "beh", to_file))
  }
  # Reversal learning
  from_file <- list.files(path = file.path(rawdata_dir, iSubject, "reversalLearning"), pattern = "sub-.*_task-reversalLearning_beh.*.csv", full.names = TRUE)
  if (length(from_file)>0){
    to_file <- basename(from_file)
    copy_file(from_file, file.path(bids_dir, iSubject, "beh", to_file))
  }
}

# ------------------------------------------------------------------------------

