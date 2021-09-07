import os
import pandas as pd
import py2neo
import numpy
# with open('铸钢数据.csv',encoding='utf-8') as temp_f:
#     col_count = [len(l.split(",")) for l in temp_f.readlines()]
# column_names = [i for i in range(max(col_count))]
# df = pd.read_csv('铸钢数据.csv', skip_blank_lines=True,
#                  header=None, names=column_names)
# print(df[0][0])
def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
def main():
    a=0
    data = pd.read_csv("3.csv",header=None)
    print(data)
    # print(len(data[0]))
    #得到所有的去重后的关系列表
    relationList = getUniqueItems(data[0].tolist())
    print(relationList)
    # 创建一个列标签为关系的dataframe对象
    newdata = pd.DataFrame(index=range(0,len(data[0])),columns=range(0,len(relationList)))
    print(len(relationList))
    # newdata[0][0] = data[1][0]
    print(newdata)
    for j in range(0, len(relationList)):
        newdata[j][0] = relationList[j]
    # newdata[]
    for i in range(0,len(data[0])):
        if data[0][i] == relationList[0] :#or data[0][i] == relationList[9]
            a = a+1
        for j in range(0,len(relationList)):
            if data[0][i] == relationList[j]:
                # a = relationList[j]
                newdata[j][a] = data[1][i]
                break
    print(newdata)
    newdata.to_csv('tangang.csv', header=1, index=0, encoding="utf_8_sig", mode='a+')

if __name__ == '__main__':
    main()
