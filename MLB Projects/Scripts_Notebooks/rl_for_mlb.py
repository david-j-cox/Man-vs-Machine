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

# Set path to local scripts
sys.path.append('/Users/davidjcox/Dropbox/Coding/Local Python Modules/')

# Set path to data
os.chdir('/Users/davidjcox/')

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#% Read in the data
raw_data = pd.read_csv()
data = raw_data.copy()
data.head()

#%
