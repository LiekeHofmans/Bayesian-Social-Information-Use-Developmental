# This script preprocesses data from the Social Network/Media Form from Qualtrics. 
#
# INPUT: 
# There are two files containing raw Qualtrics data, an old and a new one that can be found in the fMRI Mushroom folder (raw_data). 
# The old file contains data from the first set of participants, before we changed Qualtrics account. 
# The new file contains data from all participants who completed the questionnaire after the account-change.
# There are no differences in questions/flow/etc. between the two questionnaires. 
#
# OUTPUT: 
# This script creates one csv file that includes answers from participants who 
# finished the form, from both data files.
# Variables of no interest are removed and some variable names have been renamed.
# A file describing each variable can be found in the same folder as the outputted csv file. 
#
# Written by Lieke Hofmans, July 2023



# LOAD REQUIRED PACKAGES -------------------------------------------------------
list.of.packages <- c("tidyverse", "dplyr", "readr", "data.table", "naniar")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(tidyverse)
library(dplyr)
library(readr)
library(data.table)
library(naniar)
# ------------------------------------------------------------------------------


# SET WORKING DIRECTORY --------------------------------------------------------
#setwd("Z:/fMRI Projects/fMRI Project Mushroom/SocialNetwork data/raw_data")
dir_rawdata <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/raw_data/group" 
dir_bids <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/bids/group/" 
dir_bids_network <- "P:/fMRI Projects/fMRI Project Network Highschool/bids/group/social_media" # throws error if you dont have the network data
dir_checklistfile <- "P:/fMRI Projects/fMRI Project Mushroom Highschool/participant_recruitment/logbook_recruitment_mushroom_study.csv"# this is usually pw protected; convert to readable csv first (and remove when no longer needed)
# ------------------------------------------------------------------------------

### IMPORT RAW DATA ------------------------------------------------------------
SocialMediaDataComplete <- read.csv(file.path(dir_rawdata, "SocialMedia+-+Adolescents+(mushroom)_February+16,+2024_03.44.csv"), na.strings = c("", "NA"), encoding = "UTF-8") 
SocialMediaDataNetwork <- read.csv(file.path(dir_bids_network, "group_qnr-socialmedia.csv"), na.strings = c("", "NA"), encoding = "UTF-8") # Already bidsified data

checklistfile <-
  read.csv(dir_checklistfile,
           sep = ",",
           na.strings = c("", "NA")) 
checklistfile <- checklistfile[complete.cases(checklistfile$ResID..informed.consent.form.),]

# ------------------------------------------------------------------------------


### CLEAN QUESTIONNAIRE DATA ---------------------------------------------------

# Qualtrics sometimes inserted whitespace in front of ppID --> remove whitespace
SocialMediaDataComplete$ppID <-
  trimws(SocialMediaDataComplete$ppID, which = c("both"))

# Remove participants who did not completely fill in questionnaire and variables of no interest 
SocialMediaDataComplete <- SocialMediaDataComplete %>%
  filter(!is.na(ppID)) %>%
  select(finished_SMQ, RecordedDate, Duration..in.seconds., GREWUP_1:ppID)

# Test if ppIDs in social media data match those in checklist file
checklistfile <- checklistfile %>%
  filter(!is.na(Date.social.media.questionnaire))
removeIDs <- which(!SocialMediaDataComplete$ppID %in% checklistfile$ResID..informed.consent.form.)
removeIDs <- SocialMediaDataComplete$ppID[removeIDs]; removeIDs

##########################################################################################################################
##########################################################################################################################
###### Check manually what went wrong, fix it, and run code again until no items left, before moving on to next step #####
# R_3KSD8lOrK0Ign1f = actually VMBO student; should be removed
SocialMediaDataComplete$ppID[SocialMediaDataComplete$ppID=="R_3PdEsWTGpf2mzU5"] <- "R_2dWOsiM7JyNjmIy (R_3PdEsWTGpf2mzU5)"
SocialMediaDataComplete$ppID[SocialMediaDataComplete$ppID=="R_1gISesV5YeRhgNy"] <- "R_1Ebsft0n6isNOKd (R_1gISesV5YeRhgNy)"
SocialMediaDataComplete$ppID[SocialMediaDataComplete$ppID=="R_2uQwVIJ8OWAK9Au"] <- "R_1q3bfknHdB8kiwH / R_2uQwVIJ8OWAK9Au"

##########################################################################################################################
##########################################################################################################################

# remove people who are in social media data but should be removed
SocialMediaDataComplete <- SocialMediaDataComplete[!SocialMediaDataComplete$ppID %in% removeIDs,]

# Replace ppIDs with subject ID and bring to front
SocialMediaDataComplete$ppID <- checklistfile$sID[match(SocialMediaDataComplete$ppID, checklistfile$ResID..informed.consent.form.)]
SocialMediaDataComplete <- SocialMediaDataComplete %>%
  dplyr::rename(sID = ppID) %>%
  relocate(sID) %>%
  arrange(sID)

# Remove double/triple sIDs
# Manually, cause I dont have time
SocialMediaDataComplete <- SocialMediaDataComplete[-c(10,29,31,33,37,39,50,54,59,68,74,77,78,80,83,89,93,94,105,112,117,122,134),]

# Rename variables 
# -as required by Digymatex consortium
dimy_variables <- c("autonomy_c1", "autonomy_c2", "autonomy_c3",	"autonomy_w1",	"autonomy_w2",	"autonomy_w3",	
                    "literacy_1",	"literacy_2",	"literacy_3",	"growth_1",	"growth_2",	"growth_3",	"risk_1",	"risk_2",	"risk_3",	
                    "emotion_n1",	"emotion_n2",	"emotion_n3",	"emotion_a1",	"emotion_a2",	"emotion_a3",	
                    "support_1", "support_2",	"support_3",	"support_4",	"respect_1",	"respect_2",	"respect_3",	"respect_4", 
                    "citizenship_1", "citizenship_2", "citizenship_3")
setnames(SocialMediaDataComplete, 
         old = colnames(subset(SocialMediaDataComplete, select = Autonomy.in.Choice_1:Digital.Citizenship_3)), 
         new = dimy_variables)
# -to English
setnames(SocialMediaDataComplete, 
         old = c("Duration..in.seconds.", "MEDIA_USE_channels_1", "MEDIA_USE_channels_2", "MEDIA_USE_channels_3", "MEDIA_USE_channels_4", "MEDIA_USE_channels_5", "MEDIA_USE_channels_6", "Geslacht", "Leeftijd", "Educatie"), 
         new = c("duration_secs", "MEDIA_USE_twitter", "MEDIA_USE_instagram", "MEDIA_USE_whatsapp", "MEDIA_USE_snapchat", "MEDIA_USE_facebook", "MEDIA_USE_tiktok", "gender", "age", "education"))

# Recode values to numeric
recode_media_use <- function(df_col) (recode(df_col, "nooit" = 1, "om de paar weken" = 2, "minder dan 15 minuten per dag" = 3, "15-30 minuten per dag" = 4, 
                                             "30-60 minuten per dag" = 5, "1-2 uur per dag" = 6, "2-4 uur per dag" = 7, "meer dan 4 uur per dag" = 8))
recode_CIUS <- function(df_col) (recode(df_col, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5))
recode_dymi <- function(df_col) (recode(df_col, "Nooit" = 1, "Zelden" = 2, "Soms" = 3, "Vaak" = 4, "Altijd" = 5, 
                                        "Helemaal niet waar voor mij" = 1, "Niet echt waar voor mij" = 2, "Niet waar of onwaar voor mij" = 3, "Meestal waar voor mij" = 4, "Erg waar voor mij" = 5))
recode_lifesatisfaction <- function(df_col) (recode(df_col, "Helemaal ontevreden" = 1, "Behoorlijk ontevreden" = 2, "Een beetje ontevreden" = 3, 
                                                    "Niet ontevreden en niet tevreden" = 4, "Een beetje tevreden" = 5, "Behoorlijk tevreden" = 6, "Helemaal tevreden" = 7))

SocialMediaDataComplete <- SocialMediaDataComplete %>% mutate(
    SCWEEK=recode(SCWEEK, "Geen - Ik word niet eenzaam" = 1, "In de buurt van mensen zijn, zelfs als ik niet met ze praat" = 2, 
                       "Informele praatjes, b.v. met een winkelbediende of kapper" = 3,  "…Èn gesprek per week met een vriend / vrienden" = 4, 
                       "Twee of drie gesprekken per week met een vriend / vrienden" = 5, "…Èn gesprek per dag met een vriend / vrienden" = 6, 
                       "Twee of drie gesprekken per dag met een vriend / vrienden" = 7, "Meer dan bovenstaande" = 8),
    TWIT1=recode(TWIT1, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5),
    INSTA1=recode(INSTA1, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5),
    SNAP1=recode(SNAP1, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5),
    TT1=recode(TT1, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5),
    FB1=recode(FB1, "nooit" = 1, "zelden" = 2, "soms" = 3, "vaak" = 4, "heel vaak" = 5),
    MEDIA_USE0=recode(MEDIA_USE0, "Ja" = 1, "Nee" = 0),
    MEDIA_USE1=recode(MEDIA_USE1, "nooit" = 1, "1 dag per week of minder" = 2, "2-3 dagen per week" = 3, "(bijna) dagelijks" = 4),
    MEDIA_USE2=recode(MEDIA_USE2, "Ik gebruik geen social media" = 1, "minder dan 1 uur" = 2, "1-2 uur" = 3, "2-4 uur" = 4, "4-6 uur" = 5, "6-8 uur" = 6, "8 uur of meer" = 7),
    MEDIA_OTHER1=recode(MEDIA_OTHER1, "Ja" = 1, "Nee" = 0),
    gender=recode(gender, "man" = 1, "Man" = 1, "vrouw" = 2, "Vrouw" = 2, "Anders" = 3),
    education=recode(education, "VMBO" = 1, "VMBO/HAVO" = 2, "HAVO" = 3, "HAVO/VWO" = 4, "havo/vwo" = 4, "VWO/Gymnasium" = 5),
    across(matches("MEDIA_USE_"), recode_media_use),
    across(matches("CIUS"), recode_CIUS),
    across(matches(dimy_variables), recode_dymi), 
    across(matches("LifeSatisfaction"), recode_lifesatisfaction)
)
# ------------------------------------------------------------------------------

# Add social media data from people who already filled in questionnaire during network study
for (iNetworkpp in SocialMediaDataComplete$sID[is.na(SocialMediaDataComplete$SCWEEK)]){
  sID_network <- checklistfile$sID.network.study[checklistfile$sID==iNetworkpp]
  if (!is.na(sID_network)>0) {
    SMdata_network <- SocialMediaDataNetwork[SocialMediaDataNetwork$sID==sID_network,] %>%
      select(RecordedDate:LifeSatisfaction_6)
    SocialMediaDataComplete[SocialMediaDataComplete$sID==iNetworkpp, which(names(SocialMediaDataComplete)=="RecordedDate"):which(names(SocialMediaDataComplete)=="LifeSatisfaction_6")] <- SMdata_network
  }
}
SocialMediaDataComplete <- SocialMediaDataComplete %>%
  filter(!is.na(SCWEEK)) %>%
  distinct(sID, .keep_all = TRUE) %>%
  select(-finished_SMQ)
# ------------------------------------------------------------------------------


# Reformat RecordedDate to time between completion of questionnaire and fMRI scan
OverviewTestDates <- SocialMediaDataComplete[,c("sID", "RecordedDate")]
OverviewTestDates$ScanDate <- checklistfile$Date.MRI.session[match(SocialMediaDataComplete$sID, checklistfile$sID)]
OverviewTestDates$RecordedDate <- sub(" .*", "", OverviewTestDates$RecordedDate)
OverviewTestDates$ScanDate <- sub(" .*", "", OverviewTestDates$ScanDate)
OverviewTestDates$RecordedDate <- strptime(as.character(OverviewTestDates$RecordedDate), "%Y-%m-%d")
OverviewTestDates$ScanDate <- strptime(as.character(OverviewTestDates$ScanDate), "%d-%m-%Y")


SocialMediaDataComplete$RecordedDate <- as.integer(round((difftime(OverviewTestDates$ScanDate, OverviewTestDates$RecordedDate))))
SocialMediaDataComplete <- dplyr::rename(SocialMediaDataComplete, test_delay_days = RecordedDate)
# ------------------------------------------------------------------------------


# CREATE COMPLEMENTARY DEIDENTIFIED DATAFILE -----------------------------------
SocialMediaDataDeidentified <- SocialMediaDataComplete %>% 
  replace_with_na_at(c("GREWUP_1", "NSSQ", "DBNR", "MEDIA_NAMES"), condition = ~is.character(.x))
# ------------------------------------------------------------------------------


# SAVE DATA IN BIDS FOLDER -----------------------------------------------------
write_csv(SocialMediaDataComplete, file.path(dir_bids, "group_qnr-socialmedia.csv"))
write_csv(SocialMediaDataDeidentified, file.path(dir_bids, "group_qnr-socialmedia_deidentified.csv"))
# ------------------------------------------------------------------------------

