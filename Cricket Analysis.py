# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:40:41 2019

@author: vibfr
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





# The Following data processing has been done which is included in the code commented below

# THE ContinousDataset.csv TAKEN FROM KAGGLE HAS BEEN RENAMED TO Match Data.csv AFTER SLIGHT CHANGES

# Data taken from Match Data.csv
# Score Card details for each match has been taken from Score Card.csv file.
# df['Year'] indicates the newly created column extracting only the year from the Match Date column

# Prior to 1984, matches were played of 60 overs or 35-40 overs format with 8 ball per over (nearly 360 balls).
# But since 1984 the One Day International (ODI) matches are played of standard format of 50 overs and 6 balls in each over 
# (300 balls). To account for the change in the format, the scores in the matches prior to 1984 have been multiplied 
# by 5/6 to # to convert the scores equivalent to standard 50 overs format.

# df = pd.read_csv('Match Data.csv')
# score_df = pd.read_csv('Score card.csv')

# print(df.head())
#print(score_df.head())


# df['First innings runs'] = score_df['First innings runs']
# df['Second innings runs'] = score_df['Second innings runs']
# df['year'] = df['Match Date'].str.slice(-5)
# df['year'] = df['year'].astype('int32')

# convert scores in macthes prior to 1984 to standard 50 over format
# for i in df.index:
    # print(df['year'][i])
    # if df['year'][i]==1984:
        # print(i)# index is 220 for matches starting in 1984
        # break

# The data from Match Data.csv and Score card.csv files have been taken and updated and saved in the 
# Match Data Updated.csv which I will use in the program to make visualizations
# df.to_csv('Match Data Updated.csv')


df = pd.read_csv('Match Data Updated.csv')
#print(df.head())

# Remove all matches with first innings score below 100 as they might be a bad day for the teams and does not 
# really indicate the team scoring ability in different years.
# First innings score below 100 is considered an outlier
for i in df.index:
    if df['First innings runs'][i]<100:
        #print(df['First innings runs'][i])
        df.drop(index=i,inplace=True)
  
# Grouping macthes by year
df_by_year = df.groupby('year')
mean_scores = df_by_year.mean()['First innings runs'].values

df_teams = df.groupby(['Host_Country','year'])
df_india = df_teams['First innings runs'].mean()["India"]
india_index = df_india.index
df_australia = df_teams['First innings runs'].mean()["Australia"]
australia_index = df_australia.index

#print(df_india)

for i in range(13):
    mean_scores[i]*=5/6


f = plt.figure(figsize=(15,10))
ax = f.add_subplot(111)
ax.plot(df_by_year.mean()['First innings runs'].index,mean_scores,label="Venues All Over The World")
ax.plot(df_india,label="Indian Cricket Grounds")
ax.plot(df_australia,label="Australian Cricket Grounds")

ax.axhline(y=mean_scores.mean(),c='red')
ax.xaxis.set_ticks(np.arange(1971,2018,2))
for tick in ax.get_xticklabels():
    tick.set_rotation(90)

ax.set_xlabel("Year (1971-2017)",size=12)
ax.set_ylabel("Average Runs In The First Innings",size=12)
#ax2.bar(home_country,df_teams.mean()['First innings runs'])
#plt.axis([1965,2020,100,300])
ax.legend()
ax.set_title("Average First Innings Score vs Average First Innings Score In India And Australia Yearly From 1971-2017")
ax.title.set_fontsize(15)

f.savefig("Average First Innings Scores.png")
#ax2.boxplot(mean_scores)


