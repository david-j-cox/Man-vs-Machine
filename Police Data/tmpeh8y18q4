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

#%%

import urllib.request
link = 'https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_tn_nashville_2020_04_01.csv.zip'
urllib.request.urlretrieve(link, "yg821jf8611_tn_nashville_2020_04_01.csv.zip")
compressed_file = zipfile.ZipFile('yg821jf8611_tn_nashville_2020_04_01.csv')
                                  


#%% Read in the data
raw_data = pd.read_csv(r)
data = raw_data.copy()
data.head()

