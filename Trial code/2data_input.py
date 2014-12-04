#Not dynamic version. Specifies file name for pull.
#Using MI A2 Grade 5 ELA PB data extract. Data will require user adjustments due to
#averages outside of interims and cutmark outside of confidence interval

import pandas as pd
import numpy as np
from numpy import *
import pylab
import matplotlib.pyplot as plt


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


#Prepare to run A1 and A2 Proficiency
curr_cutmarkA1 = df_cut['A1_cut'].tolist()
curr_cutmarkA2 = df_cut['A2_cut'].tolist()
curr_prof_lvl = ['Advanced', 'Proficient', 'Basic', 'Warning']

#Add a column for A1 and A2 Proficiency.  Run for loop for each prof level. In df_csv
for i in xrange(len(curr_prof_lvl)-1,-1,-1):
	if i ==  len(curr_prof_lvl):
		condition = df_csv['A1'] > 0
		df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]	
	else:
		condition = df_csv['A1'] > curr_cutmarkA1[i]
		df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]

for i in xrange(len(curr_prof_lvl)-1,-1,-1):
	if i ==  len(curr_prof_lvl):
		condition = df_csv['A2'] > 0
		df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]	
	else:
		condition = df_csv['A2'] > curr_cutmarkA2[i]
		df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]

#PREPARING DATA FOR PLOTS
#Number of students that have each percentage level of ANET assessment. This graph will be undynamic
plot_df = df_csv['A2'].value_counts()
plot_index = plot_df.index

#% of students in each proficiency level assigned by cutmarks

plot_dfA1temp = df_csv['A1 Assigned Prof'].value_counts()
denomA1 = df_csv[pd.notnull(df_csv['A1 Assigned Prof'])]#gets rid of NAN in A1
plot_dfA1 = plot_dfA1temp/len(denomA1)
plot_indexA1 = plot_dfA1.index
plot_dfA2temp = df_csv['A2 Assigned Prof'].value_counts()
denomA2 = df_csv[pd.notnull(df_csv['A2 Assigned Prof'])]#gets rid of NAN in A2
plot_dfA2 = plot_dfA2temp/len(denomA2)
plot_indexA2 = plot_dfA2.index
#prepare for stacked bar chart
a = [plot_dfA1['Advanced'], plot_dfA2['Advanced']]
b = [plot_dfA1['Proficient'], plot_dfA2['Proficient']]
c = [plot_dfA1['Basic'], plot_dfA2['Basic']]
d = [plot_dfA1['Warning'], plot_dfA2['Warning']]


def cut_updates(df_cut, df_csv):

	curr_cutmarkA1 = df_cut['A1_cut'].tolist()
	curr_cutmarkA2 = df_cut['A2_cut'].tolist()
	curr_prof_lvl = ['Advanced', 'Proficient', 'Basic', 'Warning']

	#Add a column for A1 and A2 Proficiency.  Run for loop for each prof level. In df_csv
	for i in xrange(len(curr_prof_lvl)-1,-1,-1):
		if i ==  len(curr_prof_lvl):
			condition = df_csv['A1'] > 0
			df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]	
		else:
			condition = df_csv['A1'] > curr_cutmarkA1[i]
			df_csv.loc[condition, 'A1 Assigned Prof'] = curr_prof_lvl[i]

	for i in xrange(len(curr_prof_lvl)-1,-1,-1):
		if i ==  len(curr_prof_lvl):
			condition = df_csv['A2'] > 0
			df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]	
		else:
			condition = df_csv['A2'] > curr_cutmarkA2[i]
			df_csv.loc[condition, 'A2 Assigned Prof'] = curr_prof_lvl[i]

	#UPDATE Dynamic plot
	#% of students in each proficiency level assigned by cutmarks
	nplot_dfA1temp = df_csv['A1 Assigned Prof'].value_counts()
	ndenomA1 = df_csv[pd.notnull(df_csv['A1 Assigned Prof'])]#gets rid of NAN in A1
	nplot_dfA1 = nplot_dfA1temp/len(ndenomA1)

	nplot_dfA2temp = df_csv['A2 Assigned Prof'].value_counts()
	ndenomA2 = df_csv[pd.notnull(df_csv['A2 Assigned Prof'])]#gets rid of NAN in A2
	nplot_dfA2 = nplot_dfA2temp/len(ndenomA2)

	#prepare for stacked bar chart
	na = [nplot_dfA1['Advanced'], nplot_dfA2['Advanced']]
	nb = [nplot_dfA1['Proficient'], nplot_dfA2['Proficient']]
	nc = [nplot_dfA1['Basic'], nplot_dfA2['Basic']]
	nd = [nplot_dfA1['Warning'], nplot_dfA2['Warning']]
	
	return (na, nb, nc, nd, df_csv)
	
