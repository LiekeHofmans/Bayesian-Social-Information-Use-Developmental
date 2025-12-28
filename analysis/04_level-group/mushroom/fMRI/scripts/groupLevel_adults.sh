#!/bin/bash

# Group level analysis is done in the GUI, seperately for each contrast.
# Again, you can first create a design (fsf) file, to run later on. 
# Here is an example for low - high own certainty contrasts.
# - Open fsl by typing <fsl> from the command line. Select FEAT FMRI analysis.
# - From the dropdown menu in the upper right of the Data tab, change “First-level analysis” to “Higher-level analysis”.
# - Select "Inputs are 3D cope images from FEAT directories" from the dropdown menu.
# - Set number of inputs to number of subjects.
# - Select the cope directories belonging to the subjects you want to analyze:
# - Click the Paste button. In the Terminal, type ls /home/lhofman/Projects/mushroom_highschool/bids/derivatives/second_level/sub*/output.gfeat/cope1.feat/stats/cope1.nii.gz* | sort -V (or wherever your gfeat dirs live).
# - Copy and paste the list into the Input data window by typing ctrl+y.
# - Set Output directory to /home/lhofman/Projects/mushroom_highschool/bids/derivatives/group_level/low_minus_high_certainty
# - Go the stats tab and select FLAME1 from the dropdown menu.
# - Click on Full model setup
# - Average subjects by setting Number of main EVs to 1, and setting all inputs/subjects to 1. 
# - Select use automatic outlier de-weighing
# - Go to Contrasts tab and set title = groupmean>0 and EV1 = 1; title = groupmean<0 and EV1 = -1 for positive and negative contrast.
# - Click Done and inspect the design matrix window. If ok, you can close this.
# - In the post-stats tab, set Thresholding to cluster and keep z-threshold at 3.1 and cluster threshold at 0.05. 
# - Uncheck the create time series plots (they take up way too much space).
# - Click Go or Save to save the .fsf file as group_ownCertainty.fsf in the group_level scripts folder.


############################################ USER INPUT ##############################################
#######################################################################################################

# Which steps do you want to run (0 = no, 1 = yes)?
do_createMask=0

do_perceived_certaintyE1_masked=0 # run group level for perceived number of mushrooms for self (from perceived_certaintyE1_confidence model)
do_perceived_confidence_masked=0 # run group level for perceived number of mushrooms for other (from perceived_certaintyE1_confidence model)
do_perceived_certaintySI_masked=0 # run group level for perceived number of mushrooms for self (from perceived_certaintySI_confidence model)


# define directories
dir_designFiles='/home/lhofman/Projects/mushroom_highschool/analysis/group_level/scripts'
dir_brainTemplates='/home/lhofman/brain_templates'
dir_examplefunc='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/first_level/sub-207/certaintyE1_confidence/run-1_output.feat/example_func.nii.gz'
dir_output_group='/home/lhofman/Projects/mushroom_highschool/bids/derivatives/group_level'
#######################################################################################################


#######################################################################################################
# Create mask
#######################################################################################################

if [[ $do_createMask == 1 ]]; then 
    
    # transform all masks to correct dimensions   
    flirt -in $dir_brainTemplates/MNI/MNI_prob_FrontalLobe.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/MNI/MNI_prob_FrontalLobe_transformed.nii.gz \
      -applyxfm -usesqform
      
    flirt -in $dir_brainTemplates/MNI/MNI_prob_Insula.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/MNI/MNI_prob_Insula_transformed.nii.gz \
      -applyxfm -usesqform
         
    flirt -in $dir_brainTemplates/NeubertCingulateOrbitoFrontalParcellation/CingulateOrbitoFrontal_thr50_summaryimage_2mm.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/NeubertCingulateOrbitoFrontalParcellation/CingulateOrbitoFrontal_thr50_summaryimage_2mm_transformed.nii.gz \
      -applyxfm -usesqform
      
    flirt -in $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm_transformed.nii.gz \
      -applyxfm -usesqform
    
    flirt -in $dir_brainTemplates/NeubertVentralFrontalParcellation/VentralFrontal_thr75_summaryimage_2mm.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/NeubertVentralFrontalParcellation/VentralFrontal_thr75_summaryimage_2mm_transformed.nii.gz \
      -applyxfm -usesqform
      
    flirt -in $dir_brainTemplates/SalletDorsalFrontalParcellation/DorsalFrontal_thr50_summaryimage_2mm.nii.gz  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/SalletDorsalFrontalParcellation/DorsalFrontal_thr50_summaryimage_2mm_transformed.nii.gz \
      -applyxfm -usesqform  
       
    flirt -in $dir_brainTemplates/K5wholePutamen.nii  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/K5wholePutamen_transformed.nii \
      -applyxfm -usesqform

    flirt -in $dir_brainTemplates/K5wholeCaudate.nii  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/K5wholeCaudate_transformed.nii \
      -applyxfm -usesqform
      
    flirt -in $dir_brainTemplates/K5vS.nii  \
      -ref $dir_examplefunc \
      -out $dir_brainTemplates/K5vS_transformed.nii \
      -applyxfm -usesqform      
    
    # create left lateralized masks out of right masks
    fslswapdim $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm_transformed.nii.gz -x y z $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm_transformed_left.nii.gz
    
    # combine all masks
    fslmaths $dir_brainTemplates/MNI/MNI_prob_FrontalLobe_transformed.nii.gz \
        -add $dir_brainTemplates/MNI/MNI_prob_Insula_transformed.nii.gz \
        -add $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm_transformed.nii.gz \
        -add $dir_brainTemplates/MarsTPJParcellation/TPJ_thr25_2mm_transformed_left.nii.gz \
        -add $dir_brainTemplates/K5wholePutamen_transformed.nii \
        -add $dir_brainTemplates/K5wholeCaudate_transformed.nii \
        -add $dir_brainTemplates/K5vS_transformed.nii \
        $dir_brainTemplates/combinedMasks
fi 
#######################################################################################################


#######################################################################################################
# Run group level feat, masked (takes about 20 min per contrast (positive + negative) including automatic outlier deweighting (otherwise about 2 min)
#######################################################################################################


if [[ $do_perceived_certaintyE1_masked == 1 ]]; then 
    feat $dir_designFiles/masked_adults_perceived_certaintyE1.fsf  
    now=`date`  
    echo "===> feat for perceived certainty at E1 has finished at $now" 
fi

if [[ $do_perceived_certaintySI_masked == 1 ]]; then 
    feat $dir_designFiles/masked_adults_perceived_certaintySI.fsf  
    now=`date`  
    echo "===> feat for perceived certainty at SI has finished at $now" 
fi

if [[ $do_perceived_confidence_masked == 1 ]]; then 
    feat $dir_designFiles/masked_adults_perceived_confidence.fsf  
    now=`date`  
    echo "===> feat for perceived confidence at peer estimate has finished at $now" 
fi



#######################################################################################################



