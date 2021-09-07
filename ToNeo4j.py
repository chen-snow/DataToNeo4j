import numpy as np
from py2neo import Graph, Node, Relationship
import pandas as pd
# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("http://localhost:7474", username="neo4j", password='1234')
# graph.delete_all() #清除neo4j中原有的结点等所有信息

# 创建结点
data = pd.read_csv("zhugang.csv",header=None)
print(data[0][88])

# print(data[0])
# for i  in  range(1,len(data)):
#     if data[0][i] is not np.nan :
#         node = Node('brand',name = data[0][i])
#         graph.create(node)
    # node1 = Node('EuropeanStandardBrand',name = data[i][1])
    # node2 = Node('standard',name = data[i][2])
    # node3 = Node('type',name = data[i][3])
    # node4 = Node('property',name = data[i][4])
    # node5 = Node('label',name = data[i][5])
    # node6 = Node('explain',name = data[i][6])
    # node7 = Node('Oldbrand',name = data[i][7])
    # node8 = Node('W-Nr',name = data[i][8])
    # node9 = Node('UNS', name=data[i][8])
    # node10 = Node('OtherBrand', name=data[i][8])
    # for j in range(0,11):
    #     graph.create('node'+str(j))
