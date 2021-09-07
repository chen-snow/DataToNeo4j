import pandas as pd
import numpy as np
data = pd.read_csv("data/tangang.csv",header=None)
steeltype = []
print(type(steeltype))
def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
for i in range (0,len(data[0])):
    if data[3][i] is not np.nan:
        res = data[3][i].split( )
        steeltype.extend(res)

steeltype = getUniqueItems(steeltype)
print(steeltype)
