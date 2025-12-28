#!/bin/bash
#######################################################################################################
# Script to preprocess already bidsified nifti files using fmriprep
#######################################################################################################

# Installation requirements:
#   - python3 (including pip3)
#   - docker (to install Halfpipe)
#   - HalfPipe

############################################# USER INPUT ##############################################
#######################################################################################################

# Which steps do you want to run (0 = no, 1 = yes)?
do_fMRIPrep=1 # Run preprocessing using HALFipe

# Define directories and filenames
dir_halfpipe='/home/lhofman/HALFpipe/halfpipe-halfpipe-latest.simg' # where your halfpipe program is located
subjects_to_run='HALFpipe_subjectsToRun.txt' # HALFpipe needs an explicit list of subjects if there is already some preprocessed data in the bids folder.

#######################################################################################################
#######################################################################################################

##################################### Run HALFpipe's fMRIPrep #########################################

if [[ $do_fMRIPrep == 1 ]]; then
    singularity run --contain --cleanenv --bind /:/ext $dir_halfpipe --keep none #--subject-list $dir_subject_list
fi

#######################################################################################################





