#Not dynamic version. Specifies file name for pull.
#Using MI A2 Grade 5 ELA PB data extract. Data will require user adjustments due to
#averages outside of interims and cutmark outside of confidence interval

import pandas as pd
import numpy as np
from numpy import *
import pylab

#PULL CSV FOR EXPORTS DATAFRAME: df_csv
csv_filename = "InterimScoresPB(test).csv"
df_csv = pd.read_csv(csv_filename, usecols = [23, 30, 31, 32, 33], na_values=['null'])

#Pull a second dataframe with NaN = 0 to calculate Average
df_avg = pd.read_csv(csv_filename, usecols = [30, 31, 32, 33], na_values=['null',])
df_avg[np.isnan(df_avg)] = 0

#Add columns that calculate the %s that will be read into the function
df_csv['A1'] = df_csv['A1 Raw Score']/df_csv['A1 Points Possible']
df_csv['A2'] = df_csv['A2 Raw Score']/df_csv['A2 Points Possible']
df_csv['Avg'] = (df_avg['A1 Raw Score'] + df_avg['A2 Raw Score'])/(df_avg['A1 Points Possible'] + df_avg['A2 Points Possible'])

#PULL CSV FOR CUTMARKS DATAFRAME: df_cut
cut_filename = "df_cutmarks(test).csv"
df_cut = pd.read_csv(cut_filename, header = 0)

#PREPARING DATA FOR PLOTS
#Number of students that have each percentage level of ANET assessment. This graph will be undynamic
plot_df = df_csv['A2'].value_counts()
plot_index = plot_df.index

#Function for returning and updating dynamic PB plot of stacked bars
def cut_updates(df_cut, df_csv):
	#Prepare to run Proficiency
	curr_cutmark1 = df_cut['A1_cut'].tolist()
	curr_cutmark2 = df_cut['A2_cut'].tolist()
	curr_prof_lvl = ['Advanced', 'Proficient', 'Basic', 'Warning']

	#Add a column for Proficiency.  Run for loop for each prof level. In df_csv
	#A1
	for i in xrange(len(curr_prof_lvl)-1,-1,-1):
		if i ==  len(curr_prof_lvl):
			condition = df_csv['A1'] > 0
			df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]	
		else:
			condition = df_csv['A1'] > curr_cutmark1[i]
			df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]
	#A2
	for i in xrange(len(curr_prof_lvl)-1,-1,-1):
		if i ==  len(curr_prof_lvl):
			condition = df_csv['A2'] > 0
			df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]	
		else:
			condition = df_csv['A2'] > curr_cutmark2[i]
			df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]

	#PREPARING DATA FOR PLOTS

	#% of students in each proficiency level assigned by cutmarks
	#A1
	plot_df1temp = df_csv['A1 Assigned Prof'].value_counts()
	denomA1 = df_csv[pd.notnull(df_csv['A1 Assigned Prof'])]#gets rid of NAN in A1
	plot_df1 = plot_df1temp/len(denomA1)
	#A2
	plot_df2temp = df_csv['A2 Assigned Prof'].value_counts()
	denomA2 = df_csv[pd.notnull(df_csv['A2 Assigned Prof'])]#gets rid of NAN in A2
	plot_df2 = plot_df2temp/len(denomA2)
	#Combine A1 and A2 into 1 frame
	plot12 = pd.DataFrame(index=curr_prof_lvl)
	plot12['A1'] = plot_df1
	plot12['A2'] = plot_df2
	plot12[np.isnan(plot12)] = 0
		
	a = array([plot12.loc['Advanced', 'A1'], plot12.loc['Advanced', 'A2']])
	b = array([plot12.loc['Proficient', 'A1'], plot12.loc['Proficient', 'A2']])
	c = array([plot12.loc['Basic', 'A1'], plot12.loc['Basic', 'A2']])
	d = array([plot12.loc['Warning', 'A1'], plot12.loc['Warning', 'A2']])
	
	return (a, b, c, d, df_csv)