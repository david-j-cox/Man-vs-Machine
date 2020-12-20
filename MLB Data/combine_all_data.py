#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 
    David J. Cox, PhD, MSB, BCBA-D
    cox.david.j@gmail.com
    https://www.researchgate.net/profile/David_Cox26
    twitter: @davidjcox_
    LinkedIn: https://www.linkedin.com/in/coxdavidj/
    Website: https://davidjcox.xyz
"""
#Set current working directory to the folder that contains your data.
import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# Set path to local scripts
sys.path.append('/Users/davidjcox/Dropbox/Coding/Local Python Modules/')

# Set path to data
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/MLB Data/Team Data/'
os.chdir(directory)

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Combien all data into a single .csv file
all_mlb_data = []

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        if 'csv' in filename:
            raw_data = pd.read_csv(filename)
            all_mlb_data.append(raw_data)

#%% Convert it into a pandas dataframe
all_mlb_data = pd.concat(all_mlb_data)

#%% Save it
all_mlb_data.to_csv('all_pitches_08_19.csv')

#%% If pikcing up fresh
raw_data = pd.read_csv('all_pitches_08_19.csv').drop(['Unnamed: 0 '], axis=1)
df = raw_data.copy()

#%% Keep just the columns we're interested in using for the analysis
df = df[['pitch_type', 'game_date', 'player_name', 'batter', 'events', 'description', 'des', 'home_team', 'away_team', \
         'type', 'bb_type', 'balls', 'strikes', 'game_year', 'on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', \
         'inning_topbot', 'at_bat_number', 'pitch_number', 'pitch_name', 'home_score', 'away_score', 'bat_score', \
         'fld_score', 'post_away_score', 'post_home_score', 'post_bat_score', 'post_fld_score', 'if_fielding_alignment', \
         'of_fielding_alignment']]

#%% Remove players with fewer than 500 observations
number_games = df['player_name'].value_counts()
min_obs_df = df[~df['player_name'].isin(number_games[number_games< 500].index)]

#%% 