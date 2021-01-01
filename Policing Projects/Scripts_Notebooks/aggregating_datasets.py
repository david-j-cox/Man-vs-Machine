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
                if ('all_fits' not in filepath) or ('all_data' not in filepath):
                    print(filepath)
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

#%% If picking up fresh
raw_data = pd.read_csv('all_data.csv', low_memory=False).drop(['Unnamed: 0'], axis=1)
all_df = raw_data.copy()

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
  sns.boxplot(y=df, color='white')
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
fit_directory = '/Users/davidjcox/Downloads/All Fits Data/'
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
all_fit = all_fit.reset_index().drop(['index', 'Unnamed: 0'], axis=1)
all_fit.to_csv('all_fits.csv')
all_fit[::50000]

#%% Some unique hash ids were generated across multiple departments. Create unique id using city and hash id
all_fit['unique_id'] = all_fit['person_num'] + "_" + all_fit['city']
all_fit.head(20)

#%% Separate out the different dfs for different events
ninety_fit = all_fit[(all_fit['vac']>=0.90)]
print(len(ninety_fit.unique_id.unique())/(len(all_fit.unique_id.unique())))
eighty_fit = all_fit[(all_fit['vac']>=0.80)]
print(len(eighty_fit.unique_id.unique())/(len(all_fit.unique_id.unique())))

#%% Info for each specific reinforcer
cite_fits = all_fit[(all_fit['reinforcer']=='citations')]
search_fits = all_fit[(all_fit['reinforcer']=='searches')]
frisk_fits = all_fit[(all_fit['reinforcer']=='frisks')]
contra_fits = all_fit[(all_fit['reinforcer']=='contraband')]
arrest_fits = all_fit[(all_fit['reinforcer']=='arrests')]

#%% Violin plots of fit distributions
def violin(df, y_label):
  f, ax = plt.subplots(figsize=(20, 8))
  sns.violinplot(x='fit_type', y='vac', data=df, order=['overall', 'asian/pacific islander', 'black', 'hispanic', 
                                                        'white', 'other', 'unknown'])
  plt.xlabel('', fontsize=20, labelpad=(16))
  plt.ylabel(y_label, fontsize=20, labelpad=(16))
  plt.ylim(-2, 1)
  plt.yticks(fontsize=12)
  plt.xticks(fontsize=12, rotation=45)
  right_side = ax.spines["right"]
  right_side.set_visible(False)
  top = ax.spines["top"]
  top.set_visible(False)
  plt.show()

violin(cite_fits, 'Citations')
violin(search_fits, 'Searches')
violin(frisk_fits, 'Frisks')
violin(contra_fits, 'Contraband')
violin(arrest_fits, 'Arrests')

#%% Try boxen here
def boxen(df, y_label):
  f, ax = plt.subplots(figsize=(20, 8))
  sns.boxplot(x='fit_type', y='vac', color='white', data=df, order=['overall', 'asian/pacific islander', 'black', 
                                                                      'hispanic', 'white', 'other', 'unknown'])
  plt.xlabel('', fontsize=20, labelpad=(16))
  plt.ylabel(y_label, fontsize=20, labelpad=(16))
  plt.ylim(-2, 1)
  plt.yticks(fontsize=12)
  right_side = ax.spines["right"]
  right_side.set_visible(False)
  top = ax.spines["top"]
  top.set_visible(False)
  plt.show()
  
boxen(cite_fits, 'Citations')
boxen(search_fits, 'Searches')
boxen(frisk_fits, 'Frisks')
boxen(contra_fits, 'Contraband')
boxen(arrest_fits, 'Arrests')

#%% Print the proportion of officers whose databehavior was described by the single-alternative matching equation 
# with vac greater than 90%
print((round((cite_fits['vac'].ge(0.9).sum()), 5)), "= Citation Proportion >90%")
print((round((search_fits['vac'].ge(0.9).sum()), 5)), "= Search Proportion >90%")
print((round((frisk_fits['vac'].ge(0.9).sum()), 5)), "= Frisk Proportion >90%")
print((round((contra_fits['vac'].ge(0.9).sum()), 5)), "= Contraband Found Proportion >90%")
print((round((arrest_fits['vac'].ge(0.9).sum()), 5)), "= Arrest Proportion >90%")

#%% Print the proportion of officers whose databehavior was described by the single-alternative matching equation 
# with vac greater than 90%
print((round((cite_fits['vac'].ge(0.9).sum())/len(cite_fits), 5)), "= Citation Proportion >90%")
print((round((search_fits['vac'].ge(0.9).sum())/len(search_fits), 5)), "= Search Proportion >90%")
print((round((frisk_fits['vac'].ge(0.9).sum())/len(frisk_fits), 5)), "= Frisk Proportion >90%")
print((round((contra_fits['vac'].ge(0.9).sum())/len(contra_fits), 5)), "= Contraband Found Proportion >90%")
print((round((arrest_fits['vac'].ge(0.9).sum())/len(arrest_fits), 5)), "= Arrest Proportion >90%")

#%% Print the proportion of officers whose databehavior was described by the single-alternative matching equation 
# with vac greater than 80%
print((round((cite_fits['vac'].ge(0.8).sum()), 5)), "= Citation Proportion >80%")
print((round((search_fits['vac'].ge(0.8).sum()), 5)), "= Search Proportion >80%")
print((round((frisk_fits['vac'].ge(0.8).sum()), 5)), "= Frisk Proportion >80%")
print((round((contra_fits['vac'].ge(0.8).sum()), 5)), "= Contraband Found Proportion >80%")
print((round((arrest_fits['vac'].ge(0.8).sum()), 5)), "= Arrest Proportion >80%")

#%% Print the proportion of officers whose databehavior was described by the single-alternative matching equation 
# with vac greater than 80%
print((round((cite_fits['vac'].ge(0.8).sum())/len(cite_fits), 5)), "= Citation Proportion >80%")
print((round((search_fits['vac'].ge(0.8).sum())/len(search_fits), 5)), "= Search Proportion >80%")
print((round((frisk_fits['vac'].ge(0.8).sum())/len(frisk_fits), 5)), "= Frisk Proportion >80%")
print((round((contra_fits['vac'].ge(0.8).sum())/len(contra_fits), 5)), "= Contraband Found Proportion >80%")
print((round((arrest_fits['vac'].ge(0.8).sum())/len(arrest_fits), 5)), "= Arrest Proportion >80%")

#%%####################################################################################################################
# SINGLE-ALTERNATIVE MATCHING FITS
#######################################################################################################################
# Define single alternative matching equation and import packages we'll need to play with it.  
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def single_match(x, k, re):
  return (k*x)/(x+re)

#%% Functions for plots of single officer fits
def overall_plot(i, ):
    # Isolate single officer
    offcr_hash = i
    offcr_A = all_df[all_df['officer_id_hash']==i]
    offcr_A = offcr_A[offcr_A['time'].notna()]
    offcr_A = offcr_A.reset_index()
  
    # Calculate rate of stops per year and rate of citations per year
    offcr_search = offcr_A.groupby(['year'])['search_conducted'].sum()
    offcr_stops = offcr_A.groupby(['year']).size()
  
    try:
      search_per_year = offcr_search / 12
      stops_per_year = offcr_stops / 12

      # Fit the single-alt matching equation to the officer data
      behavior = stops_per_year.values
      reinforcer = search_per_year.values
      c, cov = curve_fit(single_match, reinforcer, behavior) # Fit model
      preds_from_obs = single_match(reinforcer, *c)
      r_2 = r2_score(behavior, preds_from_obs)

      # Create data for plotting the curve predicted by the single-alternative matching
      search_pred = np.linspace(0, search_per_year.max(), 100)
      stop_pred = []
      for j in list(range(len(search_pred))): # Predicted stops
        pred = round(single_match(search_pred[j], c[0], c[1]), 4)
        stop_pred.append(pred)
      
      # Plot behavior (stops) as a function of putative reinforcers (citations)
      plt.figure(figsize=(10, 7.5))
      plt.scatter(x=search_per_year, y=stops_per_year, marker='o', alpha=0.5, \
                  color='black', s=100)
      plt.plot(search_pred, stop_pred, marker='', linestyle='-', color='black')
      plt.xlabel('Searches per Year', fontsize=30)
      plt.ylabel('Stops per Year', fontsize=30)
      plt.title('Officer ID: %s' %i, fontsize =14)
      plt.text(search_per_year.max(), 0, '$R^2$=%s' %'{}'.format(round(r_2, 4)), \
              fontsize=26, horizontalalignment='right')
      plt.xticks(fontsize=20)
      plt.yticks(fontsize=20)
      plt.show()

      # Run the same analysis, but grouped by race
      # Calculate rate of stops per year and rate of citations per year
      offcr_search = offcr_A.groupby(['year', 'subject_race'])['search_conducted'].sum().unstack()
      offcr_stops = offcr_A.groupby(['year', 'subject_race']).size().unstack()
      search_per_year = offcr_search / 12
      stops_per_year = offcr_stops / 12
      search_per_year = search_per_year.fillna(0)
      stops_per_year = stops_per_year.fillna(0)

      # Loop through each race and fit the model
      cols = list(search_per_year)
      race_plot = []
      k_plot = []
      re_plot = []
      r2_plot = []

      for k in cols:
        behavior = stops_per_year[k].values
        reinforcer = search_per_year[k].values
        param_seeds = [16, 5]
        c, cov = curve_fit(single_match, reinforcer, behavior) # Fit model
        preds_from_obs = single_match(reinforcer, *c) # predictions for observed search per month
        r_2 = r2_score(behavior, preds_from_obs) # calculate r^2 values

      # Combine race fits into single df for easier plotting by race
      fits_by_race = pd.DataFrame({"est_k":k_plot, "est_re":re_plot, "r^2":r2_plot, "race":list(search_per_year)})
      
      # Create data for plotting the curve predicted by the single-alternative matching
      search_pred = np.linspace(0, search_per_year.max(), 100)

      # Predictions for Asian/Pacific Islander
      api_pred = []
      try:
        for m in list(range(len(search_pred))):
          pred = single_match(search_pred[m], fits_by_race['est_k'][0], fits_by_race['est_re'][0])
          api_pred.append(pred)
      except:
        print("Officer %s didn't search api" %i)

      # Predictions for Black
      black_pred = []
      try:
        for m in list(range(len(search_pred))):
          pred = single_match(search_pred[m], fits_by_race['est_k'][1], fits_by_race['est_re'][1])
          black_pred.append(pred)
      except:
        print("Officer %s didn't search black" %i)

      # Predictions for Hispanic
      hispanic_pred = []
      try:
        for m in list(range(len(search_pred))):
          pred = single_match(search_pred[m], fits_by_race['est_k'][2], fits_by_race['est_re'][2])
          hispanic_pred.append(pred)
      except:
        print("Officer %s didn't search hispanic" %i)

      # Predictions for White
      white_pred = []
      try:
        for m in list(range(len(search_pred))):
          pred = single_match(search_pred[m], fits_by_race['est_k'][5], fits_by_race['est_re'][5])
          white_pred.append(pred)
      except:
        print("Officer %s didn't search white" %i)

      # Plot behavior (stops) as a function of putative reinforcers (citations)
      plt.figure(figsize=(10, 7.5))

      # Raw Data
      plt.scatter(x=search_per_year['asian/pacific islander'], y=stops_per_year['asian/pacific islander'], marker='o', alpha=0.5, \
                  color='black', s=100, label='Asian/Pacific Islander')
      plt.scatter(x=search_per_year['black'], y=stops_per_year['black'], marker='o', alpha=0.5, \
                  color='blue', s=100, label='Black')
      plt.scatter(x=search_per_year['hispanic'], y=stops_per_year['hispanic'], marker='o', alpha=0.5, \
                  color='red', s=100, label='Hispanic')
      plt.scatter(x=search_per_year['white'], y=stops_per_year['white'], marker='o', alpha=0.5, \
                  color='green', s=100, label='White')
      
      # Prediction Curves
      plt.plot(search_pred, api_pred, marker='', linestyle='-', color='black')
      plt.plot(search_pred, black_pred, marker='', linestyle='-', color='blue')
      plt.plot(search_pred, hispanic_pred, marker='', linestyle='-', color='red')
      plt.plot(search_pred, white_pred, marker='', linestyle='-', color='green')
      plt.plot(search_pred, search_pred, marker='', linestyle='--', color='gray')

      # Details
      plt.xlabel('Searches per Month', fontsize=30)
      plt.ylabel('Stops per Stops', fontsize=30)
      plt.legend(fontsize=20, framealpha=0, bbox_to_anchor=(1, 0.95))
      plt.xticks(fontsize=20)
      plt.yticks(fontsize=20)
      plt.title('Officer ID: %s' %i, fontsize=14)
      plt.savefig('Officer_%s_Fit_by_Race.png' %i)
      plt.show()
  
    except:
      print('Error with officer %s' %i)

#%% Isolate officers with specific fits we're interested in showing

# 99%
ninety_nine = all_fit[(all_fit['fit_type']=='overall') & (all_fit['vac']>0.95)]
ninety_nine_un = ninety_nine['person_num'].unique()
for j in ninety_nine_un:
    overall_plot(i=j)

# 80%

# 60%

# 40%

# 20%

# 0%

#%% Create data for plotting the curve predicted by the single-alternative matching
cites_pred = np.linspace(0, cites_per_day.max(), 100)
stop_pred = []
for j in list(range(len(cites_pred))): # Predicted stops
  pred = round(single_match(cites_pred[j], c[0], c[1]), 4)
  stop_pred.append(pred)

# Plot behavior (stops) as a function of putative reinforcers (citations)
plt.figure(figsize=(10, 7.5))
plt.scatter(x=cites_per_day, y=stops_per_day, marker='o', alpha=0.5, \
            color='black', s=100)
plt.plot(cites_pred, stop_pred, marker='', linestyle='-', color='black')
plt.xlabel('Citations per Day', fontsize=30)
plt.ylabel('Stops per Day', fontsize=30)
plt.title('Officer ID: %s' %i, fontsize =14)
plt.text(cites_per_day.max(), 0, '$R^2$=%s' %'{}'.format(round(r_2, 2)), \
        fontsize=26, horizontalalignment='right')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig('Officer_%s_Overall_Fit.png' %i)
plt.show()


# Plot behavior (stops) as a function of putative reinforcers (citations) and race
plt.figure(figsize=(10, 7.5))

# Raw Data
plt.scatter(x=cites_per_day['asian/pacific islander'], y=stops_per_day['asian/pacific islander'], marker='o', alpha=0.5, \
            color='black', s=100, label='Asian/Pacific Islander')
plt.scatter(x=cites_per_day['black'], y=stops_per_day['black'], marker='o', alpha=0.5, \
            color='blue', s=100, label='Black')
plt.scatter(x=cites_per_day['hispanic'], y=stops_per_day['hispanic'], marker='o', alpha=0.5, \
            color='red', s=100, label='Hispanic')
plt.scatter(x=cites_per_day['white'], y=stops_per_day['white'], marker='o', alpha=0.5, \
            color='green', s=100, label='White')

# Prediction Curves
plt.plot(cites_pred, api_pred, marker='', linestyle='-', color='black')
plt.plot(cites_pred, black_pred, marker='', linestyle='-', color='blue')
plt.plot(cites_pred, hispanic_pred, marker='', linestyle='-', color='red')
plt.plot(cites_pred, white_pred, marker='', linestyle='-', color='green')
plt.plot(cites_pred, cites_pred, marker='', linestyle='--', color='gray')

# Details
plt.xlabel('Citations per Day', fontsize=30)
plt.ylabel('Stops per Day', fontsize=30)
plt.legend(fontsize=20, framealpha=0, bbox_to_anchor=(1, 0.95))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title('Officer ID: %s' %i, fontsize=14)
plt.savefig('Officer_%s_Fit_by_Race.png' %i)
plt.show()
