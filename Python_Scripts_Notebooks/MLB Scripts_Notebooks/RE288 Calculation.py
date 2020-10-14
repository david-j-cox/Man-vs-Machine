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
from RE288 import RE288_calc

# Point to local file for custom scripts. 
sys.path.append('C:/Users/David-PC/Dropbox/Coding/Local Python Modules/')

# Set working directory
path = os.chdir('C:/Users/David-PC/Dropbox/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/Data/')

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Combine all files into single doc. 

header = ['pitch_type','game_date','batter','pitcher','events','description',\
          'zone','des','stand','p_throws','home_team','away_team','type','hit_location',\
          'bb_type','balls','strikes','game_year','on_3b','on_2b','on_1b',\
          'outs_when_up','inning','inning_topbot','fielder_2','hit_distance_sc',\
          'launch_speed','launch_angle','effective_speed','at_bat_number',\
          'pitch_number','home_score','away_score','if_fielding_alignment','of_fielding_alignment']

# Combine all .csvs into single .csv. 
with open('All_MLB_data.csv', 'a') as singleFile:
    for file in glob.glob('*.csv'):
        if file == 'All_MLB_data.csv':
            pass
        else:
            for line in open(file, 'r'):
                if line == header:
                    pass
                else:
                    singleFile.write(line)
singleFile.close()

# %% Play with specific data
data_raw = pd.read_csv("All_MLB_data.csv", nrows=20, skiprows=23695, error_bad_lines=False)
data_raw
data = data_raw.copy()
len(data_raw)
data_raw.head()

# %% Iterate through files in folder to calculate game state for each pitch, \
#   add game state column to each .csv file, and \
#   save new .csv with different file name indicating change made.  

for file in glob.glob(path):    
    data_raw = pd.read_csv('angels_2016.csv') # Read in file
    # Select only the cols we need
    data_list = ['pitch_type','game_date','batter','pitcher','events','description',\
          'zone','des','stand','p_throws','home_team','away_team','type','hit_location',\
          'bb_type','balls','strikes','game_year','on_3b','on_2b','on_1b',\
          'outs_when_up','inning','inning_topbot','fielder_2','hit_distance_sc',\
          'launch_speed','launch_angle','effective_speed','game_pk', 'at_bat_number',\
          'pitch_number','home_score','away_score','if_fielding_alignment','of_fielding_alignment']
    data = data_raw[data_list]
    data.head()
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
    
    # Sort by game_date, inning, 
    data_gs = data_gs.sort_values(['game_pk', 'inning', 'outs_when_up', 'pitch_number'], \
                                  ascending=(True,True, True, True))
    data_gs = data_gs.reset_index()
    print(data_gs[80:100])
    # Add column to indicate whether the inning changed after each pitch. 
    data_gs['inning_same'] = data_gs.inning == data_gs.inning.shift()
    
    # Add column to indicate the change in score after each pitch. 
    data_gs['total_runs'] = data['home_score'] + data['away_score']
    data_gs['change_score'] = data_gs.total_runs - data_gs.total_runs.shift()
    for row,value in enumerate(data_gs['change_score']):
        if (value<0):
            value = 0
        else:
            value = value
      
    # Add column that sums number of runs scored in that inning after each pitch. 
    last_false = 0
    run_sum = []
    run_sum_val = 0
    for row, value in enumerate(data_gs['inning_same']):
        if (value==False):
            run_sum_val = data_gs['change_score'].loc[last_false:row].cumsum()
            run_sum.append(run_sum_val)
            last_false = row + 1
            run_sum.append(0)
            print('appended')
        else:
            pass
    all_run_sums = []
    for sublist in run_sum:
        for i in sublist:
            all_run_sums.append(i)
    
    print(run_sum)
    len(data_gs)
    len(run_sum)
    print(all_run_sums)
    
    data_gs['inning_run_sum'] = 
    (data_gs.groupby(data_gs['inning_same'].eq(False).cumsum())
                   ['change_score'].apply(lambda x: (x[::-1].cumsum())[::-1] ))
    
    print(data_gs[:50])
    
    # Save new dataframe to new .csv file titled *_gs.csv
    data_gs.to_csv(file+'_gs.csv')

# %% Combine all of the data into a single .csv file. 
# create a list with the column headers so we can skip that line when adding
# each new data set. 
header=['Unnamed: 0', 'pitch_type','game_date','batter','pitcher','events','description',\
          'zone','des','stand','p_throws','home_team','away_team','type','hit_location',\
          'bb_type','balls','strikes','game_year','on_3b','on_2b','on_1b',\
          'outs_when_up','inning','inning_topbot','fielder_2','hit_distance_sc',\
          'launch_speed','launch_angle','effective_speed','at_bat_number',\
          'pitch_number','home_score','away_score','if_fielding_alignment','of_fielding_alignment']

# Combine all game state .csvs into single .csv. 
with open('All_MLB_data.csv', 'a') as singleFile:
    for file in glob.glob(path):
        if file == 'All_MLB_data.csv':
            pass
        elif file.endswith((".csv_gs.csv")):
            for line in open(file, 'r'):
                if line == header:
                    pass
                else:
                    singleFile.write(line)
singleFile.close()