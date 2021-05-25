          #str int float之间的相互转换
#相互之间可以进行
#强转 int() float() str()
"""
                # int强制类型转换
a = 12.45
i = int(a)
print("a is ",a)
print("int(a) is ", i, type(i))
print("------------------")

#12.25不能转换为int,可以转换为bool(True)
b = input("请您输入 b = ")
i = int(b)
print("type of int(b) is ", type(i))

k = bool(b)
print("type of bool(b) is ", type(k),k)
"""

                # float强制类型转换
a = 12
f = float(a)
print(f)



                # str强制类型转换(任何类型数据转换)
s = str(True)
print(s)

