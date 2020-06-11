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

#%% Plot the number of times 
import matplotlib.pyplot as plt
import seaborn as sns

race_counts = data.subject_race.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(race_counts.index, race_counts.values, color='black')
plt.title('Nashville, TN (2010-2019)')
plt.ylabel('Number of Stops', fontsize=16)
plt.xlabel('Race', fontsize=16)
plt.show()

#%% Create list of office ids for separating data out
officers = data.officer_id_hash.unique()

data.date.max()
data.date.min()
