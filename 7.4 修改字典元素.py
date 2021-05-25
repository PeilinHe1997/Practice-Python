#1、通过赋值修改字典元素
dics = {"a":33, "b":57, "c":89}
print(dics["a"])
dics.setdefault("d",1339)
dics["b"] = 999999
print(dics)


#2、通过update函数实现对键值对更新；+和extend都不行
up_dics = {"e":78,"f":23}
dics.update(up_dics)
print(dics)
