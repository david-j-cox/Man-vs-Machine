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

# Set path to local scripts
sys.path.append('/Users/davidjcox/Dropbox/Coding/Local Python Modules/')

# Set path to data
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/Policing Projects/Data/'
os.chdir(directory)

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Loop through the files and combine all the datasets. 
all_data = []
troublesome = []
err_type = []

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(subdir, filename)
        try:
            if '.csv' in filepath:
                str_end = filename.find('2020')-1
                string = filename[:str_end]
                sep = string.find('_')
                t_city = string[:sep]
                t_state = string[(sep+1):]
                # Read in df and add cols for city sand state 
                raw_data = pd.read_csv(filename)
                data = raw_data.copy()
                data['city'] = t_city
                data['state'] = t_state
                print(data.head())
                all_data.append(data)
        except:
            err = type(Exception).__name__
            err_type.append(err)
            troublesome.append(filename)

#%% Combine into single dataframe and save
all_df = pd.concat(all_data)
all_df.to_csv('all_data.csv')

#%% Add year and month to df as unique cols
all_df['year'] = pd.DatetimeIndex(all_df['date']).year
all_df['month'] = pd.DatetimeIndex(all_df['date']).month

#%%