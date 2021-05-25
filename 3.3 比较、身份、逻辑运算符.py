#一、比较运算符
'''
==
!=
>
<
>=
<=
结果返回值为True/False
'''
a = 10
b = 5
'''两个符号之间不能有空格'''
i = (a == b)
print(i)
i = (a != b)
print(i)
i = (a > b)
print(i)
print("------------------")

#二、身份运算符
'''
is is表示是否为引用同一个对象（同一个id）
== 表示两边的值是否一样
'''
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
print("id(a) is ",id(a))
print("id(b) is ",id(b))

c = 90
d = 90
print(c is d)

e = [1,2,3]
f = e
print(e is f)
print("------------------")

#三、逻辑运算符
'''
and 同真则真
or 一真则真
not 不真则假
'''
print("1",True and True)
print("2",True and False)
print(2<4 and 3>5)

print(not 2<4)













