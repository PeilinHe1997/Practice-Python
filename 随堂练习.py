#1.判断以下代码的运行结果是（    ）
'''
a=[1,2,3,4]

def func():

　　a = [5,6,7,8]

func()
print(a)
'''
#A [1,2,3,4]   B  [5,6,7,8]
'''A'''

#2.判断以下代码的运行结果是（   ）
'''
a=[1,2,3,4]

def func():
    a.extend([5,6,7,8])

func()
print(a)
'''
#A [1,2,3,4]   b  [5,6,7,8]  c [1, 2, 3, 4, 5, 6, 7, 8]
'''
c:列表是不可变数据类型。属于引用传递
引用传递，在函数里进行值得修改,源对象也会被修改。
'''

#3.编写一个函数嵌套使用的案例


#4.递归求sum = n+(n-1)+(n-2)+(n-3)...1的和
#  递归求n!=1×2×3×...×(n-1)n阶乘
def multi(n):
    if n == 1:
        return 1
    else:
        return n * multi(n-1)
print(multi(5))
def summ(n):
    if n == 1:
        return 1
    else:
        return n + summ(n-1)
print(summ(3))


#5.将以下if—else条件判断更改为三元运算，并将其封装为一个匿名函数

a = 12
b = 23
if a>b:
    print(a)
else:
    print(b)

func1 = lambda a,b:print(a) if a > b else print(b)
f = func1(12,23)

#6.对闭包函数进行总结，尤其是闭包函数和嵌套函数和返回函数之间有哪些区别

#嵌套函数
print("---------------------嵌套函数---------------------")
def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(10)
    inner()

outer()

#返回函数
print("---------------------返回函数---------------------")
def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(10)
    return inner

test = outer()
test()

#闭包
print("---------------------闭包---------------------")
def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(a+b)
    return inner

test = outer()#输出20
test()










