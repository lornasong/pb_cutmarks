#(travis)
import pandas as pd
import numpy as np
from numpy import *
import pylab

filename = "df_plot(test).csv"
df = pd.read_csv(filename).transpose()

#beginnings of plot that has number of each percentage
#plot_df = df['A2'].value_counts()
#graph = plot_df.plot(kind= 'bar')



#beginnings of plot that has average of each performance level
#this graph has to be dynamic based on adjusted cutmarks
#plot_df2 = df.groupby('PL').aggregate(mean)
#plot_df2.plot(kind= 'bar')
#pylab.show()

#prints first three rows
#print df[:3]