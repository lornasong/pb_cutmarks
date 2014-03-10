import sys
from PyQt4 import QtGui
import pandas as pd

filename = "df_cutmarks(test).csv"
df = pd.read_csv(filename).transpose
print df