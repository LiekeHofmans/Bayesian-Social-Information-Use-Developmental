#!/bin/bash

# Before running a batch file, make sure there is already a .fsf file for 1 run/1subject of the first-level analysis.
# You can use this .fsf file as template input for the other runs, as is done by the batch file.
# - To create the initial .fsf file, open fsl by typing <fsl> from the command line. Select FEAT FMRI analysis.

# - Click on “Select 4D data” and select the fMRI run you want to analyze.
# - Leave Output directory empty
# - Keep everything in the Pre-stats as is.
# - In the registration tab, unacheck main structural image. 
# - for standard space, select an MNI brain (skull-stripped):  usr/local/fsl/data/standard/MNI152_T1_2mm_brain.
# - Set to 6 DOF to speed things up. (will be overwritten anyway).
# - Go the stats tab and click on Full model setup
# - Change the number of EVs to the number of regressors (here, 5)
# - name the EVs (e.g. low and high) and select Basic shape “Custom (3 column format)”; select the corresponding timings file.
# - set convolution to double-gamma HRF to include the undershoot. 
# - Leave the "add temporal derivatives" and "apply temporal filtering" checked.
# - Go to the Contrasts & F-tests tab and specify the contrasts. 
# - Click Done and inspect the design matrix window. If ok, you can close this.
# - In the post-stats tab, uncheck the create time series plots (they take up way too much space).
# - Click Save to save the .fsf file as 1stLevel.fsf in the scripts folder.
# - Adapt fields that change per subject to tamplate names (e.g. {ANATFILE}; see below).

############################################ USER INPUT ##############################################
#######################################################################################################

# Which steps do you want to run (0 = no, 1 = yes)?
do_mountFMG=0 # Mounts the FMG project folder to a directory on the tux
do_createTimings=0  # create the timing files per condition
do_createNuisanceRegressors=0 # create list with nuisance regressors per subject and run
do_firstLevel=0 # run fsl feat first level analysis
do_QA=1 # run quality check of first level analysis


# if do_firstLevel==1, which models?
do_certaintyE1_confidence=0 # check effect own certainty (low or high) and peer confidence (-1, 0, 1; parametric). 
do_certaintySI_confidence=0 # check effect own certainty (low or high) and peer confidence (-1, 0, 1; parametric). 
do_perceived_certaintyE1_confidence=0 # check effect perceived own certainty and perceived peer confidence (all parametric, based on computational model) 
do_perceived_certaintySI_confidence=0 # check effect perceived own certainty and perceived peer confidence (all parametric, based on computational model) 

# Define directories and filenames
dir_exclusions='/home/lhofman/fmg-research-mount/mushroom_highschool/analysis/participants_to_exclude.csv' # where the list with participants to exclude can be found
dir_bids='/home/lhofman/Projects/mushroom_highschool/bids' # where the bids folder is
dir_bids_mount='/home/lhofman/fmg-research-mount/mushroom_highschool/bids' # where the bids folder is on the mount
dir_anat='/usr/local/fsl/data/standard/MNI152_T1_2mm_brain' # where the standard MNI brain can be found

dir_fsf_certaintyE1_confidence='/home/lhofman/Projects/mushroom_highschool/analysis/first_level/scripts/certaintyE1_confidence.fsf' 
fsf_certaintyE1_confidence='certaintyE1_confidence.fsf'
dir_fsf_certaintySI_confidence='/home/lhofman/Projects/mushroom_highschool/analysis/first_level/scripts/certaintySI_confidence.fsf' 
fsf_certaintySI_confidence='certaintySI_confidence.fsf'
dir_fsf_perceived_certaintyE1_confidence='/home/lhofman/Projects/mushroom_highschool/analysis/first_level/scripts/perceived_certaintyE1_confidence.fsf' 
fsf_perceived_certaintyE1_confidence='perceived_certaintyE1_confidence.fsf'
dir_fsf_perceived_certaintySI_confidence='/home/lhofman/Projects/mushroom_highschool/analysis/first_level/scripts/perceived_certaintySI_confidence.fsf' 
fsf_perceived_certaintySI_confidence='perceived_certaintySI_confidence.fsf'


# How many cores do you want to use?
# Pick a sensible number of cores while leaving enough space for others to do their stuff and does not overburden RAM.
# 1 volume takes about 4 minutes to process.
# nproc # gives number of total logical cores; 
n_cores=20 #20

#######################################################################################################
#######################################################################################################


#######################################################################################################
# Mount FMG folder (needs password for both tux and fmgstorage and sudo rights) so all files are available
#######################################################################################################
if [[ $do_mountFMG == 1 ]]; then 
    mkdir -p /home/lhofman/fmg-research-mount/mushroom_highschool
    sudo mount -t cifs "//fmg-research.uva.nl/psychology$/fMRI Projects/fMRI Project Mushroom Highschool" /home/lhofman/fmg-research-mount/mushroom_highschool -o username=lhofman,domain=uva,noexec,uid=$(id -u),gid=$(id -g)
fi
#######################################################################################################


#######################################################################################################
# Create timing files per condition
#######################################################################################################
if [[ $do_createTimings == 1 ]]; then 
    Rscript create_FSL_timingfiles.R
fi
#######################################################################################################

#######################################################################################################
# Create nuisance regressors per subject and run
#######################################################################################################
if [[ $do_createNuisanceRegressors == 1 ]]; then 
    Rscript create_nuisance_regressors.R
fi
#######################################################################################################


#######################################################################################################
# Run first level analysis (Takes about 1.5h without prep; 4.5h inluding prep)
#######################################################################################################
if [[ $do_firstLevel == 1 ]]; then 
   
    # Load list with exclusions
    exclusions=( $(tail -n +2 $dir_exclusions | cut -d ',' -f3) )

    # Loop over subjects
    for subdir in $dir_bids/sub-* ; do  
        (      
        sub="${subdir##*/}" #keep only subject ID as sub-xxx, without full directory
        subnr=$(echo $subdir | sed 's/[^0-9]*//g') #keep only subject ID as xxx, without full directory
        subnr="${subnr#"${subnr%%[!0]*}"}" # remove leading zeros
        # Only running analysis for participants not in exclusion list
        if printf '%s\n' ${exclusions[@]} | grep -q --line-regexp $subnr; then
            echo "===> $sub is in exclusion list; Skipping first-level analysis." 
        else
            
            # Loop over runs
            now=`date`
            echo "===> Starting processing of $sub at $now"
            for run in $subdir/func/*_bold.nii.gz; do  
                run_number=$(echo $run | awk -F'/' '{ print $(NF) }' | awk -F'-' '{ print $5 }' | awk -F'_' '{ print $1 }') # run_number is either 1, 2, or 3 
                
                # Run selected models
                
                                        
                # Main effects own certainty at E1 and peer confidence 
                # ============================================================== 
                if [[ $do_certaintyE1_confidence == 1 ]]; then 

                    # 1. Copy the design file into the subject directory
                    outputdir=$dir_bids/derivatives/first_level/$sub/certaintyE1_confidence/run-$run_number'_output'
                    mkdir -p $outputdir
                    cp $dir_fsf_certaintyE1_confidence $outputdir
                
                    # 2 Adapt subject-specific information in the design file for own certainty and peer confidence            
                    funcfile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_bold'
                    conffile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_desc-confounds_regressors_selection_no_ICAAROMA.tsv'
                    EV1=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-lowCertaintyE1_events.txt'
                    EV2=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-highCertaintyE1_events.txt'
                    EV3=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-parametricConfidenceSI_events.txt'
                    NPT=$(grep 'NumberOfVolumes' $funcfile.json | sed -r 's/^[^:]*:\ (.*),$/\1/') # using jq would be more optimal, but I can't download it.     
                    
                    sed -i -e "s|{OUTPUTDIR}|$outputdir|g" \
                        -e "s|{NPT}|$NPT|g" \
                        -e "s|{ANATFILE}|$dir_anat|g" \
                        -e "s|{FUNCFILE}|$funcfile|g" \
                        -e "s|{CONFFILE}|$conffile|g" \
                        -e "s|{EV1}|$EV1|g" \
                        -e "s|{EV2}|$EV2|g" \
                        -e "s|{EV3}|$EV3|g" \
                        $outputdir/$fsf_certaintyE1_confidence
                    
                    # 3 Run first level analysis 
                    feat $outputdir/$fsf_certaintyE1_confidence
                    
                    # 4 Create registration files such that they dont change the images (I already use preprocessed images).
                    mkdir -p $outputdir.feat/reg
                    # Create identity matrix
                    cp $FSL_DIR/etc/flirtsch/ident.mat $outputdir.feat/reg/example_func2standard.mat
                    # Create image with the mean_func.nii.gz
                    cp $outputdir.feat/mean_func.nii.gz $outputdir.feat/reg/standard.nii.gz
                                                          
                    now=`date` 
                    echo "===> feat for $sub run $run_number has finished at $now" 
                fi


                # Main effects own certainty at SI and peer confidence 
                # ============================================================== 
                if [[ $do_certaintySI_confidence == 1 ]]; then 

                    # 1. Copy the design file into the subject directory
                    outputdir=$dir_bids/derivatives/first_level/$sub/certaintySI_confidence/run-$run_number'_output'
                    mkdir -p $outputdir
                    cp $dir_fsf_certaintySI_confidence $outputdir
                
                    # 2 Adapt subject-specific information in the design file for own certainty and peer confidence            
                    funcfile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_bold'
                    conffile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_desc-confounds_regressors_selection_no_ICAAROMA.tsv'
                    EV1=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-lowCertaintySI_events.txt'
                    EV2=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-highCertaintySI_events.txt'
                    EV3=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_condition-parametricConfidenceSI_events.txt'
                    NPT=$(grep 'NumberOfVolumes' $funcfile.json | sed -r 's/^[^:]*:\ (.*),$/\1/') # using jq would be more optimal, but I can't download it.     
                    
                    sed -i -e "s|{OUTPUTDIR}|$outputdir|g" \
                        -e "s|{NPT}|$NPT|g" \
                        -e "s|{ANATFILE}|$dir_anat|g" \
                        -e "s|{FUNCFILE}|$funcfile|g" \
                        -e "s|{CONFFILE}|$conffile|g" \
                        -e "s|{EV1}|$EV1|g" \
                        -e "s|{EV2}|$EV2|g" \
                        -e "s|{EV3}|$EV3|g" \
                        $outputdir/$fsf_certaintySI_confidence
                    
                    # 3 Run first level analysis 
                    feat $outputdir/$fsf_certaintySI_confidence
                    
                    # 4 Create registration files such that they dont change the images (I already use preprocessed images).
                    mkdir -p $outputdir.feat/reg
                    # Create identity matrix
                    cp $FSL_DIR/etc/flirtsch/ident.mat $outputdir.feat/reg/example_func2standard.mat
                    # Create image with the mean_func.nii.gz
                    cp $outputdir.feat/mean_func.nii.gz $outputdir.feat/reg/standard.nii.gz
                                                          
                    now=`date` 
                    echo "===> feat for $sub run $run_number has finished at $now" 
                fi
                
              
                               
                # Perceived certainty at E1 and perceived confidence at SI
                # ============================================================== 
                if [[ $do_perceived_certaintyE1_confidence == 1 ]]; then 

                    # 1. Copy the design file into the subject directory
                    outputdir=$dir_bids/derivatives/first_level/$sub/perceived_certaintyE1_confidence/run-$run_number'_output'
                    mkdir -p $outputdir
                    cp $dir_fsf_perceived_certaintyE1_confidence $outputdir
                
                    # 2 Adapt subject-specific information in the design file for own certainty and peer confidence            
                    funcfile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_bold'
                    conffile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_desc-confounds_regressors_selection_no_ICAAROMA.tsv'
                    EV1=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_params-perceivedCertainty_events.txt'
                    EV2=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_params-perceivedConfidence_events.txt'
                    NPT=$(grep 'NumberOfVolumes' $funcfile.json | sed -r 's/^[^:]*:\ (.*),$/\1/') # using jq would be more optimal, but I can't download it.     
                    
                    sed -i -e "s|{OUTPUTDIR}|$outputdir|g" \
                        -e "s|{NPT}|$NPT|g" \
                        -e "s|{ANATFILE}|$dir_anat|g" \
                        -e "s|{FUNCFILE}|$funcfile|g" \
                        -e "s|{CONFFILE}|$conffile|g" \
                        -e "s|{EV1}|$EV1|g" \
                        -e "s|{EV2}|$EV2|g" \
                        $outputdir/$fsf_perceived_certaintyE1_confidence
                    
                    # 3 Run first level analysis 
                    feat $outputdir/$fsf_perceived_certaintyE1_confidence
                    
                    # 4 Create registration files such that they dont change the images (I already use preprocessed images).
                    mkdir -p $outputdir.feat/reg
                    # Create identity matrix
                    cp $FSL_DIR/etc/flirtsch/ident.mat $outputdir.feat/reg/example_func2standard.mat
                    # Create image with the mean_func.nii.gz
                    cp $outputdir.feat/mean_func.nii.gz $outputdir.feat/reg/standard.nii.gz
                    
                    now=`date` 
                    echo "===> feat for $sub run $run_number has finished at $now" 
                fi 
                
                               
                # Perceived certainty and perceived confidence at SI
                # ============================================================== 
                if [[ $do_perceived_certaintySI_confidence == 1 ]]; then 

                    # 1. Copy the design file into the subject directory
                    outputdir=$dir_bids/derivatives/first_level/$sub/perceived_certaintySI_confidence/run-$run_number'_output'
                    mkdir -p $outputdir
                    cp $dir_fsf_perceived_certaintySI_confidence $outputdir
                
                    # 2 Adapt subject-specific information in the design file for own certainty and peer confidence            
                    funcfile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_bold'
                    conffile=$dir_bids/derivatives/halfpipe/$sub/func/$sub'_task-mushroom_run-'$run_number'_setting-preproc_desc-confounds_regressors_selection_no_ICAAROMA.tsv'
                    EV1=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_params-perceivedCertaintySI_events.txt'
                    EV2=$dir_bids_mount/$sub/func/$sub'_task-mushroom_run-'$run_number'_params-perceivedConfidence_events.txt'
                    NPT=$(grep 'NumberOfVolumes' $funcfile.json | sed -r 's/^[^:]*:\ (.*),$/\1/') # using jq would be more optimal, but I can't download it.     
                    
                    sed -i -e "s|{OUTPUTDIR}|$outputdir|g" \
                        -e "s|{NPT}|$NPT|g" \
                        -e "s|{ANATFILE}|$dir_anat|g" \
                        -e "s|{FUNCFILE}|$funcfile|g" \
                        -e "s|{CONFFILE}|$conffile|g" \
                        -e "s|{EV1}|$EV1|g" \
                        -e "s|{EV2}|$EV2|g" \
                        $outputdir/$fsf_perceived_certaintySI_confidence
                    
                    # 3 Run first level analysis 
                    feat $outputdir/$fsf_perceived_certaintySI_confidence
                    
                    # 4 Create registration files such that they dont change the images (I already use preprocessed images).
                    mkdir -p $outputdir.feat/reg
                    # Create identity matrix
                    cp $FSL_DIR/etc/flirtsch/ident.mat $outputdir.feat/reg/example_func2standard.mat
                    # Create image with the mean_func.nii.gz
                    cp $outputdir.feat/mean_func.nii.gz $outputdir.feat/reg/standard.nii.gz
                    
                    now=`date` 
                    echo "===> feat for $sub run $run_number has finished at $now" 
                fi 
                                                                 
            done 
        fi
        ) & 
        
        # allow to execute up to $n_cores jobs in parallel
        if [[ $(jobs -r -p | wc -l) -ge $n_cores ]]; then
            wait -n
        fi
         
    done      
    wait    
fi
#######################################################################################################


#######################################################################################################
# Run quality check first level
#######################################################################################################
if [[ $do_QA == 1 ]]; then 
    mkdir -p $dir_bids/derivatives/first_level/QA
    touch $dir_bids/derivatives/first_level/QA/lev1_QA_certaintyE1_confidence.html
    touch $dir_bids/derivatives/first_level/QA/lev1_QA_certaintySI_confidence.html
    touch $dir_bids/derivatives/first_level/QA/lev1_QA_perceived_certaintyE1_confidence.html
    touch $dir_bids/derivatives/first_level/QA/lev1_QA_perceived_certaintySI_confidence.html

    python3 QA_1stLevel.py # Make sure to adapt script to selected models.
    # saves html file with images from all subjects in bids/derivatives/first_level
    # mainly check collinearity. 
fi
#######################################################################################################


