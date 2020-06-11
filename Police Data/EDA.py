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
raw_data = pd.read_csv('')
data = raw_data.copy()
data.head()

