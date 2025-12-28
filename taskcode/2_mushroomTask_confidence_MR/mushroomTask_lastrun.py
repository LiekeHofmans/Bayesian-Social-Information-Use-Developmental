#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on januari 09, 2024, at 11:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import pandas as pd
import numpy as np
from numpy import random
from random import sample
from random import shuffle 
import math




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'mushroomTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'../../../raw_data/sub-%03d/mushroom/sub-%03d_task-mushroom_run-%s_beh' % (int(expInfo['participant']), int(expInfo['participant']), expInfo['run'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='Z:\\fMRI Projects\\fMRI Project Mushroom Highschool\\data_collection\\taskcode\\2_mushroomTask_confidence_MR\\mushroomTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1504, 1003], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "setup"
setupClock = core.Clock()
# window parameters
window_dimension = win.size[0] / win.size[1]
window_y = 0.5
window_x = window_y * window_dimension
aperture_size = window_y * 0.5 # size of square where the mushrooms can be shown (in one direction)
mushroom_size = aperture_size * 0.50 # size of mushroom is 1/10th of screen heigth

maxRT = 100
SI_delay = 4

# background color
bg_color=colors.Color((0, 0, 0), space='rgb')
win.color = bg_color
win.mouseVisible = False

# save empty date
expInfo['date'] = "" # overwrite actual date to deidentify data

events_filename = _thisDir + os.sep + u'../../../raw_data/sub-%03d/mushroom/sub-%03d_task-mushroom_run-%s_events' % (int(expInfo['participant']), int(expInfo['participant']), expInfo['run'])
eventsFile = data.ExperimentHandler(savePickle=False, saveWideText=True, dataFileName=events_filename)


# Initialize components for Routine "start_slide"
start_slideClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Welkom bij het Paddenstoelen spel.\n\nDe onderzoeker zal het spel zo starten.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "import_wave1_data"
import_wave1_dataClock = core.Clock()

# Initialize components for Routine "waitForTrigger"
waitForTriggerClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Succes!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
wait_for_pulse = keyboard.Keyboard()

# Initialize components for Routine "setupSamples"
setupSamplesClock = core.Clock()

# Initialize components for Routine "crossHair"
crossHairClock = core.Clock()
cross_hair = visual.TextStim(win=win, name='cross_hair',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "mushroomSample"
mushroomSampleClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text=None,
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "firstEstimation"
firstEstimationClock = core.Clock()
how_many_mushrooms = visual.TextStim(win=win, name='how_many_mushrooms',
    text='Hoeveel blauwe en rode zakken moeten vandaag worden meegenomen naar het bos?',
    font='Open Sans',
    units='height', pos=(0, 0.4), height=0.032, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
white_rectangle_3 = visual.Rect(
    win=win, name='white_rectangle_3',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18), anchor='center',
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
blue_box = visual.Rect(
    win=win, name='blue_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
showEstimate = visual.TextStim(win=win, name='showEstimate',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='White', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
sliderMarker = visual.Rect(
    win=win, name='sliderMarker',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-5.0, interpolate=True)
red_box = visual.Rect(
    win=win, name='red_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
showEstimate_red = visual.TextStim(win=win, name='showEstimate_red',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='White', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
isi = visual.TextStim(win=win, name='isi',
    text=None,
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SI"
SIClock = core.Clock()
how_many_mushrooms_2 = visual.TextStim(win=win, name='how_many_mushrooms_2',
    text='Hoeveel blauwe en rode zakken moeten vandaag worden meegenomen naar het bos?',
    font='Open Sans',
    units='height', pos=(0, 0.4), height=0.032, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
white_rectangle_peer = visual.Rect(
    win=win, name='white_rectangle_peer',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, 0.02), anchor='center',
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
peer_confidence_rating = visual.ImageStim(
    win=win,
    name='peer_confidence_rating', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.29, 0.21),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blue_box_peer = visual.Rect(
    win=win, name='blue_box_peer',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-5.0, interpolate=True)
sliderMarker_peer = visual.Rect(
    win=win, name='sliderMarker_peer',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-6.0, interpolate=True)
showEstimate_peer = visual.TextStim(win=win, name='showEstimate_peer',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
white_rectangle = visual.Rect(
    win=win, name='white_rectangle',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18), anchor='center',
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
blue_box_E1 = visual.Rect(
    win=win, name='blue_box_E1',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-9.0, interpolate=True)
showEstimate_E1 = visual.TextStim(win=win, name='showEstimate_E1',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
sliderMarker_E1 = visual.Rect(
    win=win, name='sliderMarker_E1',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-11.0, interpolate=True)
blue_box_E2 = visual.Rect(
    win=win, name='blue_box_E2',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-12.0, interpolate=True)
showEstimate_E2 = visual.TextStim(win=win, name='showEstimate_E2',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
sliderMarker_E2 = visual.Rect(
    win=win, name='sliderMarker_E2',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-14.0, interpolate=True)
enterToRespond = visual.TextStim(win=win, name='enterToRespond',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
red_box_peer = visual.Rect(
    win=win, name='red_box_peer',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightcoral', fillColor='lightcoral',
    opacity=None, depth=-16.0, interpolate=True)
showEstimate_red_peer = visual.TextStim(win=win, name='showEstimate_red_peer',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
red_box_E1 = visual.Rect(
    win=win, name='red_box_E1',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightcoral', fillColor='lightcoral',
    opacity=None, depth=-18.0, interpolate=True)
showEstimate_red_E1 = visual.TextStim(win=win, name='showEstimate_red_E1',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
red_box_E2 = visual.Rect(
    win=win, name='red_box_E2',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-20.0, interpolate=True)
showEstimate_red_E2 = visual.TextStim(win=win, name='showEstimate_red_E2',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
estimateOther = visual.TextStim(win=win, name='estimateOther',
    text='Beslissing van ander:',
    font='Open Sans',
    pos=(-0.35, 0.02), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
estimateSelf = visual.TextStim(win=win, name='estimateSelf',
    text='Beslissing van jou:',
    font='Open Sans',
    pos=(-0.35, -0.18), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);

# Initialize components for Routine "tooLate_feedback"
tooLate_feedbackClock = core.Clock()
tooLate_fb = visual.TextStim(win=win, name='tooLate_fb',
    text='Te laat!',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "save_events"
save_eventsClock = core.Clock()

# Initialize components for Routine "showBonus"
showBonusClock = core.Clock()
bonus_text = visual.TextStim(win=win, name='bonus_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
enter_to_end = keyboard.Keyboard()
blue_mushroom_4 = visual.ImageStim(
    win=win,
    name='blue_mushroom_4', 
    image='blue_mushroom.png', mask=None, anchor='center',
    ori=350.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
red_mushroom_4 = visual.ImageStim(
    win=win,
    name='red_mushroom_4', 
    image='red_mushroom.png', mask=None, anchor='center',
    ori=10.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# define trial selection
participant = expInfo['participant']
run = expInfo['run']
randomization = int(participant) % 4
if randomization == 0:
    randomization = 4
trialStructure_file = _thisDir + os.sep + u'trialLists/trial_structure_random%d_run%s.csv' % (randomization, expInfo['run'])
expInfo['trialStructure_file'] = u'trial_structure_random%d_run%s.csv' % (randomization, expInfo['run'])



list_deviance = []
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_slide"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
start_slideComponents = [text_4, key_resp]
for thisComponent in start_slideComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_slide"-------
while continueRoutine:
    # get current time
    t = start_slideClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_slideClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_slideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_slide"-------
for thisComponent in start_slideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start_slide" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "import_wave1_data"-------
continueRoutine = True
# update component parameters for each repeat
wave1Data = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('wave1_input_confidence.csv'),
    seed=None, name='wave1Data')

wave1 = wave1Data.trialList

# make list for filler rounds: 6 x SI which is closer than 3 percentage points, 3 x SI which is further than 40 percentage points. 
SI_fillers = [3, 3, 3, 3, 3, 3, 3, 40, 40, 40, 40]
shuffle(SI_fillers)
# keep track of which components have finished
import_wave1_dataComponents = []
for thisComponent in import_wave1_dataComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
import_wave1_dataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "import_wave1_data"-------
while continueRoutine:
    # get current time
    t = import_wave1_dataClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=import_wave1_dataClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in import_wave1_dataComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "import_wave1_data"-------
for thisComponent in import_wave1_dataComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "import_wave1_data" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "waitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
wait_for_pulse.keys = []
wait_for_pulse.rt = []
_wait_for_pulse_allKeys = []
# keep track of which components have finished
waitForTriggerComponents = [text_5, wait_for_pulse]
for thisComponent in waitForTriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waitForTriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "waitForTrigger"-------
while continueRoutine:
    # get current time
    t = waitForTriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waitForTriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *wait_for_pulse* updates
    if wait_for_pulse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_for_pulse.frameNStart = frameN  # exact frame index
        wait_for_pulse.tStart = t  # local t and not account for scr refresh
        wait_for_pulse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_for_pulse, 'tStartRefresh')  # time at next scr refresh
        wait_for_pulse.status = STARTED
        # keyboard checking is just starting
        wait_for_pulse.clock.reset()  # now t=0
        wait_for_pulse.clearEvents(eventType='keyboard')
    if wait_for_pulse.status == STARTED:
        theseKeys = wait_for_pulse.getKeys(keyList=['t'], waitRelease=False)
        _wait_for_pulse_allKeys.extend(theseKeys)
        if len(_wait_for_pulse_allKeys):
            wait_for_pulse.keys = _wait_for_pulse_allKeys[-1].name  # just the last key pressed
            wait_for_pulse.rt = _wait_for_pulse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "waitForTrigger"-------
for thisComponent in waitForTriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
triggerClock = core.Clock()
#triggerClock = core.monotonicClock

# the Routine "waitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(trialStructure_file),
    seed=None, name='loop_trials')
thisExp.addLoop(loop_trials)  # add the loop to the experiment
thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
if thisLoop_trial != None:
    for paramName in thisLoop_trial:
        exec('{} = thisLoop_trial[paramName]'.format(paramName))

for thisLoop_trial in loop_trials:
    currentLoop = loop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            exec('{} = thisLoop_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setupSamples"-------
    continueRoutine = True
    # update component parameters for each repeat
    # retrieved from file
    nTotal = thisLoop_trial['nTotal']
    true_ratio = thisLoop_trial['trueRatio']
    given_ratio = thisLoop_trial['trueRatio']
    confidence_level = thisLoop_trial['confidence']
    filler_trial = thisLoop_trial['fillerTrial']
    nSamples = 5
    
    # create matrix that specifies the number of observations per sample
    nObservations = [0 for iSample in range(nSamples)]
    nLeft = nTotal
    for iSample in range(1,nSamples+1): # +1 to correct for 0-indexing in Python
        xmin = -1*((nSamples-iSample)*9-nLeft)  # nLeft-x <= (nSamples-iSample)x9, with 5 for number of total samples, 9 for max observations per sample in general. 
        xmin = max(1,xmin) # xmin is either 1, or a higher minimum based on how many observations and samples still need to be shown 
        xmax = -1*((nSamples-iSample)*1-nLeft) # nLeft-x >= (nSamples-iSample)x1, with 5 for number of total samples, 1 for min observations per sample in general.
        xmax = min(9,xmax) # xmax is either 9, or a lower maximum based on how many observations and samples still need to be shown 
        toChooseFrom = [*range(xmin, xmax+1)] # +1 because python reads 'up to but not including xmax'
        x = sample(toChooseFrom,1)[0] # sample returns list; convert list to integer
        nLeft = nLeft - x
        nObservations[iSample-1] = x
    
    # Now create the randomized list with the actual observations to show
    nBlue = round(given_ratio * nTotal)
    seen_ratio = nBlue / nTotal
    nRed = nTotal - nBlue
    itemList = np.array(["blue", "red"])
    itemList = np.repeat(itemList, [nBlue, nRed])
    random.shuffle(itemList)
    
    # Based on the shuffled list with 'red' and 'blue', define how many red's and blue's are in each sample.
    start = 0
    blue = [0 for iSample in range(nSamples)]
    red = [0 for iSample in range(nSamples)]
    for iSample in range(nSamples):
      blue[iSample] = sum(itemList[start:(start+nObservations[iSample])]=="blue")
      red[iSample] = sum(itemList[start:(start+nObservations[iSample])]=="red")
      start = start + nObservations[iSample]
    # keep track of which components have finished
    setupSamplesComponents = []
    for thisComponent in setupSamplesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setupSamplesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setupSamples"-------
    while continueRoutine:
        # get current time
        t = setupSamplesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setupSamplesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupSamplesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setupSamples"-------
    for thisComponent in setupSamplesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sample_index = 0
    
    # initialize start timings of fieldsamples
    Tstart_field1 = []
    Tstart_field2 = []
    Tstart_field3 = []
    Tstart_field4 = []
    Tstart_field5 = []
    # the Routine "setupSamples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crossHair"-------
    continueRoutine = True
    # update component parameters for each repeat
    #crosshair_ITI = round(random.random() * (2.0 - 1.5) + 1.5, 1)
    crosshair_ITI = round(random.random() * (6.0 - 4.0) + 4.0, 1)
    
    win.mouseVisible = False
    # keep track of which components have finished
    crossHairComponents = [cross_hair]
    for thisComponent in crossHairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    crossHairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "crossHair"-------
    while continueRoutine:
        # get current time
        t = crossHairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=crossHairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_hair* updates
        if cross_hair.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_hair.frameNStart = frameN  # exact frame index
            cross_hair.tStart = t  # local t and not account for scr refresh
            cross_hair.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_hair, 'tStartRefresh')  # time at next scr refresh
            cross_hair.setAutoDraw(True)
        if cross_hair.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_hair.tStartRefresh + crosshair_ITI-frameTolerance:
                # keep track of stop time/frame for later
                cross_hair.tStop = t  # not accounting for scr refresh
                cross_hair.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_hair, 'tStopRefresh')  # time at next scr refresh
                cross_hair.setAutoDraw(False)
        if frameN == 1:
            Tstart_crosshair = triggerClock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crossHairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crossHair"-------
    for thisComponent in crossHairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Tend_crosshair = triggerClock.getTime()
    # the Routine "crossHair" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_samples = data.TrialHandler(nReps=5.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_samples')
    thisExp.addLoop(loop_samples)  # add the loop to the experiment
    thisLoop_sample = loop_samples.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_sample.rgb)
    if thisLoop_sample != None:
        for paramName in thisLoop_sample:
            exec('{} = thisLoop_sample[paramName]'.format(paramName))
    
    for thisLoop_sample in loop_samples:
        currentLoop = loop_samples
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_sample.rgb)
        if thisLoop_sample != None:
            for paramName in thisLoop_sample:
                exec('{} = thisLoop_sample[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "mushroomSample"-------
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        # At the start of each sample, create a matrix with x and y coordinates of stimuli on screen
        S = np.array(["blue", "red"])
        # item = thisLoop_sample['item']
        S = np.repeat(S, [blue[sample_index], red[sample_index]])
        ok = 0
        while ok == 0: 
            coor_x = np.array(random.uniform(-aperture_size,aperture_size, nObservations[sample_index]))
            coor_y = np.array(random.uniform(-aperture_size,aperture_size, nObservations[sample_index]))
            diff_x = abs(coor_x[:, None] - coor_x)
            diff_y = abs(coor_y[:, None] - coor_y)
            # check if there is a pair for which both x and y coordinates overlap. If so, resample coordinates
            tooClose = (diff_x <= mushroom_size*0.8) & (diff_y <= mushroom_size*0.8)
            if (np.triu(tooClose, k=1)==False).all(): # only take into account upper triangle to get rid of diagonal which is always 0/True.
                ok = 1
        
        # initialize mushroom images
        if red[sample_index] > 0:
            red_mushrooms = [visual.ImageStim(
                win=win,
                name='red_mushrooms', 
                image='red_mushroom.png', mask=None,
                ori=0.0, pos=(coor_x[i], coor_y[i]), size=[mushroom_size],
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)
               for i in range(red[sample_index])]
            for i in red_mushrooms:
                i.autoDraw = True
        if blue[sample_index] > 0:
            blue_mushrooms = [visual.ImageStim(
                win=win,
                name='blue_mushrooms', 
                image='blue_mushroom.png', mask=None,
                ori=0.0, pos=(coor_x[i], coor_y[i]), size=[mushroom_size],
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0) 
               for i in range(red[sample_index],red[sample_index]+blue[sample_index])]
            for i in blue_mushrooms:
                i.setAutoDraw(True)
        
        
        # keep track of which components have finished
        mushroomSampleComponents = [text_2]
        for thisComponent in mushroomSampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        mushroomSampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "mushroomSample"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = mushroomSampleClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=mushroomSampleClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(False)
            if frameN == 1:
                if sample_index == 0:
                    Tstart_field1 = triggerClock.getTime()
                if sample_index == 1:
                    Tstart_field2 = triggerClock.getTime()
                if sample_index == 2:
                    Tstart_field3 = triggerClock.getTime()
                if sample_index == 3:
                    Tstart_field4 = triggerClock.getTime()
                if sample_index == 4:
                    Tstart_field5 = triggerClock.getTime()
            
            if t < 1.2:
                continueRoutine = True
            else:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mushroomSampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mushroomSample"-------
        for thisComponent in mushroomSampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if sample_index == 0:
            Tend_field1 = triggerClock.getTime()
        if sample_index == 1:
            Tend_field2 = triggerClock.getTime()
        if sample_index == 2:
            Tend_field3 = triggerClock.getTime()
        if sample_index == 3:
            Tend_field4 = triggerClock.getTime()
        if sample_index == 4:
            Tend_field5 = triggerClock.getTime()
        
        
        if red[sample_index] > 0:
            for i in red_mushrooms:
                i.setAutoDraw(False)
        
        if blue[sample_index] > 0:
            for i in blue_mushrooms:
                i.setAutoDraw(False)
        
        sample_index = sample_index + 1
        
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [isi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *isi* updates
            if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                isi.frameNStart = frameN  # exact frame index
                isi.tStart = t  # local t and not account for scr refresh
                isi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
                isi.setAutoDraw(True)
            if isi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > isi.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    isi.tStop = t  # not accounting for scr refresh
                    isi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                    isi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed 5.0 repeats of 'loop_samples'
    
    
    # ------Prepare to start Routine "firstEstimation"-------
    continueRoutine = True
    # update component parameters for each repeat
    kb = keyboard.Keyboard()
    kb.clearEvents()
    
    # initiate slider
    markerPosition = -0.5
    tempRating = 0
    rating = 0
    ratingBeforePressed = 0
    tMove_start = t
    
    nKeys = 0
    submit = 0
    tooLate = 0
    speed = 0
    
    # text about how to submit
    howToRespond = "" 
    
    # keep track of which components have finished
    firstEstimationComponents = [how_many_mushrooms, white_rectangle_3, blue_box, showEstimate, sliderMarker, red_box, showEstimate_red, text_8]
    for thisComponent in firstEstimationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstEstimationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firstEstimation"-------
    while continueRoutine:
        # get current time
        t = firstEstimationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstEstimationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if frameN == 1:
            Tstart_estimate1 = triggerClock.getTime()
        
        # need to manually check for escape, as our key checking will interfere with
        # Builder's escape check:
        events = event.getKeys()
        if 'escape' in events: 
            core.quit()
        
        # check if participant is too late
        rt = t
        if rt > maxRT:
            tooLate = 1
            continueRoutine = False
        
        # move slider colors along with response
        keys = kb.getKeys(['b', 'y', 'e'], waitRelease = False, clear=False)
        keys_released = kb.getKeys(['b', 'y', 'e'], waitRelease = True, clear=False)
        
        # everytime a new button is pressed in, I reset the acceleration with which the slider marker moves
        if len(keys) > nKeys: # new key pressed in
            nKeys = len(keys) # update nKeys
            tMove_start = t # reset speed reference point to start of new button press
            howToRespond = "Druk op ENTER om op te slaan" # show pp can press ENTER as soon as there is a rating
        # check for sticky key: reset speed reference point and keyboard buffer at least every 2 secs
        if (t - tMove_start) > 2:
            kb.clearEvents() # if sticky key, reset keyboard buffer
            nKeys = 0
            tMove_start = t # reset speed reference point 
        
        #released only shows sth when key is released, otherwise empty. 
        #all button presses are stored in keys if clear is false. 
        # button down if keys(end).duration == None and len(keys) == len(released) + 1
        if len(keys) > len(keys_released): # button pressed in, but not yet released
            if keys[len(keys)-1].duration is not None: # keys is longer than keys released because there is a sticky key, not because a key is actually pressed in 
                kb.clearEvents()
                nKeys = 0
                tMove_start = t # reset speed reference point 
            else:
                speed = min(t - tMove_start, 2) # the longer pressed in, the faster the slider moves, with a maximum speed after 2 sec
                key = keys[len(keys)-1].name
                if key == 'b':
                    tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                    submit = 1
                elif key =='y': 
                    tempRating += math.exp(speed*1.5)-1
                    submit = 1
                elif key == 'e' and submit == 1:
                    continueRoutine = False
        elif len(keys) == len(keys_released): # all buttons released
            # make sure rating moves at least 1 tick if it was shortly pressed and released (a very low ratinTemp might otherwise be rounded to a stepsize of 0)
            if tempRating > ratingBeforePressed:
                tempRating = max(ratingBeforePressed+1, tempRating)
            elif tempRating < ratingBeforePressed:
                tempRating = min(ratingBeforePressed-1, tempRating)
            ratingBeforePressed = tempRating
        
        # Make sure rating does not exceed limits of 0 and 100
        tempRating = min(tempRating, 100)
        tempRating = max(tempRating, 0)
        rating = round(tempRating)
        markerPosition = (rating - 50) / 100
        
        
        
        # *how_many_mushrooms* updates
        if how_many_mushrooms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            how_many_mushrooms.frameNStart = frameN  # exact frame index
            how_many_mushrooms.tStart = t  # local t and not account for scr refresh
            how_many_mushrooms.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(how_many_mushrooms, 'tStartRefresh')  # time at next scr refresh
            how_many_mushrooms.setAutoDraw(True)
        
        # *white_rectangle_3* updates
        if white_rectangle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_rectangle_3.frameNStart = frameN  # exact frame index
            white_rectangle_3.tStart = t  # local t and not account for scr refresh
            white_rectangle_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_rectangle_3, 'tStartRefresh')  # time at next scr refresh
            white_rectangle_3.setAutoDraw(True)
        
        # *blue_box* updates
        if blue_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_box.frameNStart = frameN  # exact frame index
            blue_box.tStart = t  # local t and not account for scr refresh
            blue_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_box, 'tStartRefresh')  # time at next scr refresh
            blue_box.setAutoDraw(True)
        if blue_box.status == STARTED:  # only update if drawing
            blue_box.setPos([markerPosition-0.026, -0.135], log=False)
        
        # *showEstimate* updates
        if showEstimate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate.frameNStart = frameN  # exact frame index
            showEstimate.tStart = t  # local t and not account for scr refresh
            showEstimate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate, 'tStartRefresh')  # time at next scr refresh
            showEstimate.setAutoDraw(True)
        if showEstimate.status == STARTED:  # only update if drawing
            showEstimate.setPos([markerPosition-0.026, -0.135], log=False)
            showEstimate.setText(int(rating), log=False)
        
        # *sliderMarker* updates
        if sliderMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderMarker.frameNStart = frameN  # exact frame index
            sliderMarker.tStart = t  # local t and not account for scr refresh
            sliderMarker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderMarker, 'tStartRefresh')  # time at next scr refresh
            sliderMarker.setAutoDraw(True)
        if sliderMarker.status == STARTED:  # only update if drawing
            sliderMarker.setPos([markerPosition, -0.18], log=False)
        
        # *red_box* updates
        if red_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_box.frameNStart = frameN  # exact frame index
            red_box.tStart = t  # local t and not account for scr refresh
            red_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_box, 'tStartRefresh')  # time at next scr refresh
            red_box.setAutoDraw(True)
        if red_box.status == STARTED:  # only update if drawing
            red_box.setPos([markerPosition+0.026, -0.225], log=False)
        
        # *showEstimate_red* updates
        if showEstimate_red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_red.frameNStart = frameN  # exact frame index
            showEstimate_red.tStart = t  # local t and not account for scr refresh
            showEstimate_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_red, 'tStartRefresh')  # time at next scr refresh
            showEstimate_red.setAutoDraw(True)
        if showEstimate_red.status == STARTED:  # only update if drawing
            showEstimate_red.setPos([markerPosition+0.026, -0.225], log=False)
            showEstimate_red.setText(100-int(rating), log=False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:  # only update if drawing
            text_8.setText(howToRespond, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firstEstimationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firstEstimation"-------
    for thisComponent in firstEstimationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Tend_estimate1 = triggerClock.getTime()
    
    kb.clearEvents()
    
    # performance
    estimate1 = int(rating)
    if tooLate == 0:
        estimate1_rt = rt
        deviance = estimate1 - true_ratio*100
        abs_deviance = abs(deviance)
    elif tooLate == 1:
        estimate1_rt = []
    # save data 
    loop_trials.addData('cross_hair.ITI', crosshair_ITI)
    loop_trials.addData('seen_ratio', seen_ratio)
    loop_trials.addData('nMushrooms', " ".join(map(str, nObservations)))
    loop_trials.addData('nBlue', " ".join(map(str, blue)))
    loop_trials.addData('nRed', " ".join(map(str, red)))
    loop_trials.addData('estimation1.rating', estimate1)
    loop_trials.addData('estimation1.rt', estimate1_rt)
    if tooLate == 0:
        list_deviance.append(abs_deviance)
    
    
    # the Routine "firstEstimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi* updates
        if isi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi.frameNStart = frameN  # exact frame index
            isi.tStart = t  # local t and not account for scr refresh
            isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi, 'tStartRefresh')  # time at next scr refresh
            isi.setAutoDraw(True)
        if isi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                isi.tStop = t  # not accounting for scr refresh
                isi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi, 'tStopRefresh')  # time at next scr refresh
                isi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "SI"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.clearEvents()
    
    # do not run if participant was too late at first estimation 
    if tooLate == 1:
        continueRoutine = False
        estimate1 = 100 # set random estimate so program doesnt crash
    
    # filter wave1 data based on current ratio and confidence level
    filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level] # filter wave1 data / social information based on current ratio and confidence level
    # never show peer estimate of 0 or 100 (might not be believable in case participant saw both colors).
    filtered_SI = [row for row in filtered_SI if row['estimate']>0 and row['estimate']<100]
    
    # pick SI for which estimate is 15-18 percentage points in direction of true ratio. 
    delta = int(estimate1 - true_ratio * 100);
    if filler_trial == 1: # pick a peer estimate that is either super close or super far, in any direction
        close_far = SI_fillers[0]; # pick first element of shuffled list
        if true_ratio == 0 or true_ratio == 1:
            close_far = 3 # to make it more believable
        if close_far == 3:
            filtered_SI2 = [row for row in filtered_SI if row['estimate'] > estimate1 - 3 and row['estimate'] < estimate1 + 3]
            if len(filtered_SI2) == 0:
                close_far = 40;
        if close_far == 40:
            filtered_SI2 = [row for row in filtered_SI if (row['estimate'] < estimate1 - 40 or row['estimate'] > estimate1 + 40)]
        if true_ratio != 0 and true_ratio != 1:
            SI_fillers.remove(close_far)  # remove used filler trial from list
    elif delta > 0:
        if estimate1 < 16:
            filtered_SI2 = [row for row in filtered_SI if row['estimate'] == 1]
        else: 
            filtered_SI2 = [row for row in filtered_SI if row['estimate'] > estimate1 - 19 and row['estimate'] < estimate1 - 14]
    elif delta < 0:
        if estimate1 > 84:
            filtered_SI2 = [row for row in filtered_SI if row['estimate'] == 99]
        else: 
            filtered_SI2 = [row for row in filtered_SI if row['estimate'] < estimate1 + 19 and row['estimate'] > estimate1 + 14]
    elif delta == 0: # any direction
        filtered_SI2 = [row for row in filtered_SI if (row['estimate'] > estimate1 - 19 and row['estimate'] < estimate1 - 14) or (row['estimate'] < estimate1 + 19 and row['estimate'] > estimate1 + 14)]
    
    
    # if no suitable SI could be found, just include all SI only filtered based on ratio and confidence.
    if len(filtered_SI2) == 0:
        filtered_SI2 = filtered_SI
    
    # now randomly choose a peer estimate from filtered list
    random_index = int(random.randint(0,len(filtered_SI2),1))
    peer_estimate = filtered_SI2[random_index]['estimate']
    
    
    # define image to show about peers confidence 
    if confidence_level == 1:
        peers_confidence_image = "low_peerConfidence.png"
    elif confidence_level == 2:
        peers_confidence_image = "medium_peerConfidence.png"
    elif confidence_level == 3:
        peers_confidence_image = "high_peerConfidence.png"
    
    # parameters for visual peer estimate information 
    markerPosition_peer = (peer_estimate - 50) / 100
    
    # do not run if participant was too late at first estimation
    if tooLate == 1:
        continueRoutine = False
    
    kb = keyboard.Keyboard()
    kb.clearEvents()
    
    # initiate slider
    markerPosition_E1 = (estimate1-50) / 100
    markerPosition_E2 = -0.5
    tempRating = 0
    rating = 0
    ratingBeforePressed = 0
    tMove_start = t
    
    nKeys = 0
    submit = 0
    speed = 0
    SI_delay_done = 0
    
    # set alignment of text
    estimateOther.alignText='left'
    estimateSelf.alignText='left'
    
    # text about how to submit
    howToRespond = "" 
    
    
    peer_confidence_rating.setPos((markerPosition_peer, 0.21))
    peer_confidence_rating.setImage(peers_confidence_image)
    blue_box_peer.setPos([markerPosition_peer-0.026, 0.065])
    sliderMarker_peer.setPos([markerPosition_peer, 0.02])
    showEstimate_peer.setPos([markerPosition_peer-0.026, 0.065])
    showEstimate_peer.setText(peer_estimate)
    blue_box_E1.setPos([markerPosition_E1-0.026, -0.135])
    showEstimate_E1.setText(int(estimate1))
    sliderMarker_E1.setPos([markerPosition_E1, -0.18])
    red_box_peer.setPos([markerPosition_peer+0.026, -0.025])
    showEstimate_red_peer.setPos([markerPosition_peer+0.026, -0.025])
    showEstimate_red_peer.setText(100-peer_estimate)
    red_box_E1.setPos([markerPosition_E1+0.026, -0.225])
    showEstimate_red_E1.setText(100-int(estimate1))
    # keep track of which components have finished
    SIComponents = [how_many_mushrooms_2, white_rectangle_peer, peer_confidence_rating, blue_box_peer, sliderMarker_peer, showEstimate_peer, white_rectangle, blue_box_E1, showEstimate_E1, sliderMarker_E1, blue_box_E2, showEstimate_E2, sliderMarker_E2, enterToRespond, red_box_peer, showEstimate_red_peer, red_box_E1, showEstimate_red_E1, red_box_E2, showEstimate_red_E2, estimateOther, estimateSelf]
    for thisComponent in SIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SI"-------
    while continueRoutine:
        # get current time
        t = SIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if frameN == 1: 
            Tstart_SI = triggerClock.getTime()
        
        # need to manually check for escape, as our key checking will interfere with
        # Builder's escape check:
        events = event.getKeys()
        if 'escape' in events: 
            core.quit()
        
        # check if participant is too late
        rt = t
        if rt > SI_delay + maxRT:
            tooLate = 1
            continueRoutine = False
        
        # ONLY START RECORDING KEYBOARD PRESSES AFTER SI_DELAY
        if t > SI_delay:
            if SI_delay_done == 0:
                Tend_SI = triggerClock.getTime()
                Tstart_estimate2 = triggerClock.getTime()
        
            # move slider colors along with response
            keys = kb.getKeys(['b', 'y', 'e'], waitRelease = False, clear=False)
            keys_released = kb.getKeys(['b', 'y', 'e'], waitRelease = True, clear=False)
        
            # everytime a new button is pressed in, I reset the speed with which the slider marker moves
            if len(keys) > nKeys: # new key pressed in
                nKeys = len(keys) # update nKeys
                tMove_start = t # reset speed reference point to start of new button press
                howToRespond = "Druk op ENTER om op te slaan" # show pp can press ENTER as soon as there is a rating
            # check for sticky key: reset speed reference point and keyboard buffer at least every 2 secs
            if (t - tMove_start) > 2:
                kb.clearEvents() # if sticky key, reset keyboard buffer
                nKeys = 0
                tMove_start = t # reset speed reference point 
        
            #released only shows sth when key is released, otherwise empty. 
            #all button presses are stored in keys if clear is false. 
            # button down if keys(end).duration == None and len(keys) == len(released) + 1
            if len(keys) > len(keys_released): # button pressed in, but not yet released
                if keys[len(keys)-1].duration is not None: # keys is longer than keys released because there is a sticky key, not because a key is actually pressed in 
                    kb.clearEvents()
                    nKeys = 0
                    tMove_start = t # reset speed reference point 
                else:
                    speed = min(t - tMove_start, 2) # the longer pressed in, the faster the slider moves, with a maximum speed after 2 sec
                    key = keys[len(keys)-1].name
                    if key == 'b':
                        tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                        submit = 1
                    elif key =='y': 
                        tempRating += math.exp(speed*1.5)-1
                        submit = 1
                    elif key == 'e' and submit == 1:
                        continueRoutine = False
            elif len(keys) == len(keys_released): # all buttons released
                # make sure rating moves at least 1 tick if it was shortly pressed and released (a very low ratinTemp might otherwise be rounded to a stepsize of 0)
                if tempRating > ratingBeforePressed:
                    tempRating = max(ratingBeforePressed+1, tempRating)
                elif tempRating < ratingBeforePressed:
                    tempRating = min(ratingBeforePressed-1, tempRating)
                ratingBeforePressed = tempRating
        
            # Make sure rating does not exceed limits of 0 and 100
            tempRating = min(tempRating, 100)
            tempRating = max(tempRating, 0)
            rating = round(tempRating)
            markerPosition_E2 = (rating - 50) / 100
        
            SI_delay_done = 1
        
        
        
        
        
        
        
        # *how_many_mushrooms_2* updates
        if how_many_mushrooms_2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            how_many_mushrooms_2.frameNStart = frameN  # exact frame index
            how_many_mushrooms_2.tStart = t  # local t and not account for scr refresh
            how_many_mushrooms_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(how_many_mushrooms_2, 'tStartRefresh')  # time at next scr refresh
            how_many_mushrooms_2.setAutoDraw(True)
        
        # *white_rectangle_peer* updates
        if white_rectangle_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_rectangle_peer.frameNStart = frameN  # exact frame index
            white_rectangle_peer.tStart = t  # local t and not account for scr refresh
            white_rectangle_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_rectangle_peer, 'tStartRefresh')  # time at next scr refresh
            white_rectangle_peer.setAutoDraw(True)
        
        # *peer_confidence_rating* updates
        if peer_confidence_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            peer_confidence_rating.frameNStart = frameN  # exact frame index
            peer_confidence_rating.tStart = t  # local t and not account for scr refresh
            peer_confidence_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(peer_confidence_rating, 'tStartRefresh')  # time at next scr refresh
            peer_confidence_rating.setAutoDraw(True)
        
        # *blue_box_peer* updates
        if blue_box_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_box_peer.frameNStart = frameN  # exact frame index
            blue_box_peer.tStart = t  # local t and not account for scr refresh
            blue_box_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_box_peer, 'tStartRefresh')  # time at next scr refresh
            blue_box_peer.setAutoDraw(True)
        
        # *sliderMarker_peer* updates
        if sliderMarker_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderMarker_peer.frameNStart = frameN  # exact frame index
            sliderMarker_peer.tStart = t  # local t and not account for scr refresh
            sliderMarker_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderMarker_peer, 'tStartRefresh')  # time at next scr refresh
            sliderMarker_peer.setAutoDraw(True)
        
        # *showEstimate_peer* updates
        if showEstimate_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_peer.frameNStart = frameN  # exact frame index
            showEstimate_peer.tStart = t  # local t and not account for scr refresh
            showEstimate_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_peer, 'tStartRefresh')  # time at next scr refresh
            showEstimate_peer.setAutoDraw(True)
        
        # *white_rectangle* updates
        if white_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_rectangle.frameNStart = frameN  # exact frame index
            white_rectangle.tStart = t  # local t and not account for scr refresh
            white_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_rectangle, 'tStartRefresh')  # time at next scr refresh
            white_rectangle.setAutoDraw(True)
        
        # *blue_box_E1* updates
        if blue_box_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_box_E1.frameNStart = frameN  # exact frame index
            blue_box_E1.tStart = t  # local t and not account for scr refresh
            blue_box_E1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_box_E1, 'tStartRefresh')  # time at next scr refresh
            blue_box_E1.setAutoDraw(True)
        
        # *showEstimate_E1* updates
        if showEstimate_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_E1.frameNStart = frameN  # exact frame index
            showEstimate_E1.tStart = t  # local t and not account for scr refresh
            showEstimate_E1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_E1, 'tStartRefresh')  # time at next scr refresh
            showEstimate_E1.setAutoDraw(True)
        if showEstimate_E1.status == STARTED:  # only update if drawing
            showEstimate_E1.setPos([markerPosition_E1-0.026, -0.135], log=False)
        
        # *sliderMarker_E1* updates
        if sliderMarker_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderMarker_E1.frameNStart = frameN  # exact frame index
            sliderMarker_E1.tStart = t  # local t and not account for scr refresh
            sliderMarker_E1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderMarker_E1, 'tStartRefresh')  # time at next scr refresh
            sliderMarker_E1.setAutoDraw(True)
        
        # *blue_box_E2* updates
        if blue_box_E2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            blue_box_E2.frameNStart = frameN  # exact frame index
            blue_box_E2.tStart = t  # local t and not account for scr refresh
            blue_box_E2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_box_E2, 'tStartRefresh')  # time at next scr refresh
            blue_box_E2.setAutoDraw(True)
        if blue_box_E2.status == STARTED:  # only update if drawing
            blue_box_E2.setPos([markerPosition_E2-0.026, -0.135], log=False)
        
        # *showEstimate_E2* updates
        if showEstimate_E2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_E2.frameNStart = frameN  # exact frame index
            showEstimate_E2.tStart = t  # local t and not account for scr refresh
            showEstimate_E2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_E2, 'tStartRefresh')  # time at next scr refresh
            showEstimate_E2.setAutoDraw(True)
        if showEstimate_E2.status == STARTED:  # only update if drawing
            showEstimate_E2.setPos([markerPosition_E2-0.026, -0.135], log=False)
            showEstimate_E2.setText(int(rating), log=False)
        
        # *sliderMarker_E2* updates
        if sliderMarker_E2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            sliderMarker_E2.frameNStart = frameN  # exact frame index
            sliderMarker_E2.tStart = t  # local t and not account for scr refresh
            sliderMarker_E2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderMarker_E2, 'tStartRefresh')  # time at next scr refresh
            sliderMarker_E2.setAutoDraw(True)
        if sliderMarker_E2.status == STARTED:  # only update if drawing
            sliderMarker_E2.setPos([markerPosition_E2, -0.18], log=False)
        
        # *enterToRespond* updates
        if enterToRespond.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            enterToRespond.frameNStart = frameN  # exact frame index
            enterToRespond.tStart = t  # local t and not account for scr refresh
            enterToRespond.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enterToRespond, 'tStartRefresh')  # time at next scr refresh
            enterToRespond.setAutoDraw(True)
        if enterToRespond.status == STARTED:  # only update if drawing
            enterToRespond.setText(howToRespond, log=False)
        
        # *red_box_peer* updates
        if red_box_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_box_peer.frameNStart = frameN  # exact frame index
            red_box_peer.tStart = t  # local t and not account for scr refresh
            red_box_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_box_peer, 'tStartRefresh')  # time at next scr refresh
            red_box_peer.setAutoDraw(True)
        
        # *showEstimate_red_peer* updates
        if showEstimate_red_peer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_red_peer.frameNStart = frameN  # exact frame index
            showEstimate_red_peer.tStart = t  # local t and not account for scr refresh
            showEstimate_red_peer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_red_peer, 'tStartRefresh')  # time at next scr refresh
            showEstimate_red_peer.setAutoDraw(True)
        
        # *red_box_E1* updates
        if red_box_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_box_E1.frameNStart = frameN  # exact frame index
            red_box_E1.tStart = t  # local t and not account for scr refresh
            red_box_E1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_box_E1, 'tStartRefresh')  # time at next scr refresh
            red_box_E1.setAutoDraw(True)
        
        # *showEstimate_red_E1* updates
        if showEstimate_red_E1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_red_E1.frameNStart = frameN  # exact frame index
            showEstimate_red_E1.tStart = t  # local t and not account for scr refresh
            showEstimate_red_E1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_red_E1, 'tStartRefresh')  # time at next scr refresh
            showEstimate_red_E1.setAutoDraw(True)
        if showEstimate_red_E1.status == STARTED:  # only update if drawing
            showEstimate_red_E1.setPos([markerPosition_E1+0.026, -0.225], log=False)
        
        # *red_box_E2* updates
        if red_box_E2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            red_box_E2.frameNStart = frameN  # exact frame index
            red_box_E2.tStart = t  # local t and not account for scr refresh
            red_box_E2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_box_E2, 'tStartRefresh')  # time at next scr refresh
            red_box_E2.setAutoDraw(True)
        if red_box_E2.status == STARTED:  # only update if drawing
            red_box_E2.setPos([markerPosition_E2+0.026, -0.225], log=False)
        
        # *showEstimate_red_E2* updates
        if showEstimate_red_E2.status == NOT_STARTED and tThisFlip >= SI_delay-frameTolerance:
            # keep track of start time/frame for later
            showEstimate_red_E2.frameNStart = frameN  # exact frame index
            showEstimate_red_E2.tStart = t  # local t and not account for scr refresh
            showEstimate_red_E2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(showEstimate_red_E2, 'tStartRefresh')  # time at next scr refresh
            showEstimate_red_E2.setAutoDraw(True)
        if showEstimate_red_E2.status == STARTED:  # only update if drawing
            showEstimate_red_E2.setPos([markerPosition_E2+0.026, -0.225], log=False)
            showEstimate_red_E2.setText(100-int(rating), log=False)
        
        # *estimateOther* updates
        if estimateOther.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            estimateOther.frameNStart = frameN  # exact frame index
            estimateOther.tStart = t  # local t and not account for scr refresh
            estimateOther.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(estimateOther, 'tStartRefresh')  # time at next scr refresh
            estimateOther.setAutoDraw(True)
        
        # *estimateSelf* updates
        if estimateSelf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            estimateSelf.frameNStart = frameN  # exact frame index
            estimateSelf.tStart = t  # local t and not account for scr refresh
            estimateSelf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(estimateSelf, 'tStartRefresh')  # time at next scr refresh
            estimateSelf.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SI"-------
    for thisComponent in SIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Tend_estimate2 = triggerClock.getTime()
    
    kb.clearEvents()
    
    estimate2 = int(rating)
    # performance
    if tooLate == 0:
        estimate2_rt = rt-SI_delay
        deviance = estimate2 - true_ratio*100
        abs_deviance = abs(deviance)
    elif tooLate == 1:
        estimate2_rt = []
    
    # save data
    loop_trials.addData('confidence_own.rating', []) # only for practice, not in fMRI task
    loop_trials.addData('confidence_own.rt', []) # only for practice, not in fMRI task
    loop_trials.addData('estimation2.rating', estimate2)
    loop_trials.addData('estimation2.rt', estimate2_rt)
    if tooLate == 0:
        list_deviance.append(abs_deviance)
    loop_trials.addData('estimate_peer', peer_estimate)
    loop_trials.addData('confidence_peer', confidence_level)
    if loop_trials.nRemaining == 0:
        list_deviance = np.array(list_deviance)
        sample_deviance = round(sample(list(list_deviance),1)[0])
        bonus = 1.50 - sample_deviance*0.04
        if bonus < 0:
            bonus = 0 # never lower than
        if int(expInfo['run']) == 3:
            expInfo['bonus'] = bonus # only save on last run
        else: 
            expInfo['bonus'] = [] 
    
    # the Routine "SI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "tooLate_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # only run if participant was too late
    if tooLate == 0:
        continueRoutine = False
    # keep track of which components have finished
    tooLate_feedbackComponents = [tooLate_fb]
    for thisComponent in tooLate_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tooLate_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tooLate_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = tooLate_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tooLate_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tooLate_fb* updates
        if tooLate_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tooLate_fb.frameNStart = frameN  # exact frame index
            tooLate_fb.tStart = t  # local t and not account for scr refresh
            tooLate_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tooLate_fb, 'tStartRefresh')  # time at next scr refresh
            tooLate_fb.setAutoDraw(True)
        if tooLate_fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tooLate_fb.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                tooLate_fb.tStop = t  # not accounting for scr refresh
                tooLate_fb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tooLate_fb, 'tStopRefresh')  # time at next scr refresh
                tooLate_fb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tooLate_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tooLate_feedback"-------
    for thisComponent in tooLate_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "save_events"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    save_eventsComponents = []
    for thisComponent in save_eventsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    save_eventsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "save_events"-------
    while continueRoutine:
        # get current time
        t = save_eventsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=save_eventsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in save_eventsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "save_events"-------
    for thisComponent in save_eventsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Tend_trial = triggerClock.getTime()
    
    # save 
    
    eventsFile.addData('onset', Tstart_crosshair)
    eventsFile.addData('duration', Tend_trial - Tstart_crosshair)
    eventsFile.addData('trial_number', loop_trials.thisN + 1 + 25 * (int(expInfo['run'])-1) )
    if nTotal == 5 and confidence_level == 1:
        eventsFile.addData('trial_type', "low_low")
    elif nTotal == 5 and confidence_level == 2:
        eventsFile.addData('trial_type', "low_medium")
    elif nTotal == 5 and confidence_level == 3:
        eventsFile.addData('trial_type', "low_high")
    elif nTotal == 45 and confidence_level == 1:
        eventsFile.addData('trial_type', "high_low")
    elif nTotal == 45 and confidence_level == 2:
        eventsFile.addData('trial_type', "high_medium")
    elif nTotal == 45 and confidence_level == 3:
        eventsFile.addData('trial_type', "high_high")
    eventsFile.addData('estimate1', estimate1)
    eventsFile.addData('estimate1_rt', estimate1_rt)
    eventsFile.addData('estimate_peer', peer_estimate)
    eventsFile.addData('estimate2', estimate2)
    eventsFile.addData('estimate2_rt', estimate2_rt)
    eventsFile.addData('true_ratio', true_ratio)
    eventsFile.addData('seen_ratio', seen_ratio)
    eventsFile.addData('filler_trial', filler_trial)
    
    # save all timings
    
    # crosshair
    eventsFile.addData('onset_crosshair', Tstart_crosshair)
    eventsFile.addData('duration_crosshair', Tend_crosshair - Tstart_crosshair)
    
    # mushroom fields /samples
    eventsFile.addData('onset_field1', Tstart_field1)
    eventsFile.addData('duration_field1', Tend_field1 - Tstart_field1)
    
    if Tstart_field5: # only save when all samples are shown and their timing is thus recorded (during piloting, I sometimes set the number of fields to 1 to go faster)
        eventsFile.addData('onset_field2', Tstart_field2)
        eventsFile.addData('duration_field2', Tend_field2 - Tstart_field2)
    
        eventsFile.addData('onset_field3', Tstart_field3)
        eventsFile.addData('duration_field3', Tend_field3 - Tstart_field3)
    
        eventsFile.addData('onset_field4', Tstart_field4)
        eventsFile.addData('duration_field4', Tend_field4 - Tstart_field4)
    
        eventsFile.addData('onset_field5', Tstart_field5)
        eventsFile.addData('duration_field5', Tend_field5 - Tstart_field5)
    
    # first estimation phase
    eventsFile.addData('onset_estimate1', Tstart_estimate1)
    eventsFile.addData('duration_estimate1', Tend_estimate1 - Tstart_estimate1)
    
    # second estimation phase
    if Tstart_SI: # non existent when pp was too late on first estimate
        eventsFile.addData('onset_SI', Tstart_SI)
        eventsFile.addData('duration_SI', Tend_SI - Tstart_SI)
    
        eventsFile.addData('onset_estimate2', Tstart_estimate2)
        eventsFile.addData('duration_estimate2', Tend_estimate2 - Tstart_estimate2)
    
    
    #end of trial, next line:
    eventsFile.nextEntry()
    # the Routine "save_events" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_trials'


# ------Prepare to start Routine "showBonus"-------
continueRoutine = True
# update component parameters for each repeat
event.clearEvents()

# sprintf function doesnt automatically translate from py to JS, so solved it this way
if run == '3':
    text1 = "Goed gedaan!\n\nDit is het einde van het laatste oogstseizoen.\n\n"
    text2 = "Op de dag die door de computer is geselecteerd verschilde het aantal paddenstoelen plukkers dat je het bos in hebt gestuurd met een blauwe of rode zak "
    text3 = format(sample_deviance, '.0f')
    text4 = " zakken van het goede antwoord.\n\nJe bonus is daarom €1.50 - "
    text5 = " x €0.04 =\n\n€"
    text6 = format(bonus, '.2f')
    text7 = "\n\n\nDe onderzoeker zal zo het spel beëindigen."
    end_text =  text1 + text2 + text3 + text4 + text3 + text5 + text6 + text7
else: 
    text1 = "Goed gedaan!\n\nDit is het einde van oogstseizoen "
    text2 = run
    text3 = ".\n\n"
    text4 = "Je hebt nu even pauze voordat je begint aan het volgende seizoen."
    end_text =  text1 + text2 + text3 + text4

bonus_text.setText(end_text)
enter_to_end.keys = []
enter_to_end.rt = []
_enter_to_end_allKeys = []
blue_mushroom_4.setPos((window_x-0.3, -0.4))
red_mushroom_4.setPos((window_x-0.2, -0.4))
# keep track of which components have finished
showBonusComponents = [bonus_text, enter_to_end, blue_mushroom_4, red_mushroom_4]
for thisComponent in showBonusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
showBonusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "showBonus"-------
while continueRoutine:
    # get current time
    t = showBonusClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=showBonusClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bonus_text* updates
    if bonus_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bonus_text.frameNStart = frameN  # exact frame index
        bonus_text.tStart = t  # local t and not account for scr refresh
        bonus_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bonus_text, 'tStartRefresh')  # time at next scr refresh
        bonus_text.setAutoDraw(True)
    
    # *enter_to_end* updates
    waitOnFlip = False
    if enter_to_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_to_end.frameNStart = frameN  # exact frame index
        enter_to_end.tStart = t  # local t and not account for scr refresh
        enter_to_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_to_end, 'tStartRefresh')  # time at next scr refresh
        enter_to_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter_to_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter_to_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_to_end.status == STARTED and not waitOnFlip:
        theseKeys = enter_to_end.getKeys(keyList=['s'], waitRelease=False)
        _enter_to_end_allKeys.extend(theseKeys)
        if len(_enter_to_end_allKeys):
            enter_to_end.keys = _enter_to_end_allKeys[-1].name  # just the last key pressed
            enter_to_end.rt = _enter_to_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *blue_mushroom_4* updates
    if blue_mushroom_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blue_mushroom_4.frameNStart = frameN  # exact frame index
        blue_mushroom_4.tStart = t  # local t and not account for scr refresh
        blue_mushroom_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blue_mushroom_4, 'tStartRefresh')  # time at next scr refresh
        blue_mushroom_4.setAutoDraw(True)
    
    # *red_mushroom_4* updates
    if red_mushroom_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_mushroom_4.frameNStart = frameN  # exact frame index
        red_mushroom_4.tStart = t  # local t and not account for scr refresh
        red_mushroom_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_mushroom_4, 'tStartRefresh')  # time at next scr refresh
        red_mushroom_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in showBonusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "showBonus"-------
for thisComponent in showBonusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "showBonus" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
eventsFile.saveAsWideText(events_filename + '.tsv', delim='tab')
# make sure everything is closed down
eventsFile.abort()  # or data files will save again on exit


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
