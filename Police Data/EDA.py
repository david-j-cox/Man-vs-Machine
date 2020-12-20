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
sys.path.append('C:/Users/David-PC/Dropbox/Coding/Local Python Modules/')

#% Set working directory
os.chdir('C:/Users/David-PC/Dropbox/Projects/CurrentProjectManuscripts/Empirical/PersonalFun/Matching & Police Behavior/Data')

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Read in the data
nash_raw_data = pd.read_csv('tn_nashville_2020_04_01.csv', low_memory=False)
nash_data = nash_raw_data.copy()
list(data)
len(data)

#%% Run Pandas Profiling
from pandas_profiling import ProfileReport
profile = ProfileReport(nash_data, title="Nashville EDA", explorative=True)
profile.to_widgets()

#%% Save profile report to an html file
profile.to_file("Nashville_Policing_Initial_EDA.html")

#%% Plot the number of times different races were pulled over. 
import matplotlib.pyplot as plt
import seaborn as sns

race_counts = data.subject_race.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(race_counts.index, race_counts.values, color='black')
plt.title('Nashville, TN (2010-2019)')
plt.ylabel("Number of Stops (Total = %s)" %len(data), fontsize=16)
plt.xlabel('Race', fontsize=16)
plt.show()

#%% Add census data to the df
race_counts = pd.DataFrame(race_counts)
race_counts.columns = ['Stops']
race_counts['Demographics'] = [0.6316, 0.2788, 0.1654, 0.0355, 0.00, 0.0282]

#%% Plot proportion stops with different races compared to 2019 census data
plt.figure(figsize=(10,5))
barWidth = 0.3
r1 = np.arange(len(race_counts))
r2 = [x + barWidth for x in r1]
plt.bar(r1, (race_counts.Stops)/len(data), width=barWidth, color='black', edgecolor='black', label='Proportion Police Stops')
plt.bar(r2, race_counts.Demographics, width=barWidth, color='gray', edgecolor='black', label='Proportion 2018 Census')
plt.title('Nashville, TN (2010-2019)')
plt.xticks([r + barWidth for r in range(len(race_counts))], race_counts.index)
plt.ylabel("Proportion of Stops or Population", fontsize=16)
plt.xlabel('Race', fontsize=16)
plt.ylim(0, 1)
plt.legend()
plt.show()

#%% Plot the number of times different sexes were pulled over. 
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

#%% Pull the officer with the most observations to run analyses with
print(data.officer_id_hash.value_counts())
ofcr_a = data.loc[data['officer_id_hash']=='b5ca91d71f']
print('Officer b5ca91d71f pulled over', len(ofcr_a), 'people between', min(ofcr_a.date), 'and', max(ofcr_a.date))

#%% Same plots of race by Officer 'A'
race_props = (ofcr_a.subject_race.value_counts())/len(ofcr_a)
plt.figure(figsize=(10,5))
sns.barplot(race_props.index, race_props.values, color='black')
plt.title('Nashville, TN (2010-2012)')
plt.ylabel('Stops by Officer b5ca91d71f', fontsize=16)
plt.xlabel('Race', fontsize=16)
plt.ylim(0,1)
plt.show()

#%% Create lists of sums of every 50 row for citations issued
citation_data = ofcr_a.citation_issued.reset_index()
citation_data = citation_data.drop(['index'], axis=1)
citation_data = [1 if i==True else 0 for i in citation_data.citation_issued]
citation_data = pd.DataFrame(citation_data)
citation_data = citation_data.groupby(citation_data.index // 50).sum()
citation_data.describe()

#%% Plot it
plt.figure(figsize=(10,5))
sns.distplot(citation_data, bins=15, color='black')
plt.title('Officer b5ca91d71f')
plt.ylabel('Proportion of 50 Stop Bins', fontsize=16)
plt.xlabel('Number of Citations', fontsize=16)
plt.show()

#%% Create a probability that the officer searches someone
search_data = ofcr_a.search_conducted.reset_index()
search_data = search_data.drop(['index'], axis=1)
search_data = [1 if i==True else 0 for i in search_data.search_conducted]
search_data = pd.DataFrame(search_data)
search_data.columns = ['Num_Searches']
search_data = search_data.groupby(search_data.index // 815).sum()
search_data.describe()

#%% Create a probability that the officer finds contraband
contraband_data = ofcr_a.contraband_found.reset_index()
contraband_data = contraband_data.drop(['index'], axis=1)
contraband_data = [1 if i==True else 0 for i in contraband_data.contraband_found]
contraband_data = pd.DataFrame(contraband_data)
contraband_data.columns = ['Num_Contra_Found']
contraband_data = contraband_data.groupby(contraband_data.index // 815).sum()
contraband_data.describe()

#%% Combine search and contraband data
search_and_find = pd.concat([search_data, contraband_data], axis=1)
search_and_find
#%% Create ratio data
search_and_find['search_plot'] = search_and_find.Num_Searches/50

contra_add = []

for i in list(range(len(search_and_find))):
    if search_and_find.Num_Searches[i] == 0:
        contra_add.append(0)
    elif search_and_find.Num_Contra_Found[i] == 0:
        contra_add.append(0)
    else:
        num = round(search_and_find.Num_Contra_Found[i]/search_and_find.Num_Searches[i], 2)
        contra_add.append(num)

search_and_find['contra_plot'] = contra_add

search_and_find
#%% Plot scatter of search count as a function of contraband found
plt.figure(figsize=(5,5))
sns.regplot(x=search_and_find['contra_plot'], y=search_and_find['search_plot'])
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('Prop. of Searches with Contraband', fontsize=16)
plt.ylabel('Prop. of Stops with Search', fontsize=16)
plt.show()