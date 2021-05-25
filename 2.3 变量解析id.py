#变量书写规范：
# = 两边加空格

num = 12 #num 变量名；= 赋值符号；12数值
         #开辟内存空间"12"，num指向12
print("num=12",id(num))#变量的内存地址，唯一

num = 23#开辟新的内存空间"23" ，num指向23

print("num=23",id(num))

''' 多行注释
a = 90
b = a #b指向90
'''

""" 多行注释
b = 23
print(a)
print(b)

"""

a = b = c = d = 90 #a,b,c,d全部指向90的id(内存)
print("when a = b = c = d = 90",id(a),id(b),id(c),id(d))


#随堂练习
'''
4.下列函数将会有怎样的输出，并绘制内存地址图。
a = "hello"
b = a
c = b
c = "世界"
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))
'''
a = "hello"
b = a
c = b
c = "世界"
print(a)#hello
print(id(a))
print(b)#hello
print(id(b))
print(c)#世界
print(id(c))
#a和b的id相同
