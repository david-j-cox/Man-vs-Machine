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

#%% Create a rolling window of reinforcement for each pitch type
# cumsum() pandas.rolling_window()
fastballs = ['FF', 'FS', 'FT']
num_fast = 0
count = []
for i in range(len(odorizzi_df)):
    if odorizzi_df['pitch_type'][i] in fastballs:
        num_fast +=1
        count.append(num_fast)
    else:
        num_fast -=1
        count.append(num_fast)

count = pd.DataFrame(count)
x_values = range(len(odorizzi_df))
count['x_vals'] = x_values
count.columns = ['count', 'x_vals']

#%% Reinforcement learning model
movement = []
rl_pred = []
iteration = 1
err = 20

for i in range(len(count)):
    rand = random.random()
    if rand < 0.5:
        rand = rand*-err
    else:
        rand = rand*err
    rand = int(rand)
    movement.append(rand)
    val = count['count'][i]
    pred = val+rand
    rl_pred.append(pred)
    iteration+=1
    if iteration%10==0:
        err = err*0.9925

count['rl_pred'] = rl_pred
count['error'] = count['count']-count['rl_pred']

#%% Plot dynamics of fastballs over time
f, ax = plt.subplots(figsize=(15, 10))
plt.scatter('x_vals','error', data=count, marker='o', color='k')
# Making it look good
plt.xlabel("Pitch Number Out of %s" %len(odorizzi_df), fontsize=24, labelpad=(16))
plt.xticks(fontsize=16)
plt.xlim(0, 5000)
plt.ylabel("Prediction Loss Term", fontsize=24, labelpad=(16))
plt.title('Jake Odorizzi Predictions', fontsize=24)
plt.yticks(fontsize=18)
right_side = ax.spines["right"]
right_side.set_visible(False)
top = ax.spines["top"]
top.set_visible(False)
# plt.savefig('qa_metrics.png', bbox_inches='tight')
plt.show()

#%% Reinforcement learning model to predict the next pitch
movement = []
rl_pred = []
iteration = 1
err = 1

for i in range(len(count)):
    rand = random.random()
    if iteration < 12:
        movement.append(1)
    elif (iteration >=12) and (iteration < 113):
        if rand < 0.8:
            val = 1
        else:
            val = 0
        movement.append(val)
    elif (iteration >=113) and (iteration < 1000):
        if (iteration%100==0) or (iteration%23==0):
            movement.append(1)
        elif rand < 0.1:
            val = 1
            movement.append(val)
        else:
            val = 0
            movement.append(val)
    elif (iteration >=1000) and (iteration < 4236):
        if (iteration%126==0):
            movement.append(1)
        elif rand < 0.005:
            val = 1
            movement.append(val)
        else:
            val = 0
            movement.append(val)
    else:
        movement.append(0)
    iteration +=1

count['movement'] = movement
count['error'] = count['movement'].cumsum()
