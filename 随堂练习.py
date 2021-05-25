#1.输出打印以下*号的造型，并将其封装为函数
'''
*****
****
***
**
*
'''
print("-------------------第一题-------------")
def print_star():
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end = "")
        print("\t")

print_star()

#2、分别对无参函数、有参函数、返回值函数进行总结
'''
无参函数：没有参数 def max_num()
有参函数：def max_num(a,b)
返回值函数：def max_num(a,b)：
                if a > b:
                    return a
                else:
                    return b
'''

#3、模块的调用有4种方式，请你尝试将冒泡排序和选择排序进行封装，
#然后分别使用模块调用的4种方式进行调用使用模块和函数。

print("-------------------第三题-------------")
list1 = [12,23,56,77,68]
'''
import rank as r
m = r.soap_rank(list1)
print(m)
'''

'''
from rank import choose_rank 
m = choose_rank(list1)
print(m)
'''

'''
from rank import * 
m = choose_rank(list1)
print(m)
'''

import rank
m = rank.soap_rank(list1)
print(m)

#4、对参数多种传递方式进行总结。
print("-------------------第四题-------------")
def max_num(a,b):
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b
     # 位置传参        
m = max_num(12,3)

     #关键字传参(无需考虑参数位置)
K = max_num(b = 13, a = 45)

     #默认值传参
'''第一位不能使用默认值传参'''
def max_num(a,b = 45):
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b
n = max_num(13)

     #可变参数
'''一个*被自动组装为元组，两个**被自动组装为字典'''

def animals(*name):
    print(name)
    print(type(name))
    str_name = ""
    for i in name:
        str_name += i
    return str_name

str_name = animals("小可爱","小笨蛋")
print(str_name)


def animals(**name):
    print(name)
    print(type(name))
    
animals(name1 = "小可爱",name2 = "小笨蛋",name3 = "小苹果")

#5、值传递、引用传递（数据类型的可变和不可变进行总结）
'''
可变：list; dic;
不可变: int; str; tuple
'''
#6、获取用户输入的三角形的三条边，判断能否构成三角形？
print("-------------------第6题-------------")

def if_sanjiaoxing():
    a = float(input("请输入第1条边长"))
    b = float(input("请输入第2条边长"))
    c = float(input("请输入第3条边长"))
    if a + b > c and a + c > b and b + c > a:
        print("可以构成三角形")
    else:
        print("不可以构成三角形")
if_sanjiaoxing()
    


