# 查找字典元素

#1、通过指定键查找对应值
dics = {"小张":23,"小明":46,"小王":17}
print(dics["小张"])

#2、通过get函数查找对应的值
age = dics.get("小张")
print(age)

#3.1、判断字典的键是否存在
if "小张" in dics.keys():
    print("存在")
else:
    print("不存在")


#3.2、判断字典的值是否存在
if 17 in dics.values():
    print("存在")
else:
    print("不存在")
