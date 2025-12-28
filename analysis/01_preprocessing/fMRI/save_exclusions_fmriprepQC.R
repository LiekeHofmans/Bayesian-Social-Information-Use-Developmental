library("rjson")
library("reshape2")
library("tidyverse")

# Preprocessed fMRI data was quality checked by Lieke Hofmans,
# as either "yes" (=include), "no" (=exclude), or "uncertain" (=discuss).


# New ratings Rater 3 (Lieke Hofmans)
ratings <- fromJSON(file = "P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/derivatives/mri/fmriprep/exclude.json")
ratings <- as.data.frame(ratings)
# remove t1 information (which was good for everyone)
skull_strip_elements <- which(ratings == "skull_strip_report")
skull_strip_elements <- c(skull_strip_elements-1, skull_strip_elements, skull_strip_elements+1)
t1_norm_rpt_elements <- which(ratings == "t1_norm_rpt")
t1_norm_rpt_elements <- c(t1_norm_rpt_elements-1, t1_norm_rpt_elements, t1_norm_rpt_elements+1)
ratings <- ratings[c(-skull_strip_elements, -t1_norm_rpt_elements)]
# reformat data
run <- t(ratings[, grepl("run", names(ratings))])
sub <- t(ratings[, grepl("sub", names(ratings))])
type <- t(ratings[, grepl("type", names(ratings))])
rating <- t(ratings[, grepl("rating", names(ratings))])
ratings <- as.data.frame(cbind(sub, run, type, rating))
colnames(ratings) <- c("sub", "run", "type", "rating")


# Save which participants should be excluded
failed_QC <- sort(unique(ratings$sub[ratings$rating == "bad"]))
participants_to_exclude <- read.csv("P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis/participants_to_exclude.csv")
participants_to_exclude <- add_row(participants_to_exclude, exclude_fmri = as.numeric(failed_QC), reason = rep("Failed fmriprep QC", length(failed_QC)))
write_csv(participants_to_exclude, "P:/fMRI Projects/fMRI Project Mushroom Highschool/analysis/participants_to_exclude.csv")

