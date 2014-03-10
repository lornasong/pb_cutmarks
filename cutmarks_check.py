#Take test cutmarks and confidence intervals and performs 3 checks on dataframe
#Output: df_check boolean dataframe which identifies errors with TRUE
import pandas as pd
import numpy as np
from numpy import *

#test df_cutmarks
filename = "df_cutmarks(test).csv"
df_cut = pd.read_csv(filename)


#CHECK 1: Is the gap between cutmarks large enough? Assume A1 gap needs to be 1/16 and A2 gap 1/27
#Needs to be dynamic later. Will have to access to df_csv 'possible score' column to check
A1_gap = (df_cut['A1_cut'].diff()*-1) <= float(1)/float(16)
A2_gap = (df_cut['A2_cut'].diff()*-1) <= float(1)/float(24)
#Returns boolean value. Ignore row 0 values (always defaults to 0).
#TRUE in row(n) means that row(n) and row(n+1) are identified as an error - the gap is too small
df_check = pd.DataFrame(data = [A1_gap, A2_gap]).transpose()

#CHECK 2: Is the average cutmark outside of the interim cutmarks?
#This will have to become dynamic for multi-interims to identify min and max cutmarks
#Returns boolean values. TRUE in row(n) means that the row(n) avg cutmark has an error - out of bounds
Avg_mid = ((df_cut.A1_cut < df_cut.Avg_cut) & (df_cut.Avg_cut > df_cut.A2_cut)) | ((df_cut.A1_cut > df_cut.Avg_cut) & (df_cut.Avg_cut < df_cut.A2_cut))
df_check['Avg_mid'] = Avg_mid


#CHECK 3: Do the confidence intervals overlap?
#Note: Lci = Lower Confidence Interval. Uci = Upper Confidence Interval
#Need to check that the Uci of row(n) is smaller than the Lci of row(n+1)
ci = df_cut[['A1_Lci', 'A1_Uci', 'A2_Lci', 'A2_Uci', 'Avg_Lci', 'Avg_Uci']]
shift = ci['A1_Lci'].shift()
A1_overl = ci['A1_Uci'] > shift
shift = ci['A2_Lci'].shift()
A2_overl = ci['A2_Uci'] > shift
shift = ci['Avg_Lci'].shift()
Avg_overl = ci['Avg_Uci'] > shift
#Returns boolean values. Again ignore row 0 values.
#TRUE in row(n) means that the CI in row(n) and row(n+1) are identified as an error - CIs overlap
df_check['A1_overl'] = A1_overl
df_check['A2_overl'] = A2_overl
df_check['Avg_overl'] = Avg_overl

#Make row(n+1) also true if row(n) is true for checks 1 and 3
#Check 1
for i in range(3):
	for j in range(2):
		if df_check.iget_value(i + 1, j) == True:
			df_check.iloc[[i],[j]] = True
		else:
			pass
#Check 3
for i in range(3):
	for j in range(3, 6):
		if df_check.iget_value(i + 1, j) == True:
			df_check.iloc[[i],[j]] = True
		else:
			pass		
print df_check