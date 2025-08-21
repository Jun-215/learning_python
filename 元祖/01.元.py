"""
Tuple 是 Python 中用于存储集合的 4 种内置数据类型之一data，其他 3 种是 List、Set 和 Dictionary，它们都具有不同的质量和用法。

元组是一个有序且不可更改的集合。

元组用圆括号书写。


元组项
元组项是有序的、不可更改的，并且允许重复的值。
元组项是索引的，第一个项目有索引，第二个项目有索引，等等。[0][1]

"""

# 要创建一个只有一个项目的元组，您必须在该项目后添加一个逗号， 否则 Python 不会将其识别为元组。
thistuple = ("apple",)
thistuple2 = ("apple")
print(type(thistuple))
print(type(thistuple2))

"""
<class 'tuple'>
<class 'str'>
"""

# 元组的数据类型是<class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))