# python 变量与作用域
'''
1、局部变量：定义在函数中，作用域是在函数内部
2、全局变量：定义在函数外，在全局都可以使用
3、global关键字
'''
#局部变量

def func():
    a = 1
    print(a)

func()

#全局变量
a = 12
def func():
    a = 200
    print(a+23)

func()
print(a)

#当内部作用域想修改外部作用域变量时，需要用到global 关键字


a = 12
def func():
    global a
    a = 200
    print(a+23)

func()
print(a)




















