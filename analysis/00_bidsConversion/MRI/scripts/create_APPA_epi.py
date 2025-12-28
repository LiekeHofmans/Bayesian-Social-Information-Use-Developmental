#!/usr/bin/env python3


""" Creates an '_epi' file with PE encoding AP from last bold volumes 
and renames original _epi file to PA.

MAKE SURE YOUR FILES ARE ORGANIZED ACCORDING TO BIDS FORMAT

Parameters
----------
bids_dir : str
    Path to the bids directory 
subjects : array
    Array of subject IDs to be run 
sessions : array 
    Array of sessions to be run
sub_prefix : str
    Prefix that is prepended to the subject number
sub_digits : int
    Number of digits to indicate your subject ID with (e.g. 1 or 001)
session_folder : bool
    Whether session number is part of the file directory
ses_prefix : str
    Prefix that is prepended to the session number
ses_digits : int
    Number of digits to indicate your session number with (e.g. 1 or 01)
    
Returns
-------
Adjusted .nii.gz and .json _epi files, with PE direction = AP.
   """

import os
import os.path as op
import argparse
import warnings
import shutil
import json
from array import *
from glob import glob
import nibabel as nib
import re


parser = argparse.ArgumentParser(description = "Creating AP and PA _epi files", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-r', '--bids_dir', 
                    help = 'Path of the .json files to be fixed', 
                    required = True, 
                    default = None)                   

parser.add_argument('-s', '--subjects', 
                    help = 'Subject IDs to run', 
                    required = False, 
                    default = None)
                                            
parser.add_argument('-a', '--sub_prefix', 
                    help = 'Prefix to be prepended to your subject number', 
                    required = False, 
                    default = 'sub-')   

parser.add_argument('-b', '--sub_digits', 
                    help = 'Number of digits to indicate subject number ', 
                    required = False, 
                    default = 3)                                 

parser.add_argument('-n', '--sessions', 
                    help = 'Array of sessions to run', 
                    required = False, 
                    default = '1') 
                    
parser.add_argument('-z', '--session_folder', 
                    help = 'Is session number a subfolder in the directory (0=no, 1=yes)?', 
                    required = False, 
                    default = 0)  
                    
parser.add_argument('-c', '--ses_prefix', 
                    help = 'Prefix to be prepended to your session number', 
                    required = False, 
                    default = 'ses-')   

parser.add_argument('-d', '--ses_digits', 
                    help = 'Number of digits to indicate session number ', 
                    required = False, 
                    default = 1)   
                                  
args = parser.parse_args()

          
# Format input arguments, as they all come in as strings
if not op.isdir(args.bids_dir):
    raise ValueError("Cannot find %s." % bids_dir)
    
if args.subjects is not None: 
    subs = list(map(int,args.subjects.split(',')))
else: 
    list_subFolders = sorted(glob(op.join(args.bids_dir, args.sub_prefix + '*'))) # default to all subjects the script can find within the data directory
    subs = []
    for iFolder in list_subFolders:
        subs.append(int(op.basename(iFolder).split(args.sub_prefix)[1]))

sessions = list(map(int,args.sessions.split(',')))      
if ((len(sessions) > 1) and (args.session_folder == 0)):
    raise ValueError("Multiple sessions were specified, while it was indicated that there were no subfolders for the sessions.\nAdjust your folder structure such that separate sessions are stored in separate subfolders within the subject folder before running this script!")

args.sub_digits = int(args.sub_digits)
args.session_folder = int(args.session_folder)
args.ses_digits = int(args.ses_digits)


# Loop through subjects, sessions and runs 
warning_messages = ""
for iSub in subs:
    sub_str = args.sub_prefix + str(iSub).zfill(args.sub_digits)
    for iSes in sessions:
        ses_str = args.ses_prefix + str(iSes).zfill(args.ses_digits)
        
        if args.session_folder == 0:
            bids_dir = op.join(args.bids_dir, sub_str, '')
        else:
            bids_dir = op.join(args.bids_dir, sub_str, ses_str, '')
            
        # Check input folder and list all files
        if not op.isdir(bids_dir):
            msg = "Cannot find %s. Skipping this subject or session.\n" % bids_dir
            warnings.warn(msg)
            warning_messages = warning_messages + msg
            break
        
        jsons_fmap = sorted(glob(op.join(bids_dir, 'fmap', '*.json')))

        for json_PA in jsons_fmap:

               
            # Only run if conversion has not yet been completed
            json_AP = re.sub(r'dir-.+?_', 'dir-AP_', json_PA)  
            if not op.isfile(json_AP):
                               
                # open corresponding files:
                
                with open(json_PA, 'r') as f:
                    json_PA_opened = json.load(f)  
                nii_PA = json_PA.replace('.json', '.nii.gz')    
                PA_vols = nib.load(nii_PA)
                nvols = PA_vols.shape[3]
                                                   
                nii_bold = json_PA_opened['IntendedFor']
                nii_bold = op.join(bids_dir, nii_bold)
                bold_vols = nib.load(nii_bold)
                bold_vols = bold_vols.slicer[...,-nvols:] 
                json_bold = nii_bold.replace('.nii.gz', '.json')
                with open(json_bold, 'r') as f:
                    json_bold_opened = json.load(f)                                               
                           
                # save image and json file for AP direction
                nii_AP = re.sub(r'dir-.+?_', 'dir-AP_', nii_PA)            
                nib.save(bold_vols, nii_AP)
                json_bold_opened['PhaseEncodingDirection'] = 'j-'
                json_bold_opened['IntendedFor'] = json_PA_opened['IntendedFor']
                with open(json_AP, 'w') as f:
                    json.dump(json_bold_opened, f, indent=4)
                    
                # rename original image and json file for PA direction
                json_PA_renamed = re.sub(r'dir-.+?_', 'dir-PA_', json_PA) # part that needs to be replaced; replacement; filename
                nii_PA_renamed = re.sub(r'dir-.+?_', 'dir-PA_', nii_PA)
                os.rename(json_PA, json_PA_renamed)
                os.rename(nii_PA, nii_PA_renamed)
            
if len(warning_messages) == 0:
    print("====================================================\n\ncreate_APPA_epi: SUMMARY OF WARNINGS:\n\nNo warnings. Lucky you.\n\n====================================================")
else:
    print("====================================================\n\ncreate_APPA_epi: SUMMARY OF WARNINGS:\n\n" + warning_messages + "\n====================================================")
