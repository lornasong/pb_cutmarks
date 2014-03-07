#Not dynamic version. Specifies file name for pull.
#Using MI A2 Grade 5 ELA PB data extract. Data will require user adjustments due to
#averages outside of interims and cutmark outside of confidence interval

import pandas as pd
import numpy as np
from numpy import *
import pylab

filename = "InterimScoresPB(test).csv"

#Pull csv into dataframe. Column 23: PL, Column 30-37: Raw Scores & Points Possible
df = pd.read_csv(filename, usecols = [23, 30, 31, 32, 33], na_values=['null'])

#Pull a second dataframe with NaN = 0 to calculate Average
df_avg = pd.read_csv(filename, usecols = [30, 31, 32, 33], na_values=['null'])
df_avg[np.isnan(df_avg)] = 0

#Add columns that calculate the %s that will be read into the function
df['A1'] = df['A1 Raw Score']/df['A1 Points Possible']
df['A2'] = df['A2 Raw Score']/df['A2 Points Possible']
df['Avg'] = (df_avg['A1 Raw Score'] + df_avg['A2 Raw Score'])/(df_avg['A1 Points Possible'] + df_avg['A2 Points Possible'])

print df

#function: percentile cutmarks (all interims and average)
#function: confidence interval (all interims and average
#df_output: cutmarks and confidence intervals

#function: assign proficiencies based on percentile cutmarks (for latest interim)
#df_plot: list of students new proficiencies & latest interim %

#check: gaps (if the difference of the two cutmarks is < 1/(points possible)
#	currently not needed to be dynamic: 1/27 for A2
#checks: cutmark between CI
#checks: average is between the interim %

#chart: horizontal bargraph (x: number of students, y: % score distribution in discrete increments)
plot_df = df['A1'].value_counts()
plot_df.plot(kind= 'bar')
pylab.show()
#chart: vertical bargraph(x: performance level bands, y: % of kids in each band)

#print out userform