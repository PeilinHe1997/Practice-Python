a = 10
print(a)
# print(c) # NameError: name 'c' is not defined

# Error type:
# 1.NameError: 变量名错位，没有定义就使用了
# 2.SyntaxError:语法错误，少了冒号，空格等等
# 3.IO Error:做文件操作的时候遇到异常，一般是找不到文件
# 4.Zero DivisionError:0做除数
# 5.IndentationError:缩进会出现问题，python里面有严格的缩进

# 处理异常
try:
    print(b)
except Exception as e:
    print(e)

try:
    print(b)
except NameError as e:
    print(e)

try:
    print(b)
except NameError:
    print(NameError) # NameError是一个类

# 写了NameError就不能处理其它异常信息了
'''
try:
    a = 10/0 # ZeroDivisionError: division by zero
    print(b)
except NameError as e:
    print(e)
'''
try:
    a = 10/0 # ZeroDivisionError: division by zero
    print(b)
except (NameError,ZeroDivisionError) as e:# 错误类型以元组的方式并列tuple
    print(e)


lists = [12,44,4,5,0,"n",56]
for i in lists:
    print(i)
    try:
        a = 3/i
        print(a)
    except Exception as e:
        print("错误类型",e)
    else:
        print("我在a = ",i,"的时候执行")
    finally:
        print("------------")# 不管有没有错误，finally都会强制执行

# try：可能报错或出现异常的代码
# except Exception as e: 捕获try代码中的异常，Exception就是所捕捉到的异常，e是Exception的小名
# else: 没有异常的时候会执行
# finally: 不管有没有异常都要执行

#### 自定义异常 #####
strs = input("请输入一组带有空格的数字：")
lists = strs.split(" ") #空格是分隔符

if len(lists) >= 5:
    print(lists)
else:
    # 创建异常对象
    e = Exception("列表长度小于5")
    # 抛出异常
    raise e

new_lists = [] #创建空列表
for i in lists:
    try:
        element = int(i)
    except Exception as e:
        print(e)
    else:
        new_lists.append(element)
print(new_lists)
