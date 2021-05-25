#1.关于集合的描述以下正确的是（）
'''
a.集合是可变的序列；
b.集合可存储任意数据类型；
c.集合的元素使用分号隔开；
d.集合每个元素都对应一个下标，并且是从0开始的
e.元组不允许重复。
f.集合具有无序性
'''
#a b  f
#集合是可变的
#可存储任意数据类型
#用逗号隔开
#集合没有下标
#元组允许重复
#集合具有无序性

#2.请对集合的几种创建方式进行总结梳理
list1 = [1,2,6,4,5,3]
new_set = set(list1)
print(new_set)

str1 = "string"
new_set = set(str1)
print(new_set)

tuple1 = (1,2,6,4,5,3)
new_set = set(tuple1)
print(new_set)

dics1 = {"青菜":18,"鱼":40}
new_set = set(dics1)
print(new_set)

set1 = {12,33,4,5,6,677}
new_set = set(set1)
print(new_set)


#3.请对集合的基本操作增删改查进行总结

#增
set1 = {12,33,4,5,6,677}
set1.update({44})
set1.add(999)
print(set1)

#删
set1.pop()
set1.remove(677)
print(set1)

#改
set1.update({1918,2000})
set1.update(["33"])
print(set1)

#查
a = "33" in set1
print(a)




#4.请对集合的交、并、差、对称差集进行总结

set1 = {1,2,3,4,5,6,7}
set2 = {2,3,5,7,9,11}
#交
newset = set1.intersection(set2)
newset = set1 & set2
print(newset)
#并
newset = set1.union(set2)
newset = set1 | set2
print(newset)
#差
newset1 = set1.difference(set2)
newset2 = set2.difference(set1)
print(newset1)
print(newset2)

newset3 = set2.symmetric_difference(set1)
print(newset3)


