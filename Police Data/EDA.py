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
import os
import sys
import pandas as pd
import numpy as np
import scipy

# Point to local file for custom scripts. 
sys.path.append('C:/Users/David-PC/Dropbox/Coding/Local Python Modules/')  # Home PC

#% Set working directory
os.chdir('C:/Users/David-PC/Dropbox/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching & Police Behavior')

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Read in the data
raw_data = pd.read_csv('tn_nashville_2020_04_01.csv', low_memory=False)
data = raw_data.copy()
list(data)
len(data)

#%% Plot the number of times different races were pulled over. 
import matplotlib.pyplot as plt
import seaborn as sns

race_counts = data.subject_race.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(race_counts.index, race_counts.values, color='black')
plt.title('Nashville, TN (2010-2019)')
plt.ylabel('Number of Stops', fontsize=16)
plt.xlabel('Race', fontsize=16)
plt.show()

#%% Plot the number of times different races were pulled over. 
sex_counts = data.subject_sex.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(sex_counts.index, sex_counts.values, color='black')
plt.title('Nashville, TN (2010-2019)')
plt.ylabel('Number of Stops', fontsize=16)
plt.xlabel('Sex', fontsize=16)
plt.show()

#%% Create list of office ids for separating data out
officers = data.officer_id_hash.unique()
print('Number of officers in df: ', len(officers))

#%% Pull one officer to run analysis with
ofcr_a = data.loc[data['officer_id_hash']=='80ed1b32eb']
print('Officer 80ed1b32eb pulled over', len(ofcr_a), 'people between 2010 and 2019')

#%% Create lists of sums of every 50 row
search_counts = ofcr_a.
ofcr_a_prob_search = 


ofcr_a.head(20)

