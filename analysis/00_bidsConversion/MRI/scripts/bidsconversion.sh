#!/bin/bash
#######################################################################################################
# Script to convert PAR/REC files (native imaging files) into nifti files and convert format into BIDS
#######################################################################################################

# Installation requirements:
#   - python3 (including pip3)
#   - Bidscoin 
#   - dcm2niix (plugin for Bidscoin)

############################################# USER INPUT ##############################################
#######################################################################################################

# Which steps do you want to run (0 = no, 1 = yes)?
do_mountFMG=1 # Mount (map) your project folder to one of the directories on the server
do_truncating=0 # Truncating step to make sure you don't have incomplete scans
do_bidsmapper=0 # Map the raw files to nifti files (including possibility to customize mapping)
do_bidscoiner=0 # Convert the raw files to nifti files in bids format

# Define directories and filenames
dir_raw='/home/lhofman/Projects/mushroom_highschool/raw_data' # where your raw data files can be found
dir_bids='/home/lhofman/Projects/mushroom_highschool/bids' # where your bidsified data should go
dir_scans='scans' # where the scans can be found
name_bidsmap='bidsmap.yaml' # how you named your bidsmap parameter file
#dir_halfpipe='/home/lhofman/HALFpipe/halfpipe-halfpipe-latest.simg' # where your halfpipe program is located
#subjects_to_run='HALFpipe_subjectsToRun.txt' # HALFpipe needs an explicit list of subjects if there is already some preprocessed data in the bids folder.

bold_identifier='*bold*[0-9]' # added the digit indicator so the fix_truncated_scans.py script does not run the partial volumes scan upon rerun. 
#######################################################################################################
#######################################################################################################

############################### 0. Mount project folder to tux ########################################
if [[ $do_mountFMG == 1 ]]; then 
    # new drive
    mkdir -p /home/lhofman/fmg-research-mount/mushroom_highschool
    sudo mount -t cifs "//fmg-research.uva.nl/psychology$/fMRI Projects/fMRI Project Mushroom Highschool" /home/lhofman/fmg-research-mount/mushroom_highschool -o username=lhofman,domain=uva,noexec,uid=$(id -u),gid=$(id -g)
    # If you haven't done so already, copy/paste the raw files from the research drive to the project drive on this server. 
fi
#######################################################################################################


######################## 1. Make sure the PAR files only include complete scans #######################
if [[ $do_truncating == 1 ]]; then 
    python3 fix_truncated_scans.py -r $dir_raw -f $dir_scans -i $bold_identifier
fi 
#######################################################################################################


############# 2. Run bidscoin to convert to nifti and organize according to bids-format ###############

# NB: Bidscoin will convert ALL files for ALL participants it can find in the specified folder.
if [[ $do_bidsmapper == 1 ]]; then
    # The bidsmapper command can be used to check the mappings
    # If this is your first bidsmapper run and you still need to compile the bidsmap.yaml file, 
    # run the below command without <<-b $name_bidsmap>>.
    bidsmapper $dir_raw $dir_bids -m $dir_scans #-b $name_bidsmap
fi

if [[ $do_bidscoiner == 1 ]]; then 
    #bidscoiner $dir_raw $dir_bids
    # check if all mri files have indeed been bidsified
    #python3 check_bids_conversion.py -r $dir_bids
    # add meta information to the .json file: slice timing, effective echo spacing, total readout time 
    #python3 add_metadata.py -r $dir_bids
    # make sure there are 2 fieldmap images, 1 in each direction (AP and PA) and they are named correctly
    python3 create_APPA_epi.py -r $dir_bids #-s $subs
fi 
#######################################################################################################
 
 






