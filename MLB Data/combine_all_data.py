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
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/MLB Data/'
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
all_mlb_data.to_csv('MLB_pitches_08_19.csv')

#%% If pikcing up fresh
raw_data = pd.read_csv('MLB_pitches_08_19.csv')
df = raw_data.copy()

#%% Keep just the columns we're interested in using for the analysis
