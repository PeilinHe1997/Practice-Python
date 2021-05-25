'''集合（set）可变的序列，可以存贮各种数据类型，具有无序性和不重复性'''
#创建集合
#创建空集合

empty = set()
print(empty)
#基于字符串
str_set = set("我喜欢python我py")
print(str_set)
'''集合是无序的,不重复的（自动去重）'''

#基于元组
tuple_set = set((12,14,23,455))
print(tuple_set)


#基于列表
list_set = set([12,14,23,455])
print(list_set)


#基于集合
set1 = {12,14,23,455}
print(set1)
print(id(set1))
new_set = set(set1)
print(id(new_set))
print(new_set)
