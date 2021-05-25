#a=input()
a = 12 #a为变量名，12为整型数据， =赋值
#变量名：字母、下划线、数字（不在开头），不能以关键字作为变量名（FALSE）,
#不能以内置函数名作为变量

a = input()#用户输入数据，将数据赋值给变量
print(a)


a = input("请您输入")
print(a)
print(type(a))#所有输入都是字符串类型
#<class 'str'>
#print(a+12)#报错


#随堂题库

#1. 编写一个程序，提示用户输入，并获取用户输入，
#   并给返回的数据赋值，判断这个数据是什么数据类型
print("第一题：")
a=input("请输入")
print(type(a))

#2.以下变量的命名中哪一个命名是正确的?
#  True = 12    abs = 14    23name = "12"
# input_str = "小明"    _name = "Tony"

#答案：input_str = "小明"

