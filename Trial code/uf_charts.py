#(travis)
import pandas as pd
import numpy as np
from numpy import *
import pylab

filename = "df_plot(test).csv"
df = pd.read_csv(filename)

#beginnings of plot that has number of each percentage
plot_df = df['A2'].value_counts()
plot_index = plot_df.index
#graph = plot_df.plot(kind= 'bar')

#beginnings of plot that has average of each performance level
#this graph has to be dynamic based on adjusted cutmarks
plot_df2temp = df['PL'].value_counts()
plot_df2 = plot_df2temp/len(df.index)
plot_index2 = plot_df2.index

"""
print plot_df2
print plot_index2
fig, ax2 = pylab.subplots()
ax2.bar(np.arange(4), plot_df2, width = 0.03, color = 'r')
ax2.set_xticks(np.arange(4)+0.03)
ax2.set_xticklabels(plot_index2)
"""
#plot_df2.plot(kind= 'bar')
#pylab.show()