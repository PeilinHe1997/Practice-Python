#1、使用del函数删除
dics = {"小张":"天蝎座","小明":"双鱼座","小王":"双子座","小刘":"金牛座"}
list1 = ["天蝎座","双鱼座","双子座","金牛座"]
del(dics["小张"])
del list1[0]
print("dics is :",dics)
print("list1 is :",list1)

#2、使用pop()函数删除
dics = {"小张":"天蝎座","小明":"双鱼座","小王":"双子座","小刘":"金牛座"}
list1 = ["天蝎座","双鱼座","双子座","金牛座"]
dics.pop("小张")
list1.pop(0)
list1.remove("双子座")
print("dics is :",dics)
print("list1 is :",list1)

#3、使用popitem()函数删除：最后一个键值对

dics = {"小张":"天蝎座","小明":"双鱼座","小王":"双子座","小刘":"金牛座"}
dics.popitem()
print("dics is :",dics)

#4、使用clear()函数删除
dics = {"小张":"天蝎座","小明":"双鱼座","小王":"双子座","小刘":"金牛座"}
list1 = ["天蝎座","双鱼座","双子座","金牛座"]
dics.clear()
list1.clear()
print("dics is :",dics)
print("list1 is :",list1)
