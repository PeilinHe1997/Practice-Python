'''
在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，
并且在外函数的返回值是内函数的引用。这样就构成了一个闭包
'''
#step1:嵌套函数
'''
def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(10)
    inner()
outer()
'''
#step2:返回函数
'''
def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(10)
    return inner

test = outer()#输出20
test()#输出10
'''
#step3:闭包

def outer():
    b = 20
    print(b)
    def inner():
        a = 10
        print(a+b)
    return inner

test = outer()#输出20
test()












