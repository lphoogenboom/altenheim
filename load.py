import pandas as pd
import numpy as np

# [Sex , Age , CDR , MMSE , diagnosis]
test = pd.read_csv('OASIS_data.csv')

# Some CDR NaN because in prior assesment, altzheimers was sufficiently disproven.
# Because CDR was not required, it is safe to assume there is no AD, so 0 is appropriate.
test = test.fillna(0)

#print(test.head())

#print(test.loc[0,'CDR'])

maxCDR = test['CDR'].max()
cnCount = test['CDR'].value_counts()[0]
adCount = test['CDR'].value_counts()[1]
sadCount = test['CDR'].value_counts()[2]
print("No AD: "+str(cnCount)+"  |  "+"Mild AD: "+str(adCount)+"  |  "+"Severe AD: "+str(sadCount))
print("With total: "+str(test["CDR"].size))

mmsScores = np.zeros(31)
for i in range(0,377):
    val = int(test.iloc[i, 3])
    print(val)
    mmsScores[val] += 1
print(mmsScores)


"""
maxCDR = test['MMS'].max()
cnCount = test['MMS'].value_counts()[1]
adCount = test['MMS'].value_counts()[10]
sadCount = test['MMS'].value_counts()[30]
print("No AD: "+str(cnCount)+"  |  "+"Mild AD: "+str(adCount)+"  |  "+"Severe AD: "+str(sadCount))
print("With total: "+str(test["CDR"].size))
"""