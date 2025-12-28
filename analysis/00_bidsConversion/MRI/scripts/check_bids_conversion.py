#!/usr/bin/env python3


""" Checks whether all mri files have indeed been bidsified.

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
Message stating whether bids conversion was successful.
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


parser = argparse.ArgumentParser(description = "Checking number of bidsified mri files", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
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
            
        # Check subject folder and list all files
        if not op.isdir(bids_dir):
            msg = "Cannot find %s. Skipping this subject or session.\n" % bids_dir
            warnings.warn(msg)
            warning_messages = warning_messages + msg
            break
        
        filelist = []
        for root, dirs, files in os.walk(bids_dir):
            for file in files: 
                filelist.append(file)
        
        if not len(filelist) == 15:
            msg = "Missing files for %s in %s.\n" % (sub_str, bids_dir)
            warning_messages = warning_messages + msg
                                       
            
if len(warning_messages) == 0:
    print("====================================================\n\nCheck bids files: SUMMARY OF WARNINGS:\n\nNo warnings. Lucky you.\n\n====================================================")
else:
    print("====================================================\n\nCheck bids files: SUMMARY OF WARNINGS:\n\n" + warning_messages + "\n====================================================")
