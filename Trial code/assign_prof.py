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
df_avg = pd.read_csv(filename, usecols = [30, 31, 32, 33], na_values=['null',])
df_avg[np.isnan(df_avg)] = 0

#Add columns that calculate the %s that will be read into the function
df_csv['A1'] = df_csv['A1 Raw Score']/df_csv['A1 Points Possible']
df_csv['A2'] = df_csv['A2 Raw Score']/df_csv['A2 Points Possible']
df_csv['Avg'] = (df_avg['A1 Raw Score'] + df_avg['A2 Raw Score'])/(df_avg['A1 Points Possible'] + df_avg['A2 Points Possible'])

print df_csv

#PULL CSV FOR CUTMARKS DATAFRAME: df_cut

cut_filename = "df_cutmarks(test).csv"
df_cut = pd.read_csv(cut_filename, header = 0)


#ASSIGN PROFICIENCY TO A2 ADD ANOTHER COLUMN FOR PERFORMANCE LEVELS