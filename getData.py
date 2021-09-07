import pandas as pd
import numpy as np
import csv
# url = 'http://www.caishuku.com/material/detail_2832.html'
# tb = pd.read_html(url)[0]
# print(tb)
# tb1 = pd.read_html(url)[1]
# tb.to_csv('2.csv', header=1,index=0,encoding="utf_8_sig",mode='a+')
# tb.to_csv('3.csv', encoding="utf_8_sig",header=None, index=False)
# data = pd.read_csv('铸钢数据.csv')
# print(data)
# print(data[1].tolist())
def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
start_url='http://www.caishuku.com/material/detail_'
data_1 = pd.read_csv("data/碳钢牌号.csv",usecols=["0"])
data = data_1['0'].tolist()
print(len(data))
data2 = pd.read_csv("3.csv",header=None)
relationList = getUniqueItems(data2[0].tolist())
newdata = pd.DataFrame(index=range(0,1),columns=range(0,len(relationList)))
print(relationList)

# for j in range(0, len(relationList)):
#     newdata[j][0] = relationList[j]
for i in range(198,len(data)):
    url = start_url + str(data[i]) + '.html'
    tb = pd.read_html(url)[0]
    for k in range(0, len(tb[0])):
        for s in range(0, len(relationList)):
            if tb[0][k] == relationList[s]:
                newdata[s][0] = tb[1][k]
            # else:
            #     newdata[s][0] = np.nan
    newdata.to_csv('6.csv', header=0, index=0, encoding="utf_8_sig", mode='a+')
    newdata.loc[0] = np.nan
    print(i)