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

#%% Subset df by pitch type
unique_pitches = verlander_df['pitch_name'].unique()
FF = verlander_df[verlander_df['pitch_type']=='FF']
CU = verlander_df[verlander_df['pitch_type']=='CU']
FS = verlander_df[verlander_df['pitch_type']=='FS']
FC = verlander_df[verlander_df['pitch_type']=='FC']
SL = verlander_df[verlander_df['pitch_type']=='SL']
FT = verlander_df[verlander_df['pitch_type']=='FT']
IN = verlander_df[verlander_df['pitch_type']=='IN']
PO = verlander_df[verlander_df['pitch_type']=='PO']

#%% 
