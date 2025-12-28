#!/usr/bin/python

# A quick quality check on the level 1 results. 

import os
import glob

############################################ USER INPUT ##############################################
#######################################################################################################
outfile_certaintyE1_confidence='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/QA/lev1_QA_certaintyE1_confidence.html'
all_feats_certaintyE1_confidence=glob.glob('/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/sub*/certaintyE1_confidence/run-*_output.feat/')
outfile_certaintySI_confidence='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/QA/lev1_QA_certaintySI_confidence.html'
all_feats_certaintySI_confidence=glob.glob('/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/sub*/certaintySI_confidence/run-*_output.feat/')


outfile_perceived_certaintyE1_confidence='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/QA/lev1_QA_perceived_certaintyE1_confidence.html'
all_feats_perceived_certaintyE1_confidence=glob.glob('/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/sub*/perceived_certaintyE1_confidence/run-*_output.feat/')
outfile_perceived_certaintySI_confidence='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/QA/lev1_QA_perceived_certaintySI_confidence.html'
all_feats_perceived_certaintySI_confidence=glob.glob('/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/sub*/perceived_certaintySI_confidence/run-*_output.feat/')

# which models to run
do_certaintyE1_confidence=1
do_certaintySI_confidence=1
do_perceived_certaintyE1_confidence=1
do_perceived_certaintySI_confidence=1

#######################################################################################################


# Save all images for all subjects to html file.

# certaintyE1_confidence
if do_certaintyE1_confidence:
    os.system("rm %s"%(outfile_certaintyE1_confidence))

    f = open(outfile_certaintyE1_confidence, "w")
    for file in list(all_feats_certaintyE1_confidence):
      f.write("<p>============================================")
      f.write("<p>%s<br>"%(file))
      f.write("<IMG SRC=\"%s/design.png\">"%(file))
      f.write("<IMG SRC=\"%s/design_cov.png\" >"%(file))
    f.close()
    
# certaintySI_confidence
if do_certaintySI_confidence:
    os.system("rm %s"%(outfile_certaintySI_confidence))

    f = open(outfile_certaintySI_confidence, "w")
    for file in list(all_feats_certaintySI_confidence):
      f.write("<p>============================================")
      f.write("<p>%s<br>"%(file))
      f.write("<IMG SRC=\"%s/design.png\">"%(file))
      f.write("<IMG SRC=\"%s/design_cov.png\" >"%(file))
    f.close()

    
# perceived own certainty at E1 and peer confidence at E2
if do_perceived_certaintyE1_confidence:
    os.system("rm %s"%(outfile_perceived_certaintyE1_confidence))

    f = open(outfile_perceived_certaintyE1_confidence, "w")
    for file in list(all_feats_perceived_certaintyE1_confidence):
      f.write("<p>============================================")
      f.write("<p>%s<br>"%(file))
      f.write("<IMG SRC=\"%s/design.png\">"%(file))
      f.write("<IMG SRC=\"%s/design_cov.png\" >"%(file))
    f.close()
    
# perceived own certainty at SI and peer confidence at E2
if do_perceived_certaintySI_confidence:
    os.system("rm %s"%(outfile_perceived_certaintySI_confidence))

    f = open(outfile_perceived_certaintySI_confidence, "w")
    for file in list(all_feats_perceived_certaintySI_confidence):
      f.write("<p>============================================")
      f.write("<p>%s<br>"%(file))
      f.write("<IMG SRC=\"%s/design.png\">"%(file))
      f.write("<IMG SRC=\"%s/design_cov.png\" >"%(file))
    f.close()
        
    
