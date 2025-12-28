#!/usr/bin/env python3

# We manually cut of the scan runs, so we have truncated volumes which need to be removed from the files 
# to make sure the PAR file contains only complete volumes. 
# This script was copied from mri2nifti.py, part of bidsify and written by Lukas Snoek.

""" Removes incomplete volumes from PAR files.

Parameters
----------
raw_dir : str
    Path to the directory with the raw files that need fixing
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
scanfolder : str
    Name of the subfolder in which the raw files can be found
identifier : str
    Unique identifier to indicate the files to be fixed (e.g. *bold*.PAR)
    
Returns
-------
Adjusted .PAR files, with number of volumes and slices corrected for partial volumes.
   """

import os
import os.path as op
import argparse
import warnings
import shutil
import re
from array import *
from glob import glob

parser = argparse.ArgumentParser(description = "Cropping .PAR files of scans with incomplete volumes", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-r', '--raw_dir', 
                    help = 'Path of the raw files to be fixed', 
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
                    
parser.add_argument('-f', '--scanfolder', 
                    help = 'Name of the subfolder in which the raw files can be found (e.g. scans)', 
                    required = False, 
                    default = '')
                    
parser.add_argument('-i', '--identifier', 
                    help = 'Unique identifier in name of scans to be fixed (e.g. *bold*)', 
                    required = False, 
                    default = '*bold*')
args = parser.parse_args()

           
# Format input arguments, as they all come in as strings
if not op.isdir(args.raw_dir):
    raise ValueError("Cannot find %s." % raw_dir)
    
if args.subjects is not None: 
    subs = list(map(int,args.subjects.split(',')))
else: 
    list_subFolders = sorted(glob(op.join(args.raw_dir, args.sub_prefix + '*'))) # default to all subjects the script can find within the raw data directory
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
            raw_dir = op.join(args.raw_dir, sub_str, args.scanfolder, '')
        else:
            raw_dir = op.join(args.raw_dir, sub_str, ses_str, args.scanfolder, '')
            
        # Check input folder and list all files
        if not op.isdir(raw_dir):
            msg = "Cannot find %s. Skipping this subject or session.\n" % raw_dir
            warnings.warn(msg)
            warning_messages = warning_messages + msg
            break
        
        scans = sorted(glob(op.join(raw_dir, args.identifier + '.PAR')))
        for iScan in scans:
            
            # Check input file
            if not op.isfile(iScan):
                msg = "File %s does not exist. Skipping this run.\n" % raw_dir
                warnings.warn(msg)
                warning_messages = warning_messages + msg
                break
            
            # Continue with actual fixing     
            print("Fixing file %s" % iScan)
            info = dict()

            with open(iScan, 'r') as f:
                lines = f.readlines()

            found = False
            for line in lines:
                found = 'Max. number of slices/locations' in line
                if found:
                    info['n_slices'] = int(line.split(':')[-1].strip().replace('\n', ''))
                    break

            if not found:
                msg = "Could not determine number of slices from PAR header (%s). Skipping this run.\n" % iScan
                warnings.warn(msg)
                warning_messages = warning_messages + msg
                break

            found = False
            for line_nr_of_dyns, line in enumerate(lines):
                found = 'Max. number of dynamics' in line
                if found:
                    info['n_dyns'] = int(line.split(':')[-1].strip().replace('\n', ''))
                    break

            if not found:
                msg = "Could not determine number of dynamics from PAR header (%s). Skipping this run.\n" % iScan
                warnings.warn(msg)
                warning_messages = warning_messages + msg
                break
                
            found = False
            for line in lines:
                found = 'Max. number of echoes' in line
                if found:
                    info['n_echoes'] = int(line.split(':')[-1].strip().replace('\n', ''))
                    break

            if info['n_dyns'] == 1:
                msg = "%s is not an fMRI file! Skipping this file.\n" % iScan
                warnings.warn(msg)
                warning_messages = warning_messages + msg
                break

            # Multiecho fMRI has n_dyns * n_echoes volumes in the 4th dim
            info['n_vols'] = int(info['n_dyns'] * info['n_echoes'])

            found = False
            for idx_start_slices, line in enumerate(lines):
                found = '# === IMAGE INFORMATION =' in line
                if found:
                    idx_start_slices += 3
                    break

            idx_stop_slices = len(lines) - 2
            slices = lines[idx_start_slices:idx_stop_slices]
            actual_n_vols = len(slices) / info['n_slices']

            if actual_n_vols != info['n_vols']:
                print("Found %.3f vols (%i slices) for file %s, but expected %i dyns (%i slices);"
                      " going to try to fix it by removing slices from the PAR header ..." %
                      (actual_n_vols, len(slices), op.basename(iScan), info['n_vols'], info['n_vols']*info['n_slices']))

                lines_to_remove = len(slices) % info['n_slices']
                print("Number of excess slices: %i" % int(lines_to_remove))
                if lines_to_remove != 0:
                    # first store a hidden copy of the original   
                    target = iScan.replace(".PAR", "_partialVolume.PAR")
                    target = op.join(op.split(target)[0], "." + op.split(target)[1])
                    shutil.copy2(iScan, target)
                                          
                    for i in range(lines_to_remove):
                        lines.pop(idx_stop_slices - (i+1))                

                    slices = lines[idx_start_slices:(idx_stop_slices - lines_to_remove)]
                    actual_n_dyns = len(slices) / info['n_slices'] / info['n_echoes']
                    if not actual_n_dyns.is_integer():
                        msg = "Couldn't fix PAR header (probably multiple randomly dropped frames) for %s. Skipping this run.\n" % iScan
                        warnings.warn(msg)
                        warning_messages = warning_messages + msg
                        break
                        
                else:
                    actual_n_dyns = actual_n_vols

                # Replacing expected with actual number of dynamics
                lines[line_nr_of_dyns] = lines[line_nr_of_dyns].replace(str(info['n_dyns']),
                                                                        str(int(actual_n_dyns)))
                info['n_dyns'] = actual_n_dyns
                with open(iScan, 'w') as f_out:
                    [f_out.write(line) for line in lines]
                print("Done")
                
            else:
                print("Expected number of slices equals number of slices found (%s). No need to fix." % len(slices)) 
                
if len(warning_messages) == 0:
    print("===================================================\n\nfix_truncated_scans: SUMMARY OF WARNINGS:\n\nNo warnings. Lucky you.\n\n===================================================")
else:
    print("===================================================\n\nfix_truncated_scans: SUMMARY OF WARNINGS:\n\n" + warning_messages + "\n===================================================")
