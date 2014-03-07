#path: Set-Location C:\Users\lsong\Documents\GitHub\pb_cutmarks
#pull data for cutmarks

#example file name in same folder as .py
filename = ""

#read specific columns into a dataframe
import pandas as pd
import numpy as np
"""
df_t = pd.read_csv(filename, usecols = ['A1 Raw Score', 'A1 Points Possible',
									'A2 Raw Score', 'A2 Points Possible', 'A3 Points Possible'],
									dtype = float, na_values=['null'])


#use print to show data types in csv file.
#All is currently 'objects' so cannot use operations on them
print df_t.dtypes

#adding calculations
df_t['A1_percent'] = df_t['A1 Raw Score']/df_t['A1 Points Possible']
df_t['A2_percent'] = df_t['A2 Raw Score']/df_t['A2 Points Possible']
#df_t['Avg_percent'] = 

#print df_t
"""

#Trial 2
df_2 = pd.read_csv(filename, usecols = [1,2,3])
print df_2


"""
#put csv into a dataframe alternative to above?!
df = pd.DataFrame(data = df_test)
print "_____"
print df

interim = df.('A1 Raw Score') + df.('A2 Raw Score')
print interim

#Attribute:  describe([percentile_width])

"""

#rename column attributes to use for doing calculations on all
#df_t.rename(columns = {'A1 Raw Score' : 'A', 'A1 Points Possible' : 'B'}, inplace = True)


#to declare an array
#array = [interim,  testing]