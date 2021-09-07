# Pandas读取文件操作



两个主要的数据结构：Series和DataFrame

**Series**是一种类似于一维数组的对象，它由一维数组（各种numpy数据类型）以及一组与之相关的数据标签（即索引）组成，仅由一组数据即可产生最简单的Series.

Series的字符串表现形式为：索引在左边，值在右边。如果没有为数据指定索引，于是会自动创建一个0到N-1(N为数据的长度)的整数型索引，可以通过Series的**values**和**index**属性获取其数组表现形式和索引对象。

不同于列表，Series可以自己定义索引index,

对series的数据可以使用：索引名.index显示索引名.values显示数据内容

**DataFrame**是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（公用同一个索引）。

```python
 
df['w']  #选择表格中的'w'列，使用类字典属性,返回的是Series类型
df.w    #选择表格中的'w'列，使用点属性,返回的是Series类型
df[['w']]  #选择表格中的'w'列，返回的是DataFrame属性
data[0:2]  #返回第1行到第2行的所有行，前闭后开，包括前不包括后
data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
       #如果采用data[1]则报错  
data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame
```

**两种数据的横向属性是index，而只有DataFrame的columns属性指的是纵向属性**

```python
pd.to_csv()
里面的header默认为1，即保存列索引，设置成0的话便不保存列索引，没有设置成None的选项，设置成它，和设成0一样
index和header一样，它是行索引。
pd.read_csv()
里面的header默认为0，即将读取数据的第一行设置为列索引，header=1，设置读取数据的第二行为列索引。
设置为None,自动添加一个列索引，之前的第一行数据变成DataFrame里的第一行数据。
```

Numpy

[详解](https://www.runoob.com/numpy/numpy-ndarray-object.html)
