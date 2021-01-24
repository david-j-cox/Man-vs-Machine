#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
#Set current working directory to the folder that contains your data.
import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Set path to local scripts
sys.path.append('/Users/davidjcox/Dropbox/Coding/Local Python Modules/')

# Set path to data
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/MLB Projects/Pitch Data/'
os.chdir(directory)

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Read in data
raw_data = pd.read_csv('all_pitches_08_19.csv', low_memory=False)
data = raw_data.copy()
data.head()

#%% Pick a player to start with - the one with the msot observations
player_list = data['player_name'].value_counts()[:10]

#%% Subset out each of the top 10 pitchers with observations
verlander_df = data[data['player_name']=='Justin Verlander'].drop_duplicates(subset=['game_date', 'at_bat_number', 'pitch_number', 'pitch_name']).dropna(subset=['pitch_type'])
verlander_df = verlander_df.sort_values(by=['game_date', 'at_bat_number', 'pitch_number'], ascending=True).reset_index().drop(['index', 'Unnamed: 0'], axis=1)
verlander_df.head(25)
verlander_df.to_csv('verlander_df.csv')

#%% Define the environment
'''
General framework:
Runners = [1st, 2nd, 3rd]
Count, outs = [Balls, Strikes, Outs]
Inning = [1-3, 4-6, 7-9] --> [innings 1-2-3, 4-5-6, 7-8-9]
Score = [Home, Away, Assign] --> Assign = 0 if pitcher is home, 1 if away

For example, a game state at the beginning of the game with the home pitcher pitching:
    [[0, 0, 0], 
     [0, 0, 0], 
     [1, 0, 0], 
     [0, 0, 0]]

A game state in the bottom of the 4th inning, runner on 2nd, 2 outs, 2 balls, 1 strike, and a score of 6-4 (home-away):
    [[0, 1, 0], 
     [2, 1, 2], 
     [0, 4, 0], 
     [6, 4, 1]]
'''

#%% Basic reinforcement learning model.  After each pitch: 
#   - Update game state 
#   - Reinforce for guessing right pitch
#   - Punish for guessing wrong


#%% Only local reinforcement contingencies. After each pitch:
#   - Update game state
#   - Reinforce for guessing right pitch
#   - Punish for guessing wrong pitch
#   - Extra weight on pitch type if led to strike or out (Amount? How many pitches does it last? Insert memory decay? RaC model?)
#   - Extra weight on pitch type if led to ball or hit (Amount? How many pitches does it last? Insert memory decay? Rac model?)


#%% Only molar  reinforcement contingencies. After each pitch:
#   - Update game state
#   - Reinforce for guessing right pitch
#   - Punish for guessing wrong pitch
#   - Extra reinforcement weight on pitch type based on Baum 2012 (Amount? How many pitches are considered? Insert memory decay? RaC model?)
#   - Extra punishment weight on pitch type based on Baum 2012 (Amount? How many pitches are considered? Insert memory decay? Rac model?)


#%% Local and molar contingencies. After each pitch: 
#   - Update game state
#   - Reinforce for guessing right pitch
#   - Punish for guessing wrong pitch
#   - Extra weight on pitch type if led to strike or out (Amount? How many pitches does it last? Insert memory decay? RaC model?)
#   - Extra weight on pitch type if led to ball or hit (Amount? How many pitches does it last? Insert memory decay? Rac model?)
#   - Extra reinforcement weight on pitch type based on Baum 2012 (Amount? How many pitches are considered? Insert memory decay? RaC model?)
#   - Extra punishment weight on pitch type based on Baum 2012 (Amount? How many pitches are considered? Insert memory decay? Rac model?)

