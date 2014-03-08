#Not dynamic version. Specifies file name for pull.
#Using MI A2 Grade 5 ELA PB data extract. Data will require user adjustments due to
#averages outside of interims and cutmark outside of confidence interval

import pandas as pd
import numpy as np
from numpy import *
import pylab

filename = "InterimScoresPB(test).csv"

#Pull csv into dataframe. Column 23: PL, Column 30-37: Raw Scores & Points Possible
df_csv = pd.read_csv(filename, usecols = [23, 30, 31, 32, 33], na_values=['null'])

#Pull a second dataframe with NaN = 0 to calculate Average
df_avg = pd.read_csv(filename, usecols = [30, 31, 32, 33], na_values=['null',])
df_avg[np.isnan(df_avg)] = 0

#Add columns that calculate the %s that will be read into the function
df_csv['A1'] = df_csv['A1 Raw Score']/df_csv['A1 Points Possible']
df_csv['A2'] = df_csv['A2 Raw Score']/df_csv['A2 Points Possible']
df_csv['Avg'] = (df_avg['A1 Raw Score'] + df_avg['A2 Raw Score'])/(df_avg['A1 Points Possible'] + df_avg['A2 Points Possible'])

print df_csv

#Alan
#input: df_csv(columns A1, A2, Avg)
#function: percentile cutmarks (all interims and average)
#function: confidence interval (all interims and average
#output: df_cutmarks: cutmarks and confidence intervals for A1, A2, Avg

#Alan:
#input: df_cutmarks and df_csv
#function: assign proficiencies based on percentile cutmarks (for latest interim) only A2
#ouput:	df_plot (or add into df_csv)
#		list of students' new proficiencies. A2 only

#Lorna:
#check: gaps (if the difference of the two cutmarks is < 1/(points possible)
#	currently not needed to be dynamic: 1/27 for A2
#checks: confidence interval overlapping
#checks: average is between the interim %

#Lorna:
#Userform: A1, A2, Avg cutmarks. A1, A2, Avg confidence intervals
#Buttons: Print / Update / Export
#chart: horizontal bargraph (x: number of students, y: % score distribution in discrete increments)
#chart: vertical bargraph(x: performance level bands, y: % of kids in each band)