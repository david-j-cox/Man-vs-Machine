#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 
    David J. Cox, PhD, MSB, BCBA-D
    dcox33@jhmi.edu
    https://www.researchgate.net/profile/David_Cox26
    twitter: @davidjcox_
    LinkedIn: https://www.linkedin.com/in/coxdavidj/
    Website: https://davidjcox.xyz
"""
# Packages!!!
import glob
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Point to local file for custom scripts. 
sys.path.append('C:/Users/David-PC/Dropbox/Coding/Local Python Modules/')

# Set working directory
os.chdir('C:/Users/David-PC/Dropbox/Baseball Matching/')

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

from RE288 import RE288_calc

# %% Play with specific data

data_raw = pd.read_csv("pirates_2016.csv")
len(data_raw)
data_raw.head()

data = pd.read_csv('pirates_2016.csv')
list(data)
data_list = ['balls', 'strikes', 'on_3b', 'on_2b', 'on_1b', 'outs_when_up', 'inning', \
             'inning_topbot', 'game_pk', 'at_bat_number', 'pitch_number', 'bat_score', 'post_bat_score']

data_use = data[data_list]
data = data_use
# %% Iterate through files in folder to calculate game state for each pitch, \
#   add game state column to each .csv file, and \
#   save new .csv with different file name indicating change made.  

for file in glob.glob(path):
    data = pd.read_csv(file)

    # Replace null values with 0s. 
    data['on_1b'].fillna(0, inplace=True)
    data['on_2b'].fillna(0, inplace=True)
    data['on_3b'].fillna(0, inplace=True)
    
    # Replace runner MLB player IDs with a 1. 
    data.loc[(data['on_1b'] > 0), 'on_1b'] = 1
    data.loc[(data['on_2b'] > 0), 'on_2b'] = 1
    data.loc[(data['on_3b'] > 0), 'on_3b'] = 1
    
    # Assign game state identifier for every pitch thrown. 288 game states possible \
    # using all unique combinations of balls, strikes, outs, and location of baserunners.
    game_state = RE288_calc(data=data, balls='balls', strikes='strikes', outs='outs_when_up', \
           runner_first='on_1b', runner_second='on_2b', runner_third='on_3b')
    
    # Convert list to Pandas dataframe and concatenate with existing data
    game_state = pd.DataFrame(game_state)
    game_state.columns = ['game_state']
    data_gs = pd.concat([data, game_state], axis=1, join='inner')
    
    # Add column to indicate whether the inning changed after each pitch. 
    data_gs['inning_same'] = data_gs.inning == data_gs.inning.shift()
    
    # Add column to indicate the change in score after each pitch. 
    data_gs['change_score'] = data_gs['post_bat_score'] - data_gs['bat_score']
    
    # Add column that sums number of runs scored in that inning after each pitch. 
    data_gs['inning_run_sum'] = (data_gs.groupby(data_gs['inning_same'].eq(False).cumsum())
                   ['change_score'].apply(lambda x: (x[::-1].cumsum())[::-1] ))
    
    # Save new dataframe to new .csv file titled *_gs.csv
    data_gs.to_csv(file+'_gs.csv')

# %% Combine all of the data into a single .csv file. 
# create a list with the column headers so we can skip that line when adding
# each new data set. 
header=['Unnamed: 0', 'balls', 'strikes', 'on_3b', 'on_2b', 'on_1b', \
        'outs_when_up', 'inning', 'inning_topbot', 'game_pk', 'at_bat_number', \
        'pitch_number', 'bat_score', 'post_bat_score', 'game_state', \
        'inning_same', 'change_score', 'inning_run_sum']

# Combine all game state .csvs into single .csv. 
with open('All_MLB_data_2019.csv', 'a') as singleFile:
    for file in glob.glob(path):
        if file == 'All_MLB_data_2018.csv':
            pass
        elif file.endswith((".csv_gs.csv")):
            for line in open(file, 'r'):
                if line == header:
                    pass
                else:
                    singleFile.write(line)
singleFile.close()

# =============================================================================
# %% Script testing.  
# =============================================================================
data_test = pd.read_csv('Angels_2018.csv_gs.csv')
# Add column to indicate whether the inning changed after each pitch. 
data['inning_same'] = data.inning == data.inning.shift() 
# Add column to indicate the change in score after each pitch. 
for i in 

data['change_score'] = data['post_bat_score'] - data['bat_score']
# Add column that sums number of runs scored in that inning after each pitch. 
data['inning_run_sum'] = (data.groupby(data['inning_same'].eq(False).cumsum())
                   ['change_score'].apply(lambda x: (x[::-1].cumsum())[::-1] ))

data.to_csv('test.csv')

data.change_score.diff()
