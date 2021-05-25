'''
a = 1000
#Exception是某一类异常
try:
    print(b)
except Exception as e:
    print(e)

#NameError是某一个异常  
try:
    print(b)
except NameError as e:
    print(e)

try:
    print(b)
except NameError:
    print(NameError)


try:
    a = 100/0
    print(b)
except (NameError,ZeroDivisionError) as e:
    print(e)
'''

#处理异常

"""
try:
可能或报错或者出现异常的代码

except Exception as e:
捕获try代码中的异常，Exception就是所捕获到的异常，e是Exception的小名

else:
没有异常的时候会执行

finally:
不管有没有异常都要执行

"""
lists = [12,44,55,66,0,8,"n"]
for i in lists:
    print(i)
    #什么时候都会执行
    try:
        a = 3/i
        print(a)
    #有错误信息才会执行
    except Exception as e:
        print(e)
    #正确的时候执行
    else:
        print("我什么时候执行")
    #什么时候都会强制执行
    finally:
        print("----------")








        
