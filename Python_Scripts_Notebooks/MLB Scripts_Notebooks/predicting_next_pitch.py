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
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/'
os.chdir(directory)

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Read in data
raw_data = pd.read_csv('All_MLB_data_for_GME.csv')
data = raw_data.copy()
data.head()

#%% Pick a player to start with - the one with the msot observations
player_list = data['player_name'].value_counts()[:10]


#%% Subset out each of the top 10 pitchers with observations
odorizzi_df = data[data['player_name']=='Jake Odorizzi'].drop_duplicates(subset=['game_date', 'at_bat_number', 'pitch_number', 'pitch_name']).dropna(subset=['pitch_type'])
odorizzi_df = odorizzi_df.sort_values(by=['game_date', 'at_bat_number', 'pitch_number'], ascending=True).reset_index().drop(['index', 'Unnamed: 0'], axis=1)
odorizzi_df.head(25)    

#%% Subset df by pitch type
unique_pitches = odorizzi_df['pitch_name'].unique()
FF = odorizzi_df[odorizzi_df['pitch_type']=='FF']
CU = odorizzi_df[odorizzi_df['pitch_type']=='CU']
FS = odorizzi_df[odorizzi_df['pitch_type']=='FS']
FC = odorizzi_df[odorizzi_df['pitch_type']=='FC']
SL = odorizzi_df[odorizzi_df['pitch_type']=='SL']
FT = odorizzi_df[odorizzi_df['pitch_type']=='FT']
IN = odorizzi_df[odorizzi_df['pitch_type']=='IN']
PO = odorizzi_df[odorizzi_df['pitch_type']=='PO']

#%%