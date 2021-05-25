# 集合的基本运算——交并差

#交运算
'''intersection()函数/&符号'''
set1 = {"12","34","345","11","16"}
set2 = {"122","34","5","11","289"}

new_set = set2.intersection(set1)
new_set = set1 & set2
print(new_set)


#并运算
'''union()函数或者|符号'''
new_set = set2.union(set1)
new_set = set1 | set2
print(new_set)


#差运算
'''difference() : set2 - set2&set1'''
'''symmetric_difference(): set1 + set2 - 2*set2&set1'''
new_set = set2.difference(set1)
new_set2 = set2.symmetric_difference(set1)
print(new_set)
print(new_set2)
