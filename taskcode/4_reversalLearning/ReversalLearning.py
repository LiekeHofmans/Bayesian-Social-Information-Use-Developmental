#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on February 10, 2022, at 17:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# AT THE END OF THE TASK, THE EXPERIMENTER CAN CLOSE THE GAME BY PRESSING 's'.
# OTHERWISE, THE TASK CLOSES AUTOMATICALLY AFTER 10 SECS.


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'ReversalLearning'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\OneDrive\\UvA\\projects\\fMRI_SocialInformation_Uncertainty_adults\\additional_TaskQNR\\ReversalLearning\\ReversalLearning.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1504, 1003], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
# set up datafile
events_filename = _thisDir + os.sep + u'data/sub-%03d_task-reversalLearning_beh' % (int(expInfo['participant']))
eventsFile = data.ExperimentHandler(savePickle=False, saveWideText=True, dataFileName=events_filename)

# Language
language = "Dutch" # "Dutch" or "English"

###############################################################################
### text ###
###############################################################################

# instructions
if language == "Dutch":
    Instr1 = ("WELKOM!\n\n\nJe gaat nu eerst te instructies voor het volgende spel lezen.\n\n"
    "Je kunt heen en weer gaan door de instructies door middel van de LINKER en RECHTER PIJL op het toetsenbord.\n\n\n"
    "Druk nu op de RECHTER pijl om door te gaan naar de instructies.") 

    Instr2 = ("Dit spel bestaat uit meerdere rondes.\n"
    "In iedere ronde moet je kiezen tussen 2 plaatjes: een driehoek of een cirkel.\n\n"
    "Met elke keuze kun je een punt winnen of verliezen.\n"
    "Eén van de symbolen geeft steeds meer kans om te winnen en het andere symbool geeft meer kans om te verliezen.\n\n"
    "Het is jouw taak om erachter te komen welk symbool meer kans geeft om te winnen en dat symbool te kiezen door er met de muis op te klikken, zodat je zoveel mogelijk punten wint.\n\n\n\n")

    Instr3 = ("Als je een punt wint wordt dit aangegeven door een groen, vrolijk gezicht.\n"
    "Als je een punt verliest wordt dit aangegeven door een rood, verdrietig gezicht.\n\n"
    "Je hebt 5 seconden om je antwoord te geven. Als je te laat bent komt er op het scherm ""Te Laat!"" te staan en verlies je ook een punt.")

    Instr4 = ("Wissel:\nGedurende het spel kan het meerdere keren veranderen welk symbool meer kans geeft om te winnen of te verliezen. "
    "Het symbool dat eerst winst opleverde zal nu verlies opleveren (en andersom).\n\n\n"
    "Kans uitkomst:\nIn sommige rondes kan het gebeuren dat je toch verliest, ondanks dat je het symbool had gekozen dat meer kans opleverde om te winnen. "
    "Andersom kan het ook gebeuren dat je toch wint, ondanks dat je het symbool had gekozen dat meer kans opleverde om te verliezen.")

    Instr5 = ("Het spel duurt in totaal ongeveer 10 minuten.\n\n"
    "Als je nog vragen hebt kun je deze nu aan de onderzoeker stellen,\n" 
    "anders kun je op ENTER drukken om het spel te starten.")
elif language == "English": # still need to translate
    Instr1 = ("WELKOM!\n\n\nJe gaat nu eerst te instructies voor het volgende spel lezen.\n\n"
    "Je kunt heen en weer gaan door de instructies door middel van de LINKER en RECHTER PIJL op het toetsenbord.\n\n\n"
    "Druk nu op de RECHTER pijl om door te gaan naar de instructies.") 

    Instr2 = ("Dit spel bestaat uit meerdere rondes.\n"
    "In iedere ronde moet je kiezen tussen 2 plaatjes: een driehoek of een cirkel.\n\n"
    "Met elke keuze kun je een punt winnen of verliezen.\n"
    "Eén van de symbolen geeft steeds meer kans om te winnen en het andere symbool geeft meer kans om te verliezen.\n\n"
    "Het is jouw taak om erachter te komen welk symbool meer kans geeft om te winnen en dat symbool te kiezen door er met de muis op te klikken, zodat je zoveel mogelijk punten wint.\n\n\n\n")

    Instr3 = ("Als je een punt wint wordt dit aangegeven door een groen, vrolijk gezicht.\n"
    "Als je een punt verliest wordt dit aangegeven door een rood, verdrietig gezicht.\n\n"
    "Je hebt 5 seconden om je antwoord te geven. Als je te laat bent komt er op het scherm ""Te Laat!"" te staan en verlies je ook een punt.")

    Instr4 = ("Wissel:\nGedurende het spel kan het meerdere keren veranderen welk symbool meer kans geeft om te winnen of te verliezen. "
    "Het symbool dat eerst winst opleverde zal nu verlies opleveren (en andersom).\n\n\n"
    "Kans uitkomst:\nIn sommige rondes kan het gebeuren dat je toch verliest, ondanks dat je het symbool had gekozen dat meer kans opleverde om te winnen. "
    "Andersom kan het ook gebeuren dat je toch wint, ondanks dat je het symbool had gekozen dat meer kans opleverde om te verliezen.")

    Instr5 = ("Het spel duurt in totaal ongeveer 10 minuten.\n\n"
    "Als je nog vragen hebt kun je deze nu aan de onderzoeker stellen,\n" 
    "anders kun je op ENTER drukken om het spel te starten.")

# other text
if language == "Dutch":
    goodLuck_text = "Houd je hand op te muis.\n\nSucces!" # good luck text right before the task starts
    feedback_text = "Te laat!" # feedback text when too late
    finish_text1 = "Goed gedaan!\n\nDit is het einde van het spel.\nJe hebt in totaal "  # text to tell the participant the game has finished and to convey the total points earned.
    finish_text2 = " punten verdiend.\n\nGeef nu aan de onderzoeker aan dat het spel is afgelopen."
elif language == "English":
    goodLuck_text = "Please keep your hand on the mouse.\n\nGood luck!"
    feedback_text = "Too late!"
    finish_text1 = "Well done!\n\nThis is the end of the game.\nIn total, you earned "
    finish_text2 = " points.\n\nPlease tell the researcher you have finished the game."

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
navigate = keyboard.Keyboard()
InstrDict = { "1": Instr1,
              "2": Instr2, 
              "3": Instr3, 
              "4": Instr4,
              "5": Instr5, 
}

currentInstr = "1"


text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
background_triangle_example = visual.Rect(
    win=win, name='background_triangle_example',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.15, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
triangle_example = visual.ShapeStim(
    win=win, name='triangle_example',
    vertices=[[-(0.15, 0.15)[0]/2.0,-(0.15, 0.15)[1]/2.0], [+(0.15, 0.15)[0]/2.0,-(0.15, 0.15)[1]/2.0], [0,(0.15, 0.15)[1]/2.0]],
    ori=0.0, pos=(-0.15, -0.3),
    lineWidth=15.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-4.0, interpolate=True)
background_circle_example = visual.Rect(
    win=win, name='background_circle_example',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.15, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
circle_example = visual.Polygon(
    win=win, name='circle_example',
    edges=1000, size=(0.15, 0.15),
    ori=0.0, pos=(0.15, -0.3),
    lineWidth=15.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)
happyface_example = visual.ImageStim(
    win=win,
    name='happyface_example', 
    image='happyface.png', mask=None,
    ori=0.0, pos=(-0.15, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
sadface_example = visual.ImageStim(
    win=win,
    name='sadface_example', 
    image='sadface.png', mask=None,
    ori=0.0, pos=(0.15, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "good_luck"
good_luckClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=goodLuck_text,
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
# counterbalance background color of triangle and circle. 
if int(expInfo['participant']) % 2 == 0:
    col_triangle = "royalblue"
    col_circle = "gold"
else:
    col_triangle = "gold"
    col_circle = "royalblue"

# counterbalance block order (which polygon is the best option when?), orthogonal to counterbalancing of background color
if (int(expInfo['participant']) - 1) % 4 < 2:
    reference_polygon = "triangle"
else:
    reference_polygon = "circle"

# set up probabilities and reversals
probability_order = [0.2, 0.8, 0.5, 0.8, 0.2, 0.8, 0.5, 0.2, 0.8, 0.2, 0.5, 0.2, 0.8, 0.5, 0.8, 0.2, 0.5, 0.2, 0.8, 0.2, 0.5, 0.8, 0.5, 0.8, 0.2, 0.8, 0.2, 0.5, 0.8, 0.2, 0.8, 0.5, 0.8, 0.2, 0.5, 0.8, 0.2, 0.5, 0.2, 0.8] # fixed
block_number = 0
new_block = 1 # Is the current trial the start of a new block with new probabilities?
switch_counter = [] # to count how many out of 10 trials was a hit; switch probabilities at 7 out of 10. 

# set up others parameters
maxRT = 5 # 2 sec in Cools et al., 2002
feedback_face = "happyface.png" # initial value, changes according to participant's response. 
previous_outcome = []
previous_response = []
stay_shift = []
points = 0
trial = 1
nTrials = 250
background_triangle = visual.Rect(
    win=win, name='background_triangle',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=col_triangle, fillColor=col_triangle,
    opacity=None, depth=-1.0, interpolate=True)
triangle = visual.ShapeStim(
    win=win, name='triangle',
    vertices=[[-(0.15, 0.15)[0]/2.0,-(0.15, 0.15)[1]/2.0], [+(0.15, 0.15)[0]/2.0,-(0.15, 0.15)[1]/2.0], [0,(0.15, 0.15)[1]/2.0]],
    ori=0.0, pos=[0,0],
    lineWidth=15.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
background_circle = visual.Rect(
    win=win, name='background_circle',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=col_circle, fillColor=col_circle,
    opacity=None, depth=-3.0, interpolate=True)
circle = visual.Polygon(
    win=win, name='circle',
    edges=1000, size=(0.15, 0.15),
    ori=0.0, pos=[0,0],
    lineWidth=15.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-4.0, interpolate=True)
mouseResponse = event.Mouse(win=win)
x, y = [None, None]
mouseResponse.mouseClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
face = visual.ImageStim(
    win=win,
    name='face', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text=feedback_text,
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
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

# set up handler to look after randomisation of conditions etc
loop_instructions = data.TrialHandler(nReps=200.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_instructions')
thisExp.addLoop(loop_instructions)  # add the loop to the experiment
thisLoop_instruction = loop_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction.rgb)
if thisLoop_instruction != None:
    for paramName in thisLoop_instruction:
        exec('{} = thisLoop_instruction[paramName]'.format(paramName))

for thisLoop_instruction in loop_instructions:
    currentLoop = loop_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instruction.rgb)
    if thisLoop_instruction != None:
        for paramName in thisLoop_instruction:
            exec('{} = thisLoop_instruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    navigate.keys = []
    navigate.rt = []
    _navigate_allKeys = []
    text_2.setText(InstrDict[currentInstr])
    background_triangle_example.setFillColor(col_triangle)
    background_triangle_example.setLineColor(col_triangle)
    background_circle_example.setFillColor(col_circle)
    background_circle_example.setLineColor(col_circle)
    # keep track of which components have finished
    instructionsComponents = [navigate, text_2, background_triangle_example, triangle_example, background_circle_example, circle_example, happyface_example, sadface_example]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *navigate* updates
        waitOnFlip = False
        if navigate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            navigate.frameNStart = frameN  # exact frame index
            navigate.tStart = t  # local t and not account for scr refresh
            navigate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(navigate, 'tStartRefresh')  # time at next scr refresh
            navigate.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(navigate.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(navigate.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if navigate.status == STARTED and not waitOnFlip:
            theseKeys = navigate.getKeys(keyList=['right', 'left', 'return', 'num_enter'], waitRelease=False)
            _navigate_allKeys.extend(theseKeys)
            if len(_navigate_allKeys):
                navigate.keys = _navigate_allKeys[-1].name  # just the last key pressed
                navigate.rt = _navigate_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *background_triangle_example* updates
        if background_triangle_example.status == NOT_STARTED and currentInstr == "2":
            # keep track of start time/frame for later
            background_triangle_example.frameNStart = frameN  # exact frame index
            background_triangle_example.tStart = t  # local t and not account for scr refresh
            background_triangle_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_triangle_example, 'tStartRefresh')  # time at next scr refresh
            background_triangle_example.setAutoDraw(True)
        
        # *triangle_example* updates
        if triangle_example.status == NOT_STARTED and currentInstr == "2":
            # keep track of start time/frame for later
            triangle_example.frameNStart = frameN  # exact frame index
            triangle_example.tStart = t  # local t and not account for scr refresh
            triangle_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle_example, 'tStartRefresh')  # time at next scr refresh
            triangle_example.setAutoDraw(True)
        
        # *background_circle_example* updates
        if background_circle_example.status == NOT_STARTED and currentInstr == "2":
            # keep track of start time/frame for later
            background_circle_example.frameNStart = frameN  # exact frame index
            background_circle_example.tStart = t  # local t and not account for scr refresh
            background_circle_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_circle_example, 'tStartRefresh')  # time at next scr refresh
            background_circle_example.setAutoDraw(True)
        
        # *circle_example* updates
        if circle_example.status == NOT_STARTED and currentInstr == "2":
            # keep track of start time/frame for later
            circle_example.frameNStart = frameN  # exact frame index
            circle_example.tStart = t  # local t and not account for scr refresh
            circle_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_example, 'tStartRefresh')  # time at next scr refresh
            circle_example.setAutoDraw(True)
        
        # *happyface_example* updates
        if happyface_example.status == NOT_STARTED and currentInstr == "3":
            # keep track of start time/frame for later
            happyface_example.frameNStart = frameN  # exact frame index
            happyface_example.tStart = t  # local t and not account for scr refresh
            happyface_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(happyface_example, 'tStartRefresh')  # time at next scr refresh
            happyface_example.setAutoDraw(True)
        
        # *sadface_example* updates
        if sadface_example.status == NOT_STARTED and currentInstr == "3":
            # keep track of start time/frame for later
            sadface_example.frameNStart = frameN  # exact frame index
            sadface_example.tStart = t  # local t and not account for scr refresh
            sadface_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sadface_example, 'tStartRefresh')  # time at next scr refresh
            sadface_example.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if (navigate.keys == "return" or navigate.keys == "num_enter") and int(currentInstr) == 5:
        currentInstr = int(currentInstr) + 1
    elif navigate.keys == "right" and int(currentInstr) == 5:
        currentInstr = int(currentInstr)
    elif navigate.keys == "right" and int(currentInstr) != 5:
        currentInstr = int(currentInstr) + 1
    elif navigate.keys == "left":
        currentInstr = int(currentInstr) - 1
    
    if currentInstr == 0:
        currentInstr = 1  # can't go lower than
    elif currentInstr == 6:
        loop_instructions.finished=True
        currentInstr = 1 # otherwise, currentPr will give an error on the next round, because it is out-of-range.
    
    currentInstr = str(currentInstr)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 200.0 repeats of 'loop_instructions'


# ------Prepare to start Routine "good_luck"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
good_luckComponents = [text_3]
for thisComponent in good_luckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
good_luckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "good_luck"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = good_luckClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=good_luckClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in good_luckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "good_luck"-------
for thisComponent in good_luckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1000.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # counterbalance lateral position of triangle and circle
    lateralization = np.random.choice((0,1),size = 1)
    if lateralization == 0:
        position_triangle = "left"
        pos_triangle = -0.15
        pos_circle = 0.15
    elif lateralization == 1:
        position_triangle = "right"
        pos_triangle = 0.15
        pos_circle = -0.15
    
    # define probabilities
    if reference_polygon == "triangle":
        prob_triangle_rewarded = probability_order[block_number]
    elif reference_polygon == "circle":
        prob_triangle_rewarded = 1 - probability_order[block_number] # reverse probabilities if reference polygon is circle (counterbalanced)
    # define correct polygon based on probability value
    if new_block == 1:
        if prob_triangle_rewarded > 0.5:
            correct_polygon = 0
        elif prob_triangle_rewarded < 0.5:
            correct_polygon = 1
        elif prob_triangle_rewarded == 0.5:
            correct_polygon = 1 - correct_polygon
    
    # rename for clarity in output file
    if correct_polygon == 0: 
        correct_polygon_name = "triangle"
    elif correct_polygon == 1:
        correct_polygon_name = "circle"
    
    # define rewarded polygon based on chance
    random_number = np.random.random()
    if random_number <= prob_triangle_rewarded:
        rewarded_polygon = "triangle"
    elif random_number > prob_triangle_rewarded:
        rewarded_polygon = "circle"
    
    # set initial position of mouse
    win.mouseVisible = True
    mouseResponse.setPos(newPos=(0, 0))
    background_triangle.setPos((pos_triangle, 0))
    triangle.setPos((pos_triangle, 0))
    background_circle.setPos((pos_circle, 0))
    circle.setPos((pos_circle, 0))
    # setup some python lists for storing info about the mouseResponse
    mouseResponse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [background_triangle, triangle, background_circle, circle, mouseResponse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # time out after maxRT
        if t > maxRT:
            continueRoutine = False
        
        # *background_triangle* updates
        if background_triangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_triangle.frameNStart = frameN  # exact frame index
            background_triangle.tStart = t  # local t and not account for scr refresh
            background_triangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_triangle, 'tStartRefresh')  # time at next scr refresh
            background_triangle.setAutoDraw(True)
        
        # *triangle* updates
        if triangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            triangle.frameNStart = frameN  # exact frame index
            triangle.tStart = t  # local t and not account for scr refresh
            triangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle, 'tStartRefresh')  # time at next scr refresh
            triangle.setAutoDraw(True)
        
        # *background_circle* updates
        if background_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_circle.frameNStart = frameN  # exact frame index
            background_circle.tStart = t  # local t and not account for scr refresh
            background_circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_circle, 'tStartRefresh')  # time at next scr refresh
            background_circle.setAutoDraw(True)
        
        # *circle* updates
        if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle.frameNStart = frameN  # exact frame index
            circle.tStart = t  # local t and not account for scr refresh
            circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
            circle.setAutoDraw(True)
        # *mouseResponse* updates
        if mouseResponse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseResponse.frameNStart = frameN  # exact frame index
            mouseResponse.tStart = t  # local t and not account for scr refresh
            mouseResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResponse, 'tStartRefresh')  # time at next scr refresh
            mouseResponse.status = STARTED
            mouseResponse.mouseClock.reset()
            prevButtonState = mouseResponse.getPressed()  # if button is down already this ISN'T a new click
        if mouseResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouseResponse.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                mouseResponse.tStop = t  # not accounting for scr refresh
                mouseResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouseResponse, 'tStopRefresh')  # time at next scr refresh
                mouseResponse.status = FINISHED
        if mouseResponse.status == STARTED:  # only update if started and not finished!
            buttons = mouseResponse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [background_triangle, background_circle,]:
                        if obj.contains(mouseResponse):
                            gotValidClick = True
                            mouseResponse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # rt is time right after last screen flip
    response_time = t
    
    # define response
    if mouseResponse.isPressedIn(background_triangle):
        response = "triangle"
    elif mouseResponse.isPressedIn(background_circle):
        response = "circle"
    else: # if no response given / too late; they will get a minus point, but they will have to redo this trial, so they cannot finish the experiment without responding to all 250 trials.
        response = "" 
        response_time = []
    
    # define if was participant was correct (picked high probability polygon)
    if response == correct_polygon_name:
        correct = 1
    else:
        correct = 0
    
    # define if was participant was rewarded
    if response == rewarded_polygon:
        outcome = "win"
    else:
        outcome = "lose"
    
    # define if it was a stay or shift response
    if trial is not 1: 
        if response == previous_response:
            stay_shift = "stay"
        elif response is not previous_response:
            stay_shift = "shift"
    
    # save data
    eventsFile.addData('participant', int(expInfo['participant']))
    eventsFile.addData('trial_number', trial)
    eventsFile.addData('block_number', block_number + 1)
    eventsFile.addData('response', response) 
    eventsFile.addData('response_time', response_time)
    eventsFile.addData('correct', correct)
    eventsFile.addData('outcome', outcome)
    eventsFile.addData('previous_outcome', previous_outcome)
    eventsFile.addData('stay_shift', stay_shift)
    eventsFile.addData('new_block', new_block)
    eventsFile.addData('correct_polygon', correct_polygon_name)
    eventsFile.addData('rewarded_polygon', rewarded_polygon)
    eventsFile.addData('prob_triangle_rewarded', prob_triangle_rewarded)
    eventsFile.addData('position_triangle', position_triangle)
    eventsFile.nextEntry()
    
    # swap the correct / high probability polygon
    # swap if 7 out of the last 10 responses were correct, or after the 16th trial
    if response: # only count as trial if responded
        switch_counter.append(correct)
    if (sum(switch_counter[-10:]) >= 7 and len(switch_counter) >= 10) or len(switch_counter) == 16:
        new_block = 1
        block_number += 1 # switch to next block with new probabilities for next trial
        switch_counter = []
    else:
        new_block = 0
    
    # define feedback
    if response == "": 
        tooLate = 1
        points -= 1
    elif response is not "": 
        tooLate = 0
        trial += 1 # only progress to next trial if responded, not if too late
        if outcome == "win":
            feedback_face = "happyface.png"
            points += 1
        elif outcome == "lose":
            feedback_face = "sadface.png"
            points -= 1
    
    # update previous_outcome and previous_response (only when a response was given)
    if response is not "":
        previous_outcome = outcome
        previous_response = response
    
    # finish task after ntrials
    if trial == nTrials + 1:
        loop_trials.finished=True
    
    # hide cursor
    win.mouseVisible = False
    
    print(eventsFile.getAllEntries())
    # store data for loop_trials (TrialHandler)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    face.setImage(feedback_face)
    # keep track of which components have finished
    feedbackComponents = [face, text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face* updates
        if face.status == NOT_STARTED and tooLate == 0:
            # keep track of start time/frame for later
            face.frameNStart = frameN  # exact frame index
            face.tStart = t  # local t and not account for scr refresh
            face.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face, 'tStartRefresh')  # time at next scr refresh
            face.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tooLate == 1:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if t > 2: 
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000.0 repeats of 'loop_trials'


# ------Prepare to start Routine "finish"-------
continueRoutine = True
# update component parameters for each repeat
# don't give them minus points
if points < 0:
    points_shown = 0
else:
    points_shown = points

finish_text = finish_text1 + format(points_shown, '.0f') + finish_text2

eventsFile.addData('points', points)
eventsFile.addData('points_shown', points_shown)

# Experimenter closes task by pressing "s", or task closes automatically after 10 secs.
text_4.setText(finish_text)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
finishComponents = [text_4, key_resp]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if t > 10:
        continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
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
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
eventsFile.saveAsWideText(events_filename + '.csv', delim='comma')
# make sure everything is closed down
eventsFile.abort()  # or data files will save again on exit

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
