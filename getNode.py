import pandas as pd
import numpy as np
data = pd.read_csv("zhugangcompnent.csv",header=None)
startid = 0

print(data)
print(data.shape[1])
print(len(data[0]))
for i in range(0,data.shape[1]):
# for i in range(0, 1):
    newdata = pd.DataFrame(index=range(0, len(data[0])), columns=['index:ID', 'name', ':LABEL'])
    a = 0
    for j in range(1,len(data[0])):
        if data[i][j] is not np.nan:
            newdata['index:ID'][a] = j
            newdata['name'][a] = data[i][j]
            newdata[':LABEL'][a] = data[i][0]
            a = a + 1
    newdata.to_csv(data[i][0]+'.csv', header=1, index=0, encoding="utf_8_sig", mode='a+')
