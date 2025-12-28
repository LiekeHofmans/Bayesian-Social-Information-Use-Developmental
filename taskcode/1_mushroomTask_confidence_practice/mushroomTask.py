#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on maart 10, 2022, at 09:13
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
psychopyVersion = '2021.2.3'
expName = 'mushroomTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': 'prac'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'../../../raw_data/sub-%03d/mushroom/sub-%03d_task-mushroom_run-prac_beh' % (int(expInfo['participant']),int(expInfo['participant']))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\mushroom_pilot2\\data_collection\\taskcode\\1_mushroomTask_confidence_practice\\mushroomTask.py',
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
window_dimension = win.size[0] / win.size[1]
window_y = 0.5
window_x = window_y * window_dimension
aperture_size = window_y * 0.5 # size of square where the mushrooms can be shown (in one direction)
mushroom_size = aperture_size * 0.50 # size of mushroom is 1/10th of screen heigth

maxRT = 20
SI_delay = 4

# background color
bg_color=colors.Color((0, 0, 0), space='rgb')
win.color = bg_color
win.mouseVisible = False

# date as empty string
expInfo['date'] = ""  # overwrite actual date to deidentify data

# Create scan directory & all intermediate directories if don't exists (only if connected to storage folder)
#dirName = _thisDir + os.sep + u'../sub-%03d/scans' % (int(expInfo['participant']))
#if not os.path.exists(dirName):
#    os.makedirs(dirName)


# Initialize components for Routine "start_slide"
start_slideClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Welkom bij het Paddenstoelen spel.\n\nDruk op ENTER om te starten.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "import_wave1_data"
import_wave1_dataClock = core.Clock()

# Initialize components for Routine "set_practicePhase"
set_practicePhaseClock = core.Clock()
practice_phase = 0

# Initialize components for Routine "instrPrac"
instrPracClock = core.Clock()
response = keyboard.Keyboard()
Pr1 = ("PADDENSTOELEN SPEL:\n\n\nJe gaat nu eerst te instructies lezen, gevolgd door een aantal oefenrondes.\n\n"
"Je kunt heen en weer gaan door de instructies door middel van de LINKER en RECHTER PIJL op het toetsenbord.\n\n\n"
"Druk nu op de RECHTER pijl om door te gaan naar de volgende instructies.") 

Pr2 = ("In dit spel leef je met een groep mensen voor wie het eten van paddenstoelen erg belangrijk is.\n\n"
"Deze paddenstoelen worden geoogst uit een bos vlak bij jouw dorp. "
"Binnenkort is het tijd om te oogsten, en de leider van de groep heeft jou gevraagd om de oogst in goede banen te leiden.\n\n\n\n\n\n\n\n\n\n")

Pr3 = ("Elke dag gaan er 100 mensen van de groep het bos in om paddenstoelen te plukken.\n"
"Omdat de paddenstoelen erg breekbaar zijn, kan er maar 1 paddenstoel per zak meegenomen worden.\n\n"
"Er zijn 2 soorten paddenstoelen: blauwe en rode.\n"
"Het probleem is dat deze twee soorten paddenstoelen elk hun eigen zak nodig hebben: " 
"Een blauwe paddenstoel kan alleen meegenomen worden in een blauwe zak en een rode paddenstoel kan alleen meegenomen worden in een rode zak.\n\n\n\n\n\n\n\n\n\n\n\n")
 
Pr4 = ("Aan het begin van iedere dag is het jouw taak om te beslissen hoeveel mensen het bos in gaan met een blauwe zak en hoeveel mensen het bos in gaan met een rode zak.\n\n"
"Als er op een bepaalde dag 70 blauwe paddenstoelen en 30 rode paddenstoelen in het bos zijn, dan moet jij aan 70 mensen een blauwe zak en aan 30 mensen een rode zak geven.\n\n"
"Als je te veel mensen een blauwe zak zou geven, dan zouden sommigen van de plukkers die een blauwe zak dragen thuiskomen met een lege zak, " 
"terwijl er rode paddenstoelen in het bos blijven staan omdat er niet genoeg mensen waren met een rode zak. "
"Dat zou betekenen dat je oogst niet optimaal is.")  
 
Pr5 = ("Om een goede schatting te maken over hoeveel paddenstoelen plukkers een blauwe of een rode zak moeten dragen "
"sta je elke ochtend vroeg op om door 5 velden te lopen die om je dorp heen liggen.\n\n"
"In deze velden groeien ook al een paar blauwe en rode paddenstoelen. "
"De paddenstoelen die hier groeien zijn een afspiegeling van wat je op die dag zult vinden in het bos.\n\n"
"Dus, op basis van het aantal blauwe en rode paddenstoelen in de 5 velden kun je beslissen hoeveel paddenstoelen plukkers je een blauwe of een rode zak geeft.\n\n\n\n\n\n\n\n\n\n\n\n")
 
Pr6 = ("Op sommige dagen vind je veel paddenstoelen in de velden, dus heb je veel informatie om je beslissing op te baseren. "
"Op andere dagen vind je echter weinig paddenstoelen in de velden, dus heb je weinig informatie om je beslissing op te baseren.\n\n"
"Hoe meer paddestoelen je in de velden vindt, hoe preciezer ze een afspiegeling zijn van de paddenstoelen in het bos.\n"
"Bijvoorbeeld, als je 10 blauwe en 40 rode paddenstoelen in de velden vindt heb je meer informatie en kun je dus zekerder zijn van je beslissing dan als je 1 blauwe en 4 rode paddenstoelen vindt.")
 
Pr7 = ("Tijdens het spel zie je eerst de paddenstoelen in elk van de 5 velden.\n\n"
"Je beslist dan hoeveel blauwe en rode zakken vandaag moeten worden meegenomen naar het bos. "
"Je geeft je antwoord aan op een balk. Hiervoor gebruik je de pijlen op het toetsenbord.\n\n"
"Je hebt 20 seconden om je antwoord te geven. Dit is ruim genoeg tijd om over je antwoord na te denken. "
"Als je er langer over doet dan 20 seconden krijg je een waarschuwing dat je te laat was.\n\n\n\n\n\n\n\n\n\n\n\n\n")

Pr8 = ("Je wordt dan gevraagd om met de muis aan te geven hoe zeker je was van je beslissing.\n\n\n\n\n\n\n\n\n\n\n")

Pr9 = ("Je speelt meerdere rondes. Elke ronde is een nieuwe dag en alle dagen samen vormen het hele oogstseizoen.\n"
"Je gaat nu eerst een aantal dagen van de oogst oefenen.\n\n" 
"Druk op ENTER om de oefening te starten en gebruik de pijlen om te antwoorden.")




PrDict = { "1": Pr1,
              "2": Pr2, 
              "3": Pr3, 
              "4": Pr4,
              "5": Pr5, 
              "6": Pr6,
              "7": Pr7,
              "8": Pr8,
              "9": Pr9,
}

currentPr = "1"


text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
blue_mushroom = visual.ImageStim(
    win=win,
    name='blue_mushroom', units='height', 
    image='blue_mushroom.png', mask=None,
    ori=350.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
red_mushroom = visual.ImageStim(
    win=win,
    name='red_mushroom', 
    image='red_mushroom.png', mask=None,
    ori=10.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
progress_bar_fixed_2 = visual.Rect(
    win=win, name='progress_bar_fixed_2',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
progress_bar_2 = visual.Rect(
    win=win, name='progress_bar_2',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=-6.0, interpolate=True)
progress_IC_2 = visual.TextStim(win=win, name='progress_IC_2',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
img_forest = visual.ImageStim(
    win=win,
    name='img_forest', 
    image='img_forest.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.6153, 0.338),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
img_bags = visual.ImageStim(
    win=win,
    name='img_bags', 
    image='img_bags.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.6153, 0.338),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
img_fields = visual.ImageStim(
    win=win,
    name='img_fields', 
    image='img_fields.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.6153, 0.338),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
screenshotE1 = visual.ImageStim(
    win=win,
    name='screenshotE1', 
    image='screenshot_E1.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.640, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
screenshotConfidenceRating = visual.ImageStim(
    win=win,
    name='screenshotConfidenceRating', 
    image='screenshot_confidenceRating.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.5396, 0.2604),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)

# Initialize components for Routine "instrPrac2"
instrPrac2Clock = core.Clock()
response_3 = keyboard.Keyboard()
Pr2_1 = ("Goed gedaan!\n\nNadat je je antwoord hebt gegeven, zie je de beslissing van iemand anders die dit spel op een eerder moment gespeeld heeft.\n\n"
"Het aantal blauwe en rode paddenstoelen in het bos was hetzelfde voor deze deelnemer, "
"maar deze deelnemer kwam uit een ander dorp aan de andere kant van het bos. \n"
"Dat betekent dat deze deelnemer in de ochtend door andere velden aan de andere kant van het bos ging lopen, en het aantal blauwe en rode paddenstoelen in deze velden was misschien anders dan in de velden waar jij doorheen liep.\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

Pr2_2 = ("Jij vond bijvoorbeeld 5 paddenstoelen in de velden, terwijl die andere deelnemer 50 paddenstoelen vond. De andere deelnemer had dus meer informatie dan jij om zijn of haar beslissing op te baseren.\n"
"Het kan ook zijn dat de andere deelnemer minder paddenstoelen in de velden vond dan jij en dus minder informatie had.\n\n"
"Je weet echter niet of de andere deelnemer meer of minder paddenstoelen in de velden vond dan jij.")

Pr2_3 = ("Deze andere deelnemer moest tijdens het spelen van het spel ook aangeven hoe zeker hij of zij was van zijn of haar beslissing.\n"
"Dit krijg jij ook te zien.\n\n"
"Nadat je de beslissing en de zekerheid van de ander hebt gezien kun je jouw beslissing nog een keer aanpassen.")

Pr2_4 = ("\n\n\n\n\n\n\n\nJe ziet eerst nogmaals je eigen beslissing en daarboven de beslissing en de zekerheid van de ander op de huidige oogstdag.\n"
"Hun zekerheid kan LAAG, MEDIUM of HOOG zijn.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 
Pr2_5 = ("\n\n\n\n\n\n\n\nDaarna heb je de mogelijkheid om jouw beslissing aan te passen op basis van deze nieuwe informatie.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

Pr2_6 = ("Op elke oogstdag zie je de informatie van steeds weer een andere eerdere deelnemer.\n\n"
"Je gaat nu nog een aantal oefendagen spelen.\n"
"Voor zowel je eerste als je tweede beslissing heb je 20 seconden om te antwoorden.\n\n" 
"Druk op ENTER om de oefening te starten en gebruik de pijlen om te antwoorden.")




Pr2Dict = { "1": Pr2_1,
              "2": Pr2_2, 
              "3": Pr2_3, 
              "4": Pr2_4,
              "5": Pr2_5,
              "6": Pr2_6
}

currentPr2 = "1"


text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
blue_mushroom_6 = visual.ImageStim(
    win=win,
    name='blue_mushroom_6', units='height', 
    image='blue_mushroom.png', mask=None,
    ori=350.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
red_mushroom_6 = visual.ImageStim(
    win=win,
    name='red_mushroom_6', 
    image='red_mushroom.png', mask=None,
    ori=10.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
progress_bar_fixed_5 = visual.Rect(
    win=win, name='progress_bar_fixed_5',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
progress_bar_5 = visual.Rect(
    win=win, name='progress_bar_5',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=-6.0, interpolate=True)
progress_IC_5 = visual.TextStim(win=win, name='progress_IC_5',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
img_otherVillage = visual.ImageStim(
    win=win,
    name='img_otherVillage', 
    image='img_otherVillage.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.885, 0.338),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
screenshot1 = visual.ImageStim(
    win=win,
    name='screenshot1', 
    image='screenshot_SI1.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.643, 0.447),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
screenshot2 = visual.ImageStim(
    win=win,
    name='screenshot2', 
    image='screenshot_SI2.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.643, 0.447),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)

# Initialize components for Routine "Succes"
SuccesClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Succes!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_index = 0


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
how_many_mushrooms_3 = visual.TextStim(win=win, name='how_many_mushrooms_3',
    text='Hoeveel blauwe en rode zakken moeten vandaag worden meegenomen naar het bos?',
    font='Open Sans',
    units='height', pos=(0, 0.4), height=0.032, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
white_rectangle = visual.Rect(
    win=win, name='white_rectangle',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
blue_box = visual.Rect(
    win=win, name='blue_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-5.0, interpolate=True)
red_box = visual.Rect(
    win=win, name='red_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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

# Initialize components for Routine "confidenceRating"
confidenceRatingClock = core.Clock()
confidence_rating = visual.Slider(win=win, name='confidence_rating',
    startValue=None, size=(0.3, 0.05), pos=(0, 0), units=None,
    labels=('laag', 'medium', 'hoog'), ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='White', fillColor='Black', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-1, readOnly=False)
confidence_text = visual.TextStim(win=win, name='confidence_text',
    text='Hoe zeker was je van je beslissing?',
    font='Open Sans',
    pos=(0, 0.07), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_mouse = visual.TextStim(win=win, name='text_mouse',
    text='Gebruik de muis om je antwoord aan te geven',
    font='Open Sans',
    pos=(0, -0.4), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

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
    ori=0.0, pos=(0, 0.02),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
peer_confidence_rating = visual.ImageStim(
    win=win,
    name='peer_confidence_rating', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.29, 0.21),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blue_box_peer = visual.Rect(
    win=win, name='blue_box_peer',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-5.0, interpolate=True)
sliderMarker_peer = visual.Rect(
    win=win, name='sliderMarker_peer',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-6.0, interpolate=True)
showEstimate_peer = visual.TextStim(win=win, name='showEstimate_peer',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
white_rectangle_2 = visual.Rect(
    win=win, name='white_rectangle_2',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
blue_box_E1 = visual.Rect(
    win=win, name='blue_box_E1',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-11.0, interpolate=True)
blue_box_E2 = visual.Rect(
    win=win, name='blue_box_E2',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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

# Initialize components for Routine "instrBonus"
instrBonusClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
event.clearEvents()

Instr1 = ("BONUS:\n\n"
"Aan het eind van het spel krijg je een bonus.\n"
"De hoogte van deze bonus hangt af van hoe goed je het doet tijdens het spel en wordt als volgt berekend:\n\n"
"De computer kiest willekeurig een van de oogstdagen uit en vergelijkt jouw antwoord op die dag met het goede antwoord. "
"De kans dat de computer je eerste of je tweede beslissing van die dag kiest is even groot, dus beide beslissingen zijn even belangrijk.\n\n"
"Als jouw beslissing precies goed was, dan krijg je een bonus van €1,50. Voor elke zak die je ernaast zat wordt er 4 cent afgetrokken.")

Instr2 = ("Bijvoorbeeld, als jij had beslist om 70 van de 100 plukkers een blauwe zak mee te geven, maar er waren 88 blauwe paddenstoelen in het bos, "
"dan krijg je €1,50 - 18 x €0,04 = €0,78.\n\n"
"Je bonus is nooit lager dan €0,00.\n\n"
"Iedere dag kan bepalend zijn voor hoeveel bonus je aan het eind krijgt en iedere dag is dus even belangrijk.")

Instr3 = ("Zoals eerder gezegd bestaat het spel uit meerdere oogstdagen en alle dagen samen vormen het oogstseizoen. "
"In de MRI scanner zul je 3 oogstseizoenen spelen. Na elk seizoen kun je even pauze nemen voordat je verder gaat met het volgende seizoen.\n\n"
"Je gaat nu eerst 1 korter seizoen op de computer spelen om te oefenen. Je kunt nu nog geen bonus verdienen.\n\n"
"Vraag aan de onderzoeker om dit oefenblok te starten.")


InstrDict = { "1": Instr1,
              "2": Instr2,
              "3": Instr3,
}

currentInstr = "1"
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
blue_mushroom_2 = visual.ImageStim(
    win=win,
    name='blue_mushroom_2', 
    image='blue_mushroom.png', mask=None,
    ori=350.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
red_mushroom_2 = visual.ImageStim(
    win=win,
    name='red_mushroom_2', 
    image='red_mushroom.png', mask=None,
    ori=10.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
progress_bar_fixed_3 = visual.Rect(
    win=win, name='progress_bar_fixed_3',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
progress_bar_3 = visual.Rect(
    win=win, name='progress_bar_3',units='height', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=-6.0, interpolate=True)
progress_IC_3 = visual.TextStim(win=win, name='progress_IC_3',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0.48), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "Succes"
SuccesClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Succes!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_index = 0


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
how_many_mushrooms_3 = visual.TextStim(win=win, name='how_many_mushrooms_3',
    text='Hoeveel blauwe en rode zakken moeten vandaag worden meegenomen naar het bos?',
    font='Open Sans',
    units='height', pos=(0, 0.4), height=0.032, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
white_rectangle = visual.Rect(
    win=win, name='white_rectangle',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
blue_box = visual.Rect(
    win=win, name='blue_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-5.0, interpolate=True)
red_box = visual.Rect(
    win=win, name='red_box',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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

# Initialize components for Routine "confidenceRating"
confidenceRatingClock = core.Clock()
confidence_rating = visual.Slider(win=win, name='confidence_rating',
    startValue=None, size=(0.3, 0.05), pos=(0, 0), units=None,
    labels=('laag', 'medium', 'hoog'), ticks=(1, 2, 3), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    color='White', fillColor='Black', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-1, readOnly=False)
confidence_text = visual.TextStim(win=win, name='confidence_text',
    text='Hoe zeker was je van je beslissing?',
    font='Open Sans',
    pos=(0, 0.07), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_mouse = visual.TextStim(win=win, name='text_mouse',
    text='Gebruik de muis om je antwoord aan te geven',
    font='Open Sans',
    pos=(0, -0.4), height=0.032, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

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
    ori=0.0, pos=(0, 0.02),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
peer_confidence_rating = visual.ImageStim(
    win=win,
    name='peer_confidence_rating', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.29, 0.21),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blue_box_peer = visual.Rect(
    win=win, name='blue_box_peer',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-5.0, interpolate=True)
sliderMarker_peer = visual.Rect(
    win=win, name='sliderMarker_peer',units='height', 
    width=(0.008, 0.05)[0], height=(0.008, 0.05)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-6.0, interpolate=True)
showEstimate_peer = visual.TextStim(win=win, name='showEstimate_peer',
    text='',
    font='Open Sans',
    units='height', pos=[0,0], height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
white_rectangle_2 = visual.Rect(
    win=win, name='white_rectangle_2',units='height', 
    width=(1, 0.04)[0], height=(1, 0.04)[1],
    ori=0.0, pos=(0, -0.18),
    lineWidth=0.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
blue_box_E1 = visual.Rect(
    win=win, name='blue_box_E1',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-11.0, interpolate=True)
blue_box_E2 = visual.Rect(
    win=win, name='blue_box_E2',
    width=[0.06, 0.04][0], height=[0.06, 0.04][1],
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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
    ori=0.0, pos=[0,0],
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

# Initialize components for Routine "instructions_end"
instructions_endClock = core.Clock()
bonus_text = visual.TextStim(win=win, name='bonus_text',
    text='Goed gedaan!\n\nDit is het einde van het oefenblok.\n\nVraag nu aan de onderzoeker om je verdere instructies te geven.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
s_to_end = keyboard.Keyboard()
blue_mushroom_4 = visual.ImageStim(
    win=win,
    name='blue_mushroom_4', 
    image='blue_mushroom.png', mask=None,
    ori=350.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
red_mushroom_4 = visual.ImageStim(
    win=win,
    name='red_mushroom_4', 
    image='red_mushroom.png', mask=None,
    ori=10.0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# define trial selection
selected_practice_trials = randchoice([5,6,7], size = 3, replace = False)
selected_trials = randchoice(15, size = 15, replace = False)

# define trial selection
expInfo['trialStructure_file'] = 'trial_structure_prac.csv'

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
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['enter', 'return'], waitRelease=False)
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

# make list of all nTotal, ratio levels and confidence levels
levels_nTotal = [5, 45]
levels_ratio = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
levels_confidence = [1, 2, 3]
all_nTotals = np.repeat(levels_nTotal, len(levels_ratio)*len(levels_confidence))
all_ratios = np.repeat(np.repeat(np.expand_dims(levels_ratio, axis=0), len(levels_nTotal), axis=0), len(levels_confidence))

# create shuffled list of confidence levels for each combination of nTotal and ratio
all_confidences = []
for iConfidenceLists in range(len(levels_nTotal)*len(levels_ratio)):
    shuffle(levels_confidence)
    all_confidences.append(levels_confidence[:])
all_confidences = np.asarray(all_confidences).reshape(-1)

# combine nTotal ratio and confidence into one object
nTotal_ratio_confidence = [];
for iTrials in range(len(all_nTotals)):
    nTotal_ratio_confidence.append({ "nTotal": all_nTotals[iTrials], "ratio": all_ratios[iTrials], "confidence": all_confidences[iTrials] })

# make list for filler rounds: 6 x SI which is closer than 3 percentage points, 3 x SI which is further than 40 percentage points. 
SI_fillers = [3, 3, 3, 3, 3, 3, 40, 40, 40]
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

# set up handler to look after randomisation of conditions etc
practice_phases = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_phases')
thisExp.addLoop(practice_phases)  # add the loop to the experiment
thisPractice_phase = practice_phases.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_phase.rgb)
if thisPractice_phase != None:
    for paramName in thisPractice_phase:
        exec('{} = thisPractice_phase[paramName]'.format(paramName))

for thisPractice_phase in practice_phases:
    currentLoop = practice_phases
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_phase.rgb)
    if thisPractice_phase != None:
        for paramName in thisPractice_phase:
            exec('{} = thisPractice_phase[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "set_practicePhase"-------
    continueRoutine = True
    # update component parameters for each repeat
    practice_phase += 1
    startGame = 0
    # keep track of which components have finished
    set_practicePhaseComponents = []
    for thisComponent in set_practicePhaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    set_practicePhaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "set_practicePhase"-------
    while continueRoutine:
        # get current time
        t = set_practicePhaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=set_practicePhaseClock)
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
        for thisComponent in set_practicePhaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "set_practicePhase"-------
    for thisComponent in set_practicePhaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "set_practicePhase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_instrPrac = data.TrialHandler(nReps=200.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_instrPrac')
    thisExp.addLoop(loop_instrPrac)  # add the loop to the experiment
    thisLoop_instrPrac = loop_instrPrac.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrPrac.rgb)
    if thisLoop_instrPrac != None:
        for paramName in thisLoop_instrPrac:
            exec('{} = thisLoop_instrPrac[paramName]'.format(paramName))
    
    for thisLoop_instrPrac in loop_instrPrac:
        currentLoop = loop_instrPrac
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrPrac.rgb)
        if thisLoop_instrPrac != None:
            for paramName in thisLoop_instrPrac:
                exec('{} = thisLoop_instrPrac[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instrPrac"-------
        continueRoutine = True
        # update component parameters for each repeat
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # only run if phase is 1
        if practice_phase is not 1:
            loop_instrPrac.finished = True
            continueRoutine = False
        
        event.clearEvents()
        
        progress_bar_size = (window_x*2)/18 * int(currentPr)
        progress_bar_pos = (-window_x) + (window_x*2)/18 * int(currentPr) / 2
        progress_text = "Instructies: " + currentPr + "/18"
        
        text.setText(PrDict[currentPr])
        blue_mushroom.setPos((window_x-0.3, -0.4))
        red_mushroom.setPos((window_x-0.2, -0.4))
        progress_bar_fixed_2.setPos((0, 0.48))
        progress_bar_fixed_2.setSize((window_x*2, 0.03))
        progress_bar_2.setPos((progress_bar_pos, 0.48))
        progress_bar_2.setSize((progress_bar_size, 0.03))
        progress_IC_2.setText(progress_text
)
        # keep track of which components have finished
        instrPracComponents = [response, text, blue_mushroom, red_mushroom, progress_bar_fixed_2, progress_bar_2, progress_IC_2, img_forest, img_bags, img_fields, screenshotE1, screenshotConfidenceRating]
        for thisComponent in instrPracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instrPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instrPrac"-------
        while continueRoutine:
            # get current time
            t = instrPracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instrPracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['right', 'left', 'return', 'num_enter'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *blue_mushroom* updates
            if blue_mushroom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blue_mushroom.frameNStart = frameN  # exact frame index
                blue_mushroom.tStart = t  # local t and not account for scr refresh
                blue_mushroom.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_mushroom, 'tStartRefresh')  # time at next scr refresh
                blue_mushroom.setAutoDraw(True)
            
            # *red_mushroom* updates
            if red_mushroom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_mushroom.frameNStart = frameN  # exact frame index
                red_mushroom.tStart = t  # local t and not account for scr refresh
                red_mushroom.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_mushroom, 'tStartRefresh')  # time at next scr refresh
                red_mushroom.setAutoDraw(True)
            
            # *progress_bar_fixed_2* updates
            if progress_bar_fixed_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_fixed_2.frameNStart = frameN  # exact frame index
                progress_bar_fixed_2.tStart = t  # local t and not account for scr refresh
                progress_bar_fixed_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_fixed_2, 'tStartRefresh')  # time at next scr refresh
                progress_bar_fixed_2.setAutoDraw(True)
            
            # *progress_bar_2* updates
            if progress_bar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_2.frameNStart = frameN  # exact frame index
                progress_bar_2.tStart = t  # local t and not account for scr refresh
                progress_bar_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_2, 'tStartRefresh')  # time at next scr refresh
                progress_bar_2.setAutoDraw(True)
            
            # *progress_IC_2* updates
            if progress_IC_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_IC_2.frameNStart = frameN  # exact frame index
                progress_IC_2.tStart = t  # local t and not account for scr refresh
                progress_IC_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_IC_2, 'tStartRefresh')  # time at next scr refresh
                progress_IC_2.setAutoDraw(True)
            
            # *img_forest* updates
            if img_forest.status == NOT_STARTED and currentPr == "2":
                # keep track of start time/frame for later
                img_forest.frameNStart = frameN  # exact frame index
                img_forest.tStart = t  # local t and not account for scr refresh
                img_forest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_forest, 'tStartRefresh')  # time at next scr refresh
                img_forest.setAutoDraw(True)
            
            # *img_bags* updates
            if img_bags.status == NOT_STARTED and currentPr == "3":
                # keep track of start time/frame for later
                img_bags.frameNStart = frameN  # exact frame index
                img_bags.tStart = t  # local t and not account for scr refresh
                img_bags.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_bags, 'tStartRefresh')  # time at next scr refresh
                img_bags.setAutoDraw(True)
            
            # *img_fields* updates
            if img_fields.status == NOT_STARTED and currentPr == "5":
                # keep track of start time/frame for later
                img_fields.frameNStart = frameN  # exact frame index
                img_fields.tStart = t  # local t and not account for scr refresh
                img_fields.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_fields, 'tStartRefresh')  # time at next scr refresh
                img_fields.setAutoDraw(True)
            
            # *screenshotE1* updates
            if screenshotE1.status == NOT_STARTED and currentPr == "7":
                # keep track of start time/frame for later
                screenshotE1.frameNStart = frameN  # exact frame index
                screenshotE1.tStart = t  # local t and not account for scr refresh
                screenshotE1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screenshotE1, 'tStartRefresh')  # time at next scr refresh
                screenshotE1.setAutoDraw(True)
            
            # *screenshotConfidenceRating* updates
            if screenshotConfidenceRating.status == NOT_STARTED and currentPr == "8":
                # keep track of start time/frame for later
                screenshotConfidenceRating.frameNStart = frameN  # exact frame index
                screenshotConfidenceRating.tStart = t  # local t and not account for scr refresh
                screenshotConfidenceRating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screenshotConfidenceRating, 'tStartRefresh')  # time at next scr refresh
                screenshotConfidenceRating.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instrPracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instrPrac"-------
        for thisComponent in instrPracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #win.getMovieFrame()
        #name = "instrPractice_{age}.png".format(age = currentPr)
        #win.saveMovieFrames(name) 
        
        if (response.keys == "return" or response.keys == "num_enter") and int(currentPr) == 9:
            currentPr = int(currentPr) + 1
        elif response.keys == "right" and int(currentPr) == 9:
            currentPr = int(currentPr)
        elif response.keys == "right" and int(currentPr) != 9:
            currentPr = int(currentPr) + 1
        elif response.keys == "left":
            currentPr = int(currentPr) - 1
        
        if currentPr == 0:
            currentPr = 1  # can't go lower than
        elif currentPr == 10:
            loop_instrPrac.finished=True
            currentPr = 1 # otherwise, currentPr will give an error on the next round, because it is out-of-range.
        
        currentPr = str(currentPr)
        
        # the Routine "instrPrac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 200.0 repeats of 'loop_instrPrac'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_instrPrac2 = data.TrialHandler(nReps=200.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_instrPrac2')
    thisExp.addLoop(loop_instrPrac2)  # add the loop to the experiment
    thisLoop_instrPrac2 = loop_instrPrac2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrPrac2.rgb)
    if thisLoop_instrPrac2 != None:
        for paramName in thisLoop_instrPrac2:
            exec('{} = thisLoop_instrPrac2[paramName]'.format(paramName))
    
    for thisLoop_instrPrac2 in loop_instrPrac2:
        currentLoop = loop_instrPrac2
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrPrac2.rgb)
        if thisLoop_instrPrac2 != None:
            for paramName in thisLoop_instrPrac2:
                exec('{} = thisLoop_instrPrac2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instrPrac2"-------
        continueRoutine = True
        # update component parameters for each repeat
        response_3.keys = []
        response_3.rt = []
        _response_3_allKeys = []
        # only run if phase is 2
        if practice_phase is not 2:
            loop_instrPrac2.finished = True
            continueRoutine = False
        
        event.clearEvents()
        
        progress_bar_size = (window_x*2)/18 * (int(currentPr2) + 9)
        progress_bar_pos = (-window_x) + (window_x*2)/18 * (int(currentPr2) + 9) / 2
        progress_text = "Instructies: " + str(int(currentPr2)+9) + "/18"
        
        
        
        text_7.setText(Pr2Dict[currentPr2])
        blue_mushroom_6.setPos((window_x-0.3, -0.4))
        red_mushroom_6.setPos((window_x-0.2, -0.4))
        progress_bar_fixed_5.setPos((0, 0.48))
        progress_bar_fixed_5.setSize((window_x*2, 0.03))
        progress_bar_5.setPos((progress_bar_pos, 0.48))
        progress_bar_5.setSize((progress_bar_size, 0.03))
        progress_IC_5.setText(progress_text
)
        # keep track of which components have finished
        instrPrac2Components = [response_3, text_7, blue_mushroom_6, red_mushroom_6, progress_bar_fixed_5, progress_bar_5, progress_IC_5, img_otherVillage, screenshot1, screenshot2]
        for thisComponent in instrPrac2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instrPrac2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instrPrac2"-------
        while continueRoutine:
            # get current time
            t = instrPrac2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instrPrac2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_3* updates
            waitOnFlip = False
            if response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_3.frameNStart = frameN  # exact frame index
                response_3.tStart = t  # local t and not account for scr refresh
                response_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_3, 'tStartRefresh')  # time at next scr refresh
                response_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response_3.status == STARTED and not waitOnFlip:
                theseKeys = response_3.getKeys(keyList=['right', 'left', 'return', 'num_enter'], waitRelease=False)
                _response_3_allKeys.extend(theseKeys)
                if len(_response_3_allKeys):
                    response_3.keys = _response_3_allKeys[-1].name  # just the last key pressed
                    response_3.rt = _response_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            
            # *blue_mushroom_6* updates
            if blue_mushroom_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blue_mushroom_6.frameNStart = frameN  # exact frame index
                blue_mushroom_6.tStart = t  # local t and not account for scr refresh
                blue_mushroom_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_mushroom_6, 'tStartRefresh')  # time at next scr refresh
                blue_mushroom_6.setAutoDraw(True)
            
            # *red_mushroom_6* updates
            if red_mushroom_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_mushroom_6.frameNStart = frameN  # exact frame index
                red_mushroom_6.tStart = t  # local t and not account for scr refresh
                red_mushroom_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_mushroom_6, 'tStartRefresh')  # time at next scr refresh
                red_mushroom_6.setAutoDraw(True)
            
            # *progress_bar_fixed_5* updates
            if progress_bar_fixed_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_fixed_5.frameNStart = frameN  # exact frame index
                progress_bar_fixed_5.tStart = t  # local t and not account for scr refresh
                progress_bar_fixed_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_fixed_5, 'tStartRefresh')  # time at next scr refresh
                progress_bar_fixed_5.setAutoDraw(True)
            
            # *progress_bar_5* updates
            if progress_bar_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_5.frameNStart = frameN  # exact frame index
                progress_bar_5.tStart = t  # local t and not account for scr refresh
                progress_bar_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_5, 'tStartRefresh')  # time at next scr refresh
                progress_bar_5.setAutoDraw(True)
            
            # *progress_IC_5* updates
            if progress_IC_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_IC_5.frameNStart = frameN  # exact frame index
                progress_IC_5.tStart = t  # local t and not account for scr refresh
                progress_IC_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_IC_5, 'tStartRefresh')  # time at next scr refresh
                progress_IC_5.setAutoDraw(True)
            
            # *img_otherVillage* updates
            if img_otherVillage.status == NOT_STARTED and currentPr2 == "1":
                # keep track of start time/frame for later
                img_otherVillage.frameNStart = frameN  # exact frame index
                img_otherVillage.tStart = t  # local t and not account for scr refresh
                img_otherVillage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_otherVillage, 'tStartRefresh')  # time at next scr refresh
                img_otherVillage.setAutoDraw(True)
            
            # *screenshot1* updates
            if screenshot1.status == NOT_STARTED and currentPr2 == "4":
                # keep track of start time/frame for later
                screenshot1.frameNStart = frameN  # exact frame index
                screenshot1.tStart = t  # local t and not account for scr refresh
                screenshot1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screenshot1, 'tStartRefresh')  # time at next scr refresh
                screenshot1.setAutoDraw(True)
            
            # *screenshot2* updates
            if screenshot2.status == NOT_STARTED and currentPr2 == "5":
                # keep track of start time/frame for later
                screenshot2.frameNStart = frameN  # exact frame index
                screenshot2.tStart = t  # local t and not account for scr refresh
                screenshot2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(screenshot2, 'tStartRefresh')  # time at next scr refresh
                screenshot2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instrPrac2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instrPrac2"-------
        for thisComponent in instrPrac2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #win.getMovieFrame()
        #name = "instrPractice_{age}.png".format(age = currentPr)
        #win.saveMovieFrames(name) 
        
        if (response_3.keys == "return" or response_3.keys == "num_enter") and int(currentPr2) == 6:
            currentPr2 = int(currentPr2) + 1
        elif response_3.keys == "right" and int(currentPr2) == 6:
            currentPr2 = int(currentPr2)
        elif response_3.keys == "right" and int(currentPr2) != 6:
            currentPr2 = int(currentPr2) + 1
        elif response_3.keys == "left":
            currentPr2 = int(currentPr2) - 1
        
        if currentPr2 == 0:
            currentPr2 = 1  # can't go lower than
        elif currentPr2 == 7:
            loop_instrPrac2.finished=True
        
        currentPr2 = str(currentPr2)
        # the Routine "instrPrac2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 200.0 repeats of 'loop_instrPrac2'
    
    
    # ------Prepare to start Routine "Succes"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    SuccesComponents = [text_6]
    for thisComponent in SuccesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SuccesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Succes"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = SuccesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SuccesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SuccesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Succes"-------
    for thisComponent in SuccesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    loop_prTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trial_structure_prac.csv', selection=selected_practice_trials),
        seed=None, name='loop_prTrials')
    thisExp.addLoop(loop_prTrials)  # add the loop to the experiment
    thisLoop_prTrial = loop_prTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_prTrial.rgb)
    if thisLoop_prTrial != None:
        for paramName in thisLoop_prTrial:
            exec('{} = thisLoop_prTrial[paramName]'.format(paramName))
    
    for thisLoop_prTrial in loop_prTrials:
        currentLoop = loop_prTrials
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_prTrial.rgb)
        if thisLoop_prTrial != None:
            for paramName in thisLoop_prTrial:
                exec('{} = thisLoop_prTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "setupSamples"-------
        continueRoutine = True
        # update component parameters for each repeat
        # retrieved from file
        if startGame == 0:
            nTotal = thisLoop_prTrial['nTotal']
            true_ratio = thisLoop_prTrial['trueRatio']
            given_ratio = thisLoop_prTrial['trueRatio']
            filler_trial = thisLoop_prTrial['fillerTrial']
        elif startGame == 1:
            nTotal = thisLoop_trial['nTotal']
            true_ratio = thisLoop_trial['trueRatio']
            given_ratio = thisLoop_trial['trueRatio']
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
        # the Routine "setupSamples" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "crossHair"-------
        continueRoutine = True
        # update component parameters for each repeat
        crosshair_ITI = round(random.random() * (2.0 - 1.5) + 1.5, 1)
        
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
        #win.getMovieFrame()
        #win.saveMovieFrames('crosshair.png') 
        
        
        # the Routine "crossHair" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_prSamples = data.TrialHandler(nReps=5.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='loop_prSamples')
        thisExp.addLoop(loop_prSamples)  # add the loop to the experiment
        thisLoop_prSample = loop_prSamples.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_prSample.rgb)
        if thisLoop_prSample != None:
            for paramName in thisLoop_prSample:
                exec('{} = thisLoop_prSample[paramName]'.format(paramName))
        
        for thisLoop_prSample in loop_prSamples:
            currentLoop = loop_prSamples
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_prSample.rgb)
            if thisLoop_prSample != None:
                for paramName in thisLoop_prSample:
                    exec('{} = thisLoop_prSample[paramName]'.format(paramName))
            
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
            
            #win.getMovieFrame()
            #name = "sample_{age}.png".format(age = sample_index)
            #win.saveMovieFrames(name) 
            
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
        # completed 5.0 repeats of 'loop_prSamples'
        
        
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
        if startGame == 1:
            howToRespond = "" 
        else: 
            howToRespond = "Gebruik de pijlen om je beslissing aan te geven\nen druk op ENTER om je beslissing op te slaan."
        
        #pic_done = 0
        
        # keep track of which components have finished
        firstEstimationComponents = [how_many_mushrooms_3, white_rectangle, blue_box, showEstimate, sliderMarker, red_box, showEstimate_red, text_8]
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
            #if pic_done == 0:
            #    win.getMovieFrame()
            #    win.saveMovieFrames('estimation1.png') 
            #    pic_done = 1
            
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
            keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
            keys_released = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = True, clear=False)
            
            
            # everytime a new button is pressed in, I reset the acceleration with which the slider marker moves
            if len(keys) > nKeys: # new key pressed in
                nKeys = len(keys) # update nKeys
                tMove_start = t # reset speed reference point to start of new button press
                if startGame == 1:
                    howToRespond = "Druk op ENTER om op te slaan" # show pp can press ENTER as soon as there is a rating
            # check for sticky key: reset speed reference point and keyboard buffer at least every 2 secs
            if (t - tMove_start) > 2:
                kb.clearEvents() # if sticky key, reset keyboard buffer
                nKeys = 0
                tMove_start = t # reset speed reference point 
            
            # sticky key detection: if the same button with duration None is in the list of all key presses more than once
            #if len(keys):
            #    key = keys[len(keys)-1].name
            #    if key == 'o':
            #        for x in keys:
            #            print("fout all: ", x.name, x.duration)
            #        for y in keys_released: 
            #            print("fout released: ", y.name, y.duration)
            #        stickyDetection = []
            #        for x in keys: 
            #            if x.duration is None:
            #                stickyDetection.append(x.name)
            #                contains_duplicates = len(stickyDetection) != len(set(stickyDetection)) # a set only keeps unique elements
            #                if contains_duplicates:
            #                    print("should be empty")
            #                    kb.clearEvents()
            #                    tMove_start = t
            #                    keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
            #                    for x in keys:
            #                        print("should be empty: ", x.name, x.duration)
            
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
                    if key == 'left':
                        tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                        submit = 1
                    elif key =='right': 
                        tempRating += math.exp(speed*1.5)-1
                        submit = 1
                    elif (key == 'return' or key == 'num_enter') and submit == 1:
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
            
            
            
            
            
            # *how_many_mushrooms_3* updates
            if how_many_mushrooms_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                how_many_mushrooms_3.frameNStart = frameN  # exact frame index
                how_many_mushrooms_3.tStart = t  # local t and not account for scr refresh
                how_many_mushrooms_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(how_many_mushrooms_3, 'tStartRefresh')  # time at next scr refresh
                how_many_mushrooms_3.setAutoDraw(True)
            
            # *white_rectangle* updates
            if white_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                white_rectangle.frameNStart = frameN  # exact frame index
                white_rectangle.tStart = t  # local t and not account for scr refresh
                white_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(white_rectangle, 'tStartRefresh')  # time at next scr refresh
                white_rectangle.setAutoDraw(True)
            
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
        #win.getMovieFrame()
        #win.saveMovieFrames('response.png') 
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
        if startGame == 1: 
            loop_trials.addData('cross_hair.ITI', crosshair_ITI)
            loop_trials.addData('seen_ratio', seen_ratio)
            loop_trials.addData('nMushrooms', " ".join(map(str, nObservations)))
            loop_trials.addData('nBlue', " ".join(map(str, blue)))
            loop_trials.addData('nRed', " ".join(map(str, red)))
            loop_trials.addData('estimation1.rating', estimate1)
            loop_trials.addData('estimation1.rt', estimate1_rt)
            if tooLate == 0:
                list_deviance.append(abs_deviance)
        
        
        win.mouseVisible = False
        
        
        # the Routine "firstEstimation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "confidenceRating"-------
        continueRoutine = True
        # update component parameters for each repeat
        # do not run if participant was too late at first estimation
        if tooLate == 1:
            continueRoutine = False
        
        # initiate mouse
        mouse = event.Mouse(win=win)
        win.mouseVisible = True
        mouse.setPos(newPos=(0,-0.3))
        
        #pic_done = 0
        confidence_rating.reset()
        # keep track of which components have finished
        confidenceRatingComponents = [confidence_rating, confidence_text, text_mouse]
        for thisComponent in confidenceRatingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        confidenceRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "confidenceRating"-------
        while continueRoutine:
            # get current time
            t = confidenceRatingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confidenceRatingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #if t > 0.5 and pic_done == 0:
            #    win.getMovieFrame()
            #    win.saveMovieFrames('confidenceRating.png') 
            #    pic_done = 1
            
            # *confidence_rating* updates
            if confidence_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_rating.frameNStart = frameN  # exact frame index
                confidence_rating.tStart = t  # local t and not account for scr refresh
                confidence_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_rating, 'tStartRefresh')  # time at next scr refresh
                confidence_rating.setAutoDraw(True)
            
            # Check confidence_rating for response to end routine
            if confidence_rating.getRating() is not None and confidence_rating.status == STARTED:
                continueRoutine = False
            
            # *confidence_text* updates
            if confidence_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_text.frameNStart = frameN  # exact frame index
                confidence_text.tStart = t  # local t and not account for scr refresh
                confidence_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_text, 'tStartRefresh')  # time at next scr refresh
                confidence_text.setAutoDraw(True)
            
            # *text_mouse* updates
            if text_mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_mouse.frameNStart = frameN  # exact frame index
                text_mouse.tStart = t  # local t and not account for scr refresh
                text_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_mouse, 'tStartRefresh')  # time at next scr refresh
                text_mouse.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confidenceRatingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "confidenceRating"-------
        for thisComponent in confidenceRatingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if startGame == 1 and tooLate == 0: 
            loop_trials.addData('confidence_own.rating', confidence_rating.getRating())
            loop_trials.addData('confidence_own.rt', t)
        win.mouseVisible = False
        core.wait(0.5)
        # the Routine "confidenceRating" was not non-slip safe, so reset the non-slip timer
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
        
        # retrieve confidence level to use in this trial, based on current nTotal and ratio and filer wave1 data
        if startGame == 0:
            confidence_level = trial_index + 1
            filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level] # filter wave1 data / social information based on current ratio and confidence level
        elif filler_trial == 0:
            confidence_level = [row for row in nTotal_ratio_confidence if row['nTotal']==nTotal and row['ratio']==true_ratio][0]['confidence'] # pick first element with specific ratio and nTotal and return confidence level
            nTotal_ratio_confidence = [row for row in nTotal_ratio_confidence if not (row['nTotal']==nTotal and row['ratio']==true_ratio and row['confidence']==confidence_level)]  # remove element so it wont be used another time
            filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level] # filter wave1 data / social information based on current ratio and confidence level
        elif filler_trial == 1:
            filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio]  # filter wave1 data / social information based on current ratio 
            if true_ratio == 0 or true_ratio == 1:
                confidence_level = 3 # makes more sense if peer is very confidence in those obvious trials
                filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level]
        
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
                confidence_level = 1
                filtered_SI2 = [row for row in filtered_SI if (row['estimate'] < estimate1 - 40 or row['estimate'] > estimate1 + 40) and row['confidence'] == confidence_level]
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
        
        
        # if no suitable SI could be found, just include all SI
        if len(filtered_SI2) == 0:
            filtered_SI2 = filtered_SI
        
        # now randomly choose a peer estimate from filtered list
        random_index = int(random.randint(0,len(filtered_SI2),1))
        peer_estimate = filtered_SI2[random_index]['estimate']
        confidence_level = filtered_SI2[random_index]['confidence']
        
        # define image to show about peers confidence 
        if confidence_level == 1:
            peers_confidence_image = "low_peerConfidence.png"
        elif confidence_level == 2:
            peers_confidence_image = "medium_peerConfidence.png"
        elif confidence_level == 3:
            peers_confidence_image = "high_peerConfidence.png"
        
        # parameters for visual peer estimate information 
        markerPosition_peer = (peer_estimate - 50) / 100
        
        # do not run if in first practice phase
        if practice_phase is not 2:
            continueRoutine = False
        
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
        
        # set alignment of text
        estimateOther.alignText='left'
        estimateSelf.alignText='left'
        
        # text about how to submit
        if startGame == 1:
            howToRespond = "" 
        else: 
            howToRespond = "Gebruik de pijlen om je beslissing aan te geven\nen druk op ENTER om je beslissing op te slaan."
        
        #pic_done = 0
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
        SIComponents = [how_many_mushrooms_2, white_rectangle_peer, peer_confidence_rating, blue_box_peer, sliderMarker_peer, showEstimate_peer, white_rectangle_2, blue_box_E1, showEstimate_E1, sliderMarker_E1, blue_box_E2, showEstimate_E2, sliderMarker_E2, enterToRespond, red_box_peer, showEstimate_red_peer, red_box_E1, showEstimate_red_E1, red_box_E2, showEstimate_red_E2, estimateOther, estimateSelf]
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
            #if t > 1 and t < SI_delay and pic_done == 0 and confidence_level == 2:
            #    win.getMovieFrame()
            #    win.saveMovieFrames('estimation2_1.png') 
            #    pic_done = 1
            #if t > SI_delay and pic_done == 1 and confidence_level == 2:
            #    win.getMovieFrame()
            #    win.saveMovieFrames('estimation2_2.png') 
            #    pic_done = 2
            
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
            
                # move slider colors along with response
                keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
                keys_released = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = True, clear=False)
            
                # everytime a new button is pressed in, I reset the speed with which the slider marker moves
                if len(keys) > nKeys: # new key pressed in
                    nKeys = len(keys) # update nKeys
                    tMove_start = t # reset speed reference point to start of new button press
                    if startGame == 1:
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
                        if key == 'left':
                            tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                            submit = 1
                        elif key =='right': 
                            tempRating += math.exp(speed*1.5)-1
                            submit = 1
                        elif (key == 'return' or key == 'num_enter') and submit == 1:
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
            
            # *white_rectangle_2* updates
            if white_rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                white_rectangle_2.frameNStart = frameN  # exact frame index
                white_rectangle_2.tStart = t  # local t and not account for scr refresh
                white_rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(white_rectangle_2, 'tStartRefresh')  # time at next scr refresh
                white_rectangle_2.setAutoDraw(True)
            
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
        #win.getMovieFrame()
        #win.saveMovieFrames('response.png') 
        kb.clearEvents()
        
        if startGame == 1: 
            estimate2 = int(rating)
            # performance
            if tooLate == 0:
                estimate2_rt = rt-SI_delay
                deviance = estimate2 - true_ratio*100
                abs_deviance = abs(deviance)
            elif tooLate == 1:
                estimate2_rt = []
        
            # only save data during actual task, not practice
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
                expInfo['bonus'] = bonus
        
        
        trial_index += 1
        
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
    # completed 1.0 repeats of 'loop_prTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_instrBonus = data.TrialHandler(nReps=200.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_instrBonus')
    thisExp.addLoop(loop_instrBonus)  # add the loop to the experiment
    thisLoop_instrBonu = loop_instrBonus.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrBonu.rgb)
    if thisLoop_instrBonu != None:
        for paramName in thisLoop_instrBonu:
            exec('{} = thisLoop_instrBonu[paramName]'.format(paramName))
    
    for thisLoop_instrBonu in loop_instrBonus:
        currentLoop = loop_instrBonus
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_instrBonu.rgb)
        if thisLoop_instrBonu != None:
            for paramName in thisLoop_instrBonu:
                exec('{} = thisLoop_instrBonu[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instrBonus"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # only run if phase is 2
        if practice_phase is not 2:
            loop_instrBonus.finished = True
            continueRoutine = False
        
        progress_bar_size = (window_x*2)/18 * (int(currentInstr) + 15)
        progress_bar_pos = (-window_x) + (window_x*2)/18 * (int(currentInstr) + 15) / 2
        progress_text = "Instructions: " + str(int(currentInstr)+15) + "/18"
        
        text_3.setText(InstrDict[currentInstr])
        blue_mushroom_2.setPos((window_x-0.3, -0.4))
        red_mushroom_2.setPos((window_x-0.2, -0.4))
        progress_bar_fixed_3.setPos((0, 0.48))
        progress_bar_fixed_3.setSize((window_x*2, 0.03))
        progress_bar_3.setPos((progress_bar_pos, 0.48))
        progress_bar_3.setSize((progress_bar_size, 0.03))
        progress_IC_3.setText(progress_text
)
        # keep track of which components have finished
        instrBonusComponents = [key_resp_2, text_3, blue_mushroom_2, red_mushroom_2, progress_bar_fixed_3, progress_bar_3, progress_IC_3]
        for thisComponent in instrBonusComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instrBonusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instrBonus"-------
        while continueRoutine:
            # get current time
            t = instrBonusClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instrBonusClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['right', 'left', 's'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *blue_mushroom_2* updates
            if blue_mushroom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blue_mushroom_2.frameNStart = frameN  # exact frame index
                blue_mushroom_2.tStart = t  # local t and not account for scr refresh
                blue_mushroom_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_mushroom_2, 'tStartRefresh')  # time at next scr refresh
                blue_mushroom_2.setAutoDraw(True)
            
            # *red_mushroom_2* updates
            if red_mushroom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_mushroom_2.frameNStart = frameN  # exact frame index
                red_mushroom_2.tStart = t  # local t and not account for scr refresh
                red_mushroom_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_mushroom_2, 'tStartRefresh')  # time at next scr refresh
                red_mushroom_2.setAutoDraw(True)
            
            # *progress_bar_fixed_3* updates
            if progress_bar_fixed_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_fixed_3.frameNStart = frameN  # exact frame index
                progress_bar_fixed_3.tStart = t  # local t and not account for scr refresh
                progress_bar_fixed_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_fixed_3, 'tStartRefresh')  # time at next scr refresh
                progress_bar_fixed_3.setAutoDraw(True)
            
            # *progress_bar_3* updates
            if progress_bar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_3.frameNStart = frameN  # exact frame index
                progress_bar_3.tStart = t  # local t and not account for scr refresh
                progress_bar_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_3, 'tStartRefresh')  # time at next scr refresh
                progress_bar_3.setAutoDraw(True)
            
            # *progress_IC_3* updates
            if progress_IC_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                progress_IC_3.frameNStart = frameN  # exact frame index
                progress_IC_3.tStart = t  # local t and not account for scr refresh
                progress_IC_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_IC_3, 'tStartRefresh')  # time at next scr refresh
                progress_IC_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instrBonusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instrBonus"-------
        for thisComponent in instrBonusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #win.getMovieFrame()
        #name = "instructions_{age}.png".format(age = currentInstr)
        #win.saveMovieFrames(name) 
        
        if (key_resp_2.keys == "s") and int(currentInstr) == 3:
            currentInstr = int(currentInstr) + 1
        elif key_resp_2.keys == "right" and int(currentInstr) == 3:
            currentInstr = int(currentInstr)
        elif key_resp_2.keys == "right" and int(currentInstr) != 3:
            currentInstr = int(currentInstr) + 1
        elif key_resp_2.keys == "left":
            currentInstr = int(currentInstr) - 1
        
        if currentInstr == 0:
            currentInstr = 1  # can't go lower than
        elif currentInstr == 4:
            loop_instrBonus.finished=True
        
        currentInstr = str(currentInstr)
        
        list_deviance = []
        trial_index = 0
        startGame = 1
        
        # the Routine "instrBonus" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 200.0 repeats of 'loop_instrBonus'
    
# completed 2.0 repeats of 'practice_phases'


# ------Prepare to start Routine "Succes"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
SuccesComponents = [text_6]
for thisComponent in SuccesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SuccesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Succes"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = SuccesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SuccesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SuccesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Succes"-------
for thisComponent in SuccesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_structure_prac.csv', selection='selected_trials'),
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
    if startGame == 0:
        nTotal = thisLoop_prTrial['nTotal']
        true_ratio = thisLoop_prTrial['trueRatio']
        given_ratio = thisLoop_prTrial['trueRatio']
        filler_trial = thisLoop_prTrial['fillerTrial']
    elif startGame == 1:
        nTotal = thisLoop_trial['nTotal']
        true_ratio = thisLoop_trial['trueRatio']
        given_ratio = thisLoop_trial['trueRatio']
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
    # the Routine "setupSamples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crossHair"-------
    continueRoutine = True
    # update component parameters for each repeat
    crosshair_ITI = round(random.random() * (2.0 - 1.5) + 1.5, 1)
    
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
    #win.getMovieFrame()
    #win.saveMovieFrames('crosshair.png') 
    
    
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
        
        #win.getMovieFrame()
        #name = "sample_{age}.png".format(age = sample_index)
        #win.saveMovieFrames(name) 
        
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
    if startGame == 1:
        howToRespond = "" 
    else: 
        howToRespond = "Gebruik de pijlen om je beslissing aan te geven\nen druk op ENTER om je beslissing op te slaan."
    
    #pic_done = 0
    
    # keep track of which components have finished
    firstEstimationComponents = [how_many_mushrooms_3, white_rectangle, blue_box, showEstimate, sliderMarker, red_box, showEstimate_red, text_8]
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
        #if pic_done == 0:
        #    win.getMovieFrame()
        #    win.saveMovieFrames('estimation1.png') 
        #    pic_done = 1
        
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
        keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
        keys_released = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = True, clear=False)
        
        
        # everytime a new button is pressed in, I reset the acceleration with which the slider marker moves
        if len(keys) > nKeys: # new key pressed in
            nKeys = len(keys) # update nKeys
            tMove_start = t # reset speed reference point to start of new button press
            if startGame == 1:
                howToRespond = "Druk op ENTER om op te slaan" # show pp can press ENTER as soon as there is a rating
        # check for sticky key: reset speed reference point and keyboard buffer at least every 2 secs
        if (t - tMove_start) > 2:
            kb.clearEvents() # if sticky key, reset keyboard buffer
            nKeys = 0
            tMove_start = t # reset speed reference point 
        
        # sticky key detection: if the same button with duration None is in the list of all key presses more than once
        #if len(keys):
        #    key = keys[len(keys)-1].name
        #    if key == 'o':
        #        for x in keys:
        #            print("fout all: ", x.name, x.duration)
        #        for y in keys_released: 
        #            print("fout released: ", y.name, y.duration)
        #        stickyDetection = []
        #        for x in keys: 
        #            if x.duration is None:
        #                stickyDetection.append(x.name)
        #                contains_duplicates = len(stickyDetection) != len(set(stickyDetection)) # a set only keeps unique elements
        #                if contains_duplicates:
        #                    print("should be empty")
        #                    kb.clearEvents()
        #                    tMove_start = t
        #                    keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
        #                    for x in keys:
        #                        print("should be empty: ", x.name, x.duration)
        
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
                if key == 'left':
                    tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                    submit = 1
                elif key =='right': 
                    tempRating += math.exp(speed*1.5)-1
                    submit = 1
                elif (key == 'return' or key == 'num_enter') and submit == 1:
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
        
        
        
        
        
        # *how_many_mushrooms_3* updates
        if how_many_mushrooms_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            how_many_mushrooms_3.frameNStart = frameN  # exact frame index
            how_many_mushrooms_3.tStart = t  # local t and not account for scr refresh
            how_many_mushrooms_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(how_many_mushrooms_3, 'tStartRefresh')  # time at next scr refresh
            how_many_mushrooms_3.setAutoDraw(True)
        
        # *white_rectangle* updates
        if white_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_rectangle.frameNStart = frameN  # exact frame index
            white_rectangle.tStart = t  # local t and not account for scr refresh
            white_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_rectangle, 'tStartRefresh')  # time at next scr refresh
            white_rectangle.setAutoDraw(True)
        
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
    #win.getMovieFrame()
    #win.saveMovieFrames('response.png') 
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
    if startGame == 1: 
        loop_trials.addData('cross_hair.ITI', crosshair_ITI)
        loop_trials.addData('seen_ratio', seen_ratio)
        loop_trials.addData('nMushrooms', " ".join(map(str, nObservations)))
        loop_trials.addData('nBlue', " ".join(map(str, blue)))
        loop_trials.addData('nRed', " ".join(map(str, red)))
        loop_trials.addData('estimation1.rating', estimate1)
        loop_trials.addData('estimation1.rt', estimate1_rt)
        if tooLate == 0:
            list_deviance.append(abs_deviance)
    
    
    win.mouseVisible = False
    
    
    # the Routine "firstEstimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "confidenceRating"-------
    continueRoutine = True
    # update component parameters for each repeat
    # do not run if participant was too late at first estimation
    if tooLate == 1:
        continueRoutine = False
    
    # initiate mouse
    mouse = event.Mouse(win=win)
    win.mouseVisible = True
    mouse.setPos(newPos=(0,-0.3))
    
    #pic_done = 0
    confidence_rating.reset()
    # keep track of which components have finished
    confidenceRatingComponents = [confidence_rating, confidence_text, text_mouse]
    for thisComponent in confidenceRatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    confidenceRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "confidenceRating"-------
    while continueRoutine:
        # get current time
        t = confidenceRatingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=confidenceRatingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #if t > 0.5 and pic_done == 0:
        #    win.getMovieFrame()
        #    win.saveMovieFrames('confidenceRating.png') 
        #    pic_done = 1
        
        # *confidence_rating* updates
        if confidence_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_rating.frameNStart = frameN  # exact frame index
            confidence_rating.tStart = t  # local t and not account for scr refresh
            confidence_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_rating, 'tStartRefresh')  # time at next scr refresh
            confidence_rating.setAutoDraw(True)
        
        # Check confidence_rating for response to end routine
        if confidence_rating.getRating() is not None and confidence_rating.status == STARTED:
            continueRoutine = False
        
        # *confidence_text* updates
        if confidence_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_text.frameNStart = frameN  # exact frame index
            confidence_text.tStart = t  # local t and not account for scr refresh
            confidence_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_text, 'tStartRefresh')  # time at next scr refresh
            confidence_text.setAutoDraw(True)
        
        # *text_mouse* updates
        if text_mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mouse.frameNStart = frameN  # exact frame index
            text_mouse.tStart = t  # local t and not account for scr refresh
            text_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mouse, 'tStartRefresh')  # time at next scr refresh
            text_mouse.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidenceRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "confidenceRating"-------
    for thisComponent in confidenceRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if startGame == 1 and tooLate == 0: 
        loop_trials.addData('confidence_own.rating', confidence_rating.getRating())
        loop_trials.addData('confidence_own.rt', t)
    win.mouseVisible = False
    core.wait(0.5)
    # the Routine "confidenceRating" was not non-slip safe, so reset the non-slip timer
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
    
    # retrieve confidence level to use in this trial, based on current nTotal and ratio and filer wave1 data
    if startGame == 0:
        confidence_level = trial_index + 1
        filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level] # filter wave1 data / social information based on current ratio and confidence level
    elif filler_trial == 0:
        confidence_level = [row for row in nTotal_ratio_confidence if row['nTotal']==nTotal and row['ratio']==true_ratio][0]['confidence'] # pick first element with specific ratio and nTotal and return confidence level
        nTotal_ratio_confidence = [row for row in nTotal_ratio_confidence if not (row['nTotal']==nTotal and row['ratio']==true_ratio and row['confidence']==confidence_level)]  # remove element so it wont be used another time
        filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level] # filter wave1 data / social information based on current ratio and confidence level
    elif filler_trial == 1:
        filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio]  # filter wave1 data / social information based on current ratio 
        if true_ratio == 0 or true_ratio == 1:
            confidence_level = 3 # makes more sense if peer is very confidence in those obvious trials
            filtered_SI = [row for row in wave1 if row['true_ratio']==true_ratio and row['confidence']==confidence_level]
    
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
            confidence_level = 1
            filtered_SI2 = [row for row in filtered_SI if (row['estimate'] < estimate1 - 40 or row['estimate'] > estimate1 + 40) and row['confidence'] == confidence_level]
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
    
    
    # if no suitable SI could be found, just include all SI
    if len(filtered_SI2) == 0:
        filtered_SI2 = filtered_SI
    
    # now randomly choose a peer estimate from filtered list
    random_index = int(random.randint(0,len(filtered_SI2),1))
    peer_estimate = filtered_SI2[random_index]['estimate']
    confidence_level = filtered_SI2[random_index]['confidence']
    
    # define image to show about peers confidence 
    if confidence_level == 1:
        peers_confidence_image = "low_peerConfidence.png"
    elif confidence_level == 2:
        peers_confidence_image = "medium_peerConfidence.png"
    elif confidence_level == 3:
        peers_confidence_image = "high_peerConfidence.png"
    
    # parameters for visual peer estimate information 
    markerPosition_peer = (peer_estimate - 50) / 100
    
    # do not run if in first practice phase
    if practice_phase is not 2:
        continueRoutine = False
    
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
    
    # set alignment of text
    estimateOther.alignText='left'
    estimateSelf.alignText='left'
    
    # text about how to submit
    if startGame == 1:
        howToRespond = "" 
    else: 
        howToRespond = "Gebruik de pijlen om je beslissing aan te geven\nen druk op ENTER om je beslissing op te slaan."
    
    #pic_done = 0
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
    SIComponents = [how_many_mushrooms_2, white_rectangle_peer, peer_confidence_rating, blue_box_peer, sliderMarker_peer, showEstimate_peer, white_rectangle_2, blue_box_E1, showEstimate_E1, sliderMarker_E1, blue_box_E2, showEstimate_E2, sliderMarker_E2, enterToRespond, red_box_peer, showEstimate_red_peer, red_box_E1, showEstimate_red_E1, red_box_E2, showEstimate_red_E2, estimateOther, estimateSelf]
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
        #if t > 1 and t < SI_delay and pic_done == 0 and confidence_level == 2:
        #    win.getMovieFrame()
        #    win.saveMovieFrames('estimation2_1.png') 
        #    pic_done = 1
        #if t > SI_delay and pic_done == 1 and confidence_level == 2:
        #    win.getMovieFrame()
        #    win.saveMovieFrames('estimation2_2.png') 
        #    pic_done = 2
        
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
        
            # move slider colors along with response
            keys = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = False, clear=False)
            keys_released = kb.getKeys(['left', 'right', 'return', 'num_enter', 'o'], waitRelease = True, clear=False)
        
            # everytime a new button is pressed in, I reset the speed with which the slider marker moves
            if len(keys) > nKeys: # new key pressed in
                nKeys = len(keys) # update nKeys
                tMove_start = t # reset speed reference point to start of new button press
                if startGame == 1:
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
                    if key == 'left':
                        tempRating -= math.exp(speed*1.5)-1 # -1 to make it move extra slow for short presses, but still fast for long presses. 
                        submit = 1
                    elif key =='right': 
                        tempRating += math.exp(speed*1.5)-1
                        submit = 1
                    elif (key == 'return' or key == 'num_enter') and submit == 1:
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
        
        # *white_rectangle_2* updates
        if white_rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_rectangle_2.frameNStart = frameN  # exact frame index
            white_rectangle_2.tStart = t  # local t and not account for scr refresh
            white_rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_rectangle_2, 'tStartRefresh')  # time at next scr refresh
            white_rectangle_2.setAutoDraw(True)
        
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
    #win.getMovieFrame()
    #win.saveMovieFrames('response.png') 
    kb.clearEvents()
    
    if startGame == 1: 
        estimate2 = int(rating)
        # performance
        if tooLate == 0:
            estimate2_rt = rt-SI_delay
            deviance = estimate2 - true_ratio*100
            abs_deviance = abs(deviance)
        elif tooLate == 1:
            estimate2_rt = []
    
        # only save data during actual task, not practice
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
            expInfo['bonus'] = bonus
    
    
    trial_index += 1
    
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
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_trials'


# ------Prepare to start Routine "instructions_end"-------
continueRoutine = True
# update component parameters for each repeat
s_to_end.keys = []
s_to_end.rt = []
_s_to_end_allKeys = []
blue_mushroom_4.setPos((window_x-0.3, -0.4))
red_mushroom_4.setPos((window_x-0.2, -0.4))
# keep track of which components have finished
instructions_endComponents = [bonus_text, s_to_end, blue_mushroom_4, red_mushroom_4]
for thisComponent in instructions_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_end"-------
while continueRoutine:
    # get current time
    t = instructions_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_endClock)
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
    
    # *s_to_end* updates
    waitOnFlip = False
    if s_to_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        s_to_end.frameNStart = frameN  # exact frame index
        s_to_end.tStart = t  # local t and not account for scr refresh
        s_to_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(s_to_end, 'tStartRefresh')  # time at next scr refresh
        s_to_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(s_to_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(s_to_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if s_to_end.status == STARTED and not waitOnFlip:
        theseKeys = s_to_end.getKeys(keyList=['s'], waitRelease=False)
        _s_to_end_allKeys.extend(theseKeys)
        if len(_s_to_end_allKeys):
            s_to_end.keys = _s_to_end_allKeys[-1].name  # just the last key pressed
            s_to_end.rt = _s_to_end_allKeys[-1].rt
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
    for thisComponent in instructions_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_end"-------
for thisComponent in instructions_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
