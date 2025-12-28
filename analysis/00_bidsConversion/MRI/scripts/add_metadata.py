#!/usr/bin/env python3

# Manually add metadata to .json files after bids-conversion

""" Adds metadata to .json files after bids-conversion.

MAKE SURE YOUR FILES ARE ORGANIZED ACCORDING TO BIDS FORMAT

Parameters
----------
bids_dir : str
    Path to the directory with the .json files that need fixing
subjects : array
    Array of subject IDs to be run (if a run does not need fixing, script will not change anything and continue with next run)
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
ees : float
    Effective echo spacing
trt : float
    Total readout time
        
Returns
-------
Adjusted .json files, with slice timings, effective echo spacing and total readout time.
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
import numpy as np


parser = argparse.ArgumentParser(description = "Adding slice timings to .json files", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
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
                    
parser.add_argument('-e', '--ees', 
                    help = 'Effective echo spacing', 
                    required = False, 
                    default = 0.0006909) # spinoza center default
                    
parser.add_argument('-t', '--trt', 
                    help = 'Total readout time', 
                    required = False, 
                    default = 0.0269452) # spinoza center default                      
                    
parser.add_argument('-tr', '--TR', 
                    help = 'Repetition time', 
                    required = False, 
                    default = 2) # spinoza center default  
                                                                          
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
args.ees = float(args.ees)
args.trt = float(args.trt)

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
        
        jsons = sorted(glob(op.join(bids_dir, 'f*', '*.json')))
        for this_json in jsons:
            
            # Check input file
            if not op.isfile(this_json):
                msg = "File %s does not exist. Skipping this run.\n" % this_json
                warnings.warn(msg)
                warning_messages = warning_messages + msg
                break
            
            # Continue with adding metadata     
            with open(this_json, 'r') as f:
                this_json_opened = json.load(f)
                current_metadata = dict()   
            
                
            if 'EffectiveEchoSpacing' not in this_json_opened.keys():
                print("Adding effective echo spacing to %s" % this_json)
                 
                ees = args.ees
                current_metadata.update({'EffectiveEchoSpacing': ees})
                 
            if 'TotalReadoutTime' not in this_json_opened.keys():
                print("Adding total readout time to %s" % this_json)
                 
                trt = args.trt
                current_metadata.update({'TotalReadoutTime': trt})
            
            if "_epi" in this_json:
                
                if isinstance(this_json_opened['IntendedFor'], list):        
                    current_metadata.update({'IntendedFor': this_json_opened['IntendedFor'][0]})
                
            if "_bold" in this_json:
                
                if 'RepetitionTime' not in this_json_opened.keys():
                    print("Adding repetition time to %s" % this_json) 
                    
                    TR = args.TR
                    current_metadata.update({'RepetitionTime': TR})
                      
                if 'SliceTiming' not in this_json_opened.keys():
                    print("Adding slice timing to %s" % this_json)
                    
                    if 'RepetitionTime' not in this_json_opened.keys():
                        this_tr = args.TR           
                    else:
                        this_tr = this_json_opened['RepetitionTime']
                    
                    corresp_func = this_json.replace('.json', '.nii.gz')
                    nr_slices = nib.load(corresp_func).header.get_data_shape()[2]    
                    slice_timing = np.linspace(0, this_tr, nr_slices+1)[:-1]
                    
                    slice_timing = slice_timing.tolist()
                    current_metadata.update({'SliceTiming': slice_timing})           

            if len(current_metadata) > 0:                
                this_json_opened.update(current_metadata)
                with open(this_json, 'w') as updated_f:
                    json.dump(this_json_opened, updated_f, indent=4)


if len(warning_messages) == 0:
    print("====================================================\n\nadd_metadata: SUMMARY OF WARNINGS:\n\nNo warnings. Lucky you.\n\n====================================================")
else:
    print("====================================================\n\nadd_metadata: SUMMARY OF WARNINGS:\n\n" + warning_messages + "\n====================================================")
