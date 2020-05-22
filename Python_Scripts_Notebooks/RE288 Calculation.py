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
                                  ascending=(True,False,False,False))
    data_gs = data_gs.reset_index()
    
    # Add column to indicate whether the inning changed after each pitch. 
    data_gs['inning_same'] = data_gs.inning == data_gs.inning.shift()
    
    # Add column of total runs scored to this point in game. 
    data_gs['total_runs'] = data['home_score'] + data['away_score'] 
    runs_scored = []
    for row, value in enumerate(data_gs['game_pk']):
        curr_game = value
        df_length = len(data_gs)-1
        if (row<df_length):
            prev_row_game = row+1
            prev_row_game_val = data_gs.game_pk[prev_row_game]
            if (curr_game!=prev_row_game_val):
                runs = data_gs.home_score[row] + data_gs.away_score[row]
                runs_scored.append(runs)
            if (row==0):
                prev_row = row+1
                ho_sc_1 = data_gs.home_score[row]
                aw_sc_1 = data_gs.away_score[row]
                curr_tot = ho_sc_1 + aw_sc_1
                ho_sc_2 = data_gs.home_score[prev_row]
                aw_sc_2 = data_gs.away_score[prev_row]
                prev_tot = ho_sc_2 + aw_sc_2
                if (curr_tot < prev_tot):
                    runs_scored.append(prev_tot)
                else:
                    runs_scored.append(curr_tot)
            else:
                prev_row = row-1
                ho_sc_1 = data_gs.home_score[row]
                aw_sc_1 = data_gs.away_score[row]
                curr_tot = ho_sc_1 + aw_sc_1
                ho_sc_2 = data_gs.home_score[prev_row]
                aw_sc_2 = data_gs.away_score[prev_row]
                prev_tot = ho_sc_2 + aw_sc_2
                if (curr_tot > prev_tot):
                    runs_scored.append(prev_tot)
                else:
                    runs_scored.append(curr_tot)
        if (row==df_length):
            prev_row = row-1
            ho_sc_1 = data_gs.home_score[row]
            aw_sc_1 = data_gs.away_score[row]
            curr_tot = ho_sc_1 + aw_sc_1
            ho_sc_2 = data_gs.home_score[prev_row]
            aw_sc_2 = data_gs.away_score[prev_row]
            prev_tot = ho_sc_2 + aw_sc_2
            if (curr_tot > prev_tot):
                runs_scored.append(prev_tot)
            else:
                runs_scored.append(curr_tot)
    
    # Append total runs col to df.
    change_score = pd.DataFrame(runs_scored)
    change_score.columns = ['total_runs']
    data_gs = pd.concat([data_gs, runs_scored], axis=1)  
    
    # Add column to indicate the change in score after each pitch. 
    change_score = [] 
    for row, value in enumerate(data_gs['inning_same']):
        if (value==True):
            minus = row-1
            change_val = data_gs.total_runs[minus] - data_gs.total_runs[row]
            if change_val >= 0:
                change_score.append(change_val)
            else:
                change_score.append(0)
        else:
            change_score.append(0)


    
    # Append the change_score col to df
    change_score = pd.DataFrame(change_score)
    change_score.columns = ['change_score']
    data_gs = pd.concat([data_gs, change_score], axis=1)  
    
    
      
    # Add column that sums number of runs scored in that inning after each pitch. 
    last_false = 0
    run_sum = []
    run_sum_val = 0
    for row, value in enumerate(data_gs['inning_same']):
        if (value==False):
            end = row-1
            run_sum_val = data_gs['change_score'].loc[last_false:end].cumsum()
            run_sum.append(run_sum_val)
            last_false = row + 1
            print('appended')
        else:
            pass
    all_run_sums = []
    for sublist in run_sum:
        for i in sublist:
            all_run_sums.append(i)
    
    # Append the cumulative sum of runs to the df
    runs_to_inning_end = pd.DataFrame(all_run_sums)
    runs_to_inning_end.columns = ['runs_inn_end']
    data_gs = pd.concat([data_gs, runs_to_inning_end], axis=1)

data_gs.head(50)
list(data_gs)
    
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