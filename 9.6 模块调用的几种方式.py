'''
四种调用方式
1. import random        import + 模块名
2. import random as r   import + 模块名+as+变量名
3. from random import randint   from + 模块名 + import + 函数名
4. from random import *         from + 模块名 + import + 星号       (导入所有函数)
'''
#当math_module在另一个文件夹时，使用以下方法：
import sys
sys.path.append(r"C:\Users\84021\Desktop\自学\Python.le\第九章 函数")


list1 = [123,45,66,78,90]

import math_module
new_list = math_module.oushu_list(list1)
print(new_list)

import math_module as m
new_list = m.oushu_list(list1)
print(new_list)

from math_module import oushu_list
new_list = oushu_list(list1)
print(new_list)


from math_module import *
new_list = soap_rank(list1)
print(new_list)


