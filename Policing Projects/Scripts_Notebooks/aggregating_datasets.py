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
directory = '/Users/davidjcox/Dropbox (Personal)/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching/KaggleWebscrapingAnalysis/Man-vs-Machine/Policing Projects/Data/'
os.chdir(directory)

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Loop through the files and combine all the raw datasets. 
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

# Combine into single dataframe
all_df = pd.concat(all_data)

# Add year and month to df as unique col
all_df['year'] = pd.DatetimeIndex(all_df['date']).year
all_df['month'] = pd.DatetimeIndex(all_df['date']).month

# Save 
all_df.to_csv('all_data.csv')

#%% Some one-off stats for the ms
all_df.year.describe()
len(all_df.officer_id_hash.unique())

#%% Create individual data frames for the different independent and dependent variables
offcr_stops = all_df.groupby(['year', 'month', 'officer_id_hash']).size()
offcr_cites = all_df.groupby(['year', 'month', 'officer_id_hash', 'citation_issued']).size()
offcr_search = all_df.groupby(['year', 'month', 'officer_id_hash', 'search_conducted']).size()
offcr_frisk = all_df.groupby(['year', 'month', 'officer_id_hash', 'frisk_performed']).size()
offcr_contra = all_df.groupby(['year', 'month', 'officer_id_hash', 'contraband_found']).size()
offcr_arrest = all_df.groupby(['year', 'month', 'officer_id_hash', 'arrest_made']).size()

#%% Print descriptions of each subset dataframe 
from scipy.stats import skew
grouped_data = [offcr_stops, offcr_cites, offcr_search, offcr_frisk, offcr_contra, offcr_arrest]
data_type = ['Stops', 'Citations', 'Searches', 'Frisks', 'Contraband Found', 'Arrests']

for i in range(len(grouped_data)):
  print(data_type[i], "| Skew =", round(skew(grouped_data[i]), 4), "\n", grouped_data[i].describe(), "\n")
  
#%% Plot letter-value plots / boxen plots of the different distributions. 
def boxen(df, x_label):
  f, ax = plt.subplots(figsize=(2, 5))
  sns.boxenplot(y=df, color='white')
  plt.xlabel(x_label, fontsize=20, labelpad=(16))
  plt.ylabel('Count per Month', fontsize=20, labelpad=(16))
  plt.ylim(.1, 1000)
  plt.yscale("log")
  plt.yticks(ticks=[.1, 1, 10, 100], labels=['0.1', '1', '10', '100'], fontsize=12)
  # plt.yticks(fontsize=12)
  right_side = ax.spines["right"]
  right_side.set_visible(False)
  top = ax.spines["top"]
  top.set_visible(False)
  plt.show()

boxen(offcr_stops, 'Stops')
boxen(offcr_cites, 'Citations')
boxen(offcr_search, 'Searches')
boxen(offcr_frisk, 'Frisks')
boxen(offcr_contra, 'Contraband')
boxen(offcr_arrest, 'Arrests')

#%% Combine all the fit dataframes
fit_directory = '/Users/davidjcox/Downloads/All Fits/'
all_fit = []
troublesome = []
err_type = []

for subdir, dirs, files in os.walk(fit_directory):
    for filename in files:
        filepath = os.path.join(subdir, filename)
        try:
            if '.csv' in filepath:
                str_end = filename.find('_')
                string = filename[:str_end]
                # Read in df and add cols for city sand state 
                raw_data = pd.read_csv(filepath)
                data = raw_data.copy()
                data['city'] = string
                all_fit.append(data)
        except:
            err = type(Exception).__name__
            err_type.append(err)
            troublesome.append(filename)

# Combine into single dataframe
all_fit = pd.concat(all_fit)

# Save 
all_fit.to_csv('all_fits.csv')

#%% Separate out the different dfs for different events
cite_fits = all_fit[all_fit['reniforcer']=='citations']

#%% Print the proportion of officers whose databehavior was described by the single-alternative matching equation 
# with vac greater than 90%
print((round((cite_fits['vac'].ge(0.9).sum())/len(cite_fits), 5)), "= Citation Proportion >90%")
print((round((search_fits['vac'].ge(0.9).sum())/len(search_fits), 5)), "= Search Proportion >90%")
print((round((frisk_fits['vac'].ge(0.9).sum())/len(frisk_fits), 5)), "= Frisk Proportion >90%")
print((round((contra_fits['vac'].ge(0.9).sum())/len(contra_fits), 5)), "= Contraband Found Proportion >90%")
print((round((arrest_fits['vac'].ge(0.9).sum())/len(arrest_fits), 5)), "= Arrest Proportion >90%")