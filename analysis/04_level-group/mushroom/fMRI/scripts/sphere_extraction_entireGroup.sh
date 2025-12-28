#!/bin/bash

# Script to extract mean contrast estimates per subject per cluster


############################################ USER INPUT ##############################################
#######################################################################################################

# Do we have to mount the project folder?
do_mountFMG=0 # Mounts the FMG project folder to a directory on the tux

# Define directory of group level contrast data
groupComparison_peerConfidence_masked_folder="/home/lhofman/Projects/mushroom_highschool/bids/derivatives/group_level/masked_groupComparison_perceived_confidence.gfeat/cope1.feat"

peerConfidence_masked_folder="/home/lhofman/Projects/mushroom_highschool/bids/derivatives/group_level/masked_entireGroup_peerConfidence.gfeat/cope1.feat"

# folder with brain templates (masks)
dir_brainTemplates='/home/lhofman/brain_templates'

# Where to store the data?
output_file="/home/lhofman/fmg-research-mount/mushroom_highschool/bids/derivatives/mri/group_level/individual_peerConfidence_estimates_BOLD.csv"

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
# Extract subject level COPE values for each spherical cluster after flame1 analysis --MASKED
#######################################################################################################

# Create file that combines each subjects cope value
fslmerge -t $peerConfidence_masked_folder/allbetas.nii.gz `ls /home/lhofman/Projects/mushroom_highschool/bids/derivatives/second_level/sub-*/certaintyE1_confidence.gfeat/cope2.feat/stats/cope1.nii.gz | sort -V`

# Extract subject level cope values from sphere within each cluster
#-------------------------------------------------------------------------------
mkdir -p $peerConfidence_masked_folder/peak_spheres
[ -f "$peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt" ] && rm $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt # in case the file already exists, remove and create anew
touch $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt
cluster -i $groupComparison_peerConfidence_masked_folder/thresh_zstat1 -t 3.1 -c $peerConfidence_masked_folder/stats/cope1 | sed '1d' | awk '{print $4, $5, $6;}' | while read line ; do # defines x, y, z coordinates
    x=$(echo $line | awk '{print $1}') 
    y=$(echo $line | awk '{print $2}')
    z=$(echo $line | awk '{print $3}')
    fslmaths $dir_brainTemplates/tpl-MNI152NLin2009cAsym_res-02_desc-brain_T1w -mul 0 -add 1 -roi $x 1 $y 1 $z 1 0 1 $peerConfidence_masked_folder/peak_spheres/$x$y$z"_point" -odt float # Create mask of peak voxel
    fslmaths $peerConfidence_masked_folder/peak_spheres/$x$y$z"_point" -kernel sphere 3 -fmean $peerConfidence_masked_folder/peak_spheres/$x$y$z"_sphere" -odt float # extend to sphere
    fslmeants -i $peerConfidence_masked_folder/allbetas -m $peerConfidence_masked_folder/peak_spheres/$x$y$z"_sphere" | tr '\n' ' ' >> $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp.txt # calculate individual mean cope value within sphere
    echo '\n' >> $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp.txt # add newline, otherwise I don't get it transposed
done
tac $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp.txt > $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp2.txt # reverse order from largest to smallest cluster first
awk '{ for (i=1; i<=NF; i++) RtoC[i]= (i in RtoC?RtoC[i] OFS :"") $i; } 
    END{ for (i=1; i<=NF; i++) print RtoC[i] }' $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp2.txt > $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt # no idea what it means, but it transposes. 
sed -i '$ d' $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt # remove last row with '\n'
rm $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp.txt $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere_tmp2.txt # remove temporary files


#######################################################################################################

# Extract subject IDs without leading zeros and save to temp file
ls /home/lhofman/Projects/mushroom_highschool/bids/derivatives/second_level/sub-*/certaintyE1_confidence.gfeat/cope2.feat/stats/cope1.nii.gz | \
    sort -V | sed -E 's|.*/sub-0*([0-9]+)/.*|\1|' > $peerConfidence_masked_folder/stats/subject_ids.txt

# Prepend subject IDs as first column
paste $peerConfidence_masked_folder/stats/subject_ids.txt $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt > \
    $peerConfidence_masked_folder/stats/tmp_with_ids.txt
    
# Add header row
printf "sID\tventromedial_PFC\tanteriormedial_PFC\tmidcingulate_cortex\n" > $output_file
    
# Append data
cat $peerConfidence_masked_folder/stats/tmp_with_ids.txt >> $output_file
    
# Clean up
rm -f $peerConfidence_masked_folder/allbetas.nii.gz
rm -f $peerConfidence_masked_folder/stats/tmp_with_ids.txt
rm -f $peerConfidence_masked_folder/stats/subject_ids.txt
rm -f $peerConfidence_masked_folder/stats/entireGroup_subjectMeansPerSphere.txt
rm -rf $peerConfidence_masked_folder/peak_spheres

