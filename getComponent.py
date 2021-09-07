import os
import pandas as pd
import py2neo
import numpy
with open('2.csv',encoding='utf-8') as temp_f:
    col_count = [len(l.split(",")) for l in temp_f.readlines()]
column_names = [i for i in range(max(col_count))]
df = pd.read_csv('2.csv', skip_blank_lines=True,
                 header=None, names=column_names)
print(df)
list1 = ['C.max','C.min','Si.max','Si.min','Mn.max','Mn.min','P.max','P.min',
         'S.max','S.min','Cr.max','Cr.min','Ni.max','Ni.min','Mo.max','Mo.min',
         'N.max','N.min','Ti.max','Ti.min','V.max','V.min','Nb.max','Nb.min',
         'B.max','B.min','Co.max','Co.min','更多']
print(len(list1))
component = pd.DataFrame(index=range(0,len(df[0])),columns=list1)
# print(component)
# print(df.loc[0])
a=0
for i in range(0,len(df[0]),3):
    a = i / 3
    for j in range(0,len(df.loc[0])):
        if df[j][i] == 'C':
            component[list1[1]][a]=df[j][i+1]
            component[list1[0]][a] = df[j][i + 2]
        elif df[j][i] == 'Si':
            component[list1[3]][a] = df[j][i + 1]
            component[list1[2]][a] = df[j][i + 2]
        elif df[j][i] == 'Mn':
            component[list1[5]][a] = df[j][i + 1]
            component[list1[4]][a] = df[j][i + 2]
        elif df[j][i] == 'P':
            component[list1[7]][a] = df[j][i + 1]
            component[list1[6]][a] = df[j][i + 2]
        elif df[j][i] == 'S':
            component[list1[9]][a] = df[j][i + 1]
            component[list1[8]][a] = df[j][i + 2]
        elif df[j][i] == 'Cr':
            component[list1[11]][a] = df[j][i + 1]
            component[list1[10]][a] = df[j][i + 2]
        elif df[j][i] == 'Ni':
            component[list1[13]][a] = df[j][i + 1]
            component[list1[12]][a] = df[j][i + 2]
        elif df[j][i] == 'Mo':
            component[list1[15]][a] = df[j][i + 1]
            component[list1[14]][a] = df[j][i + 2]
        elif df[j][i] == 'N':
            component[list1[17]][a] = df[j][i + 1]
            component[list1[16]][a] = df[j][i + 2]
        elif df[j][i] == 'Ti':
            component[list1[19]][a] = df[j][i + 1]
            component[list1[18]][a] = df[j][i + 2]
        elif df[j][i] == 'V':
            component[list1[21]][a] = df[j][i + 1]
            component[list1[20]][a] = df[j][i + 2]
        elif df[j][i] == 'Nb':
            component[list1[23]][a] = df[j][i + 1]
            component[list1[22]][a] = df[j][i + 2]
        elif df[j][i] == 'B':
            component[list1[25]][a] = df[j][i + 1]
            component[list1[24]][a] = df[j][i + 2]
        elif df[j][i] == 'Co':
            component[list1[27]][a] = df[j][i + 1]
            component[list1[26]][a] = df[j][i + 2]
        elif df[j][i] == '更多':
            component[list1[28]][a] = df[j][i + 2]
print(component)
component.to_csv('zhugangcompnent.csv', header=1, index=0, encoding="utf_8_sig", mode='a+')


