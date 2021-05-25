# 元组的查找操作
'''不能对元组对象进行增删改查的操作，
但是我们可以对元组的整体进行查删、统计、合并的操作
***对元组整体的操作***
'''

# 1、获取元组的单个元素
nations = ("中国","美国","瑞士","印度")
"nations[2] = 12#错误语法"
print(nations[2])

# 2、对元组进行切片；
print(nations[:3])

# 3、判断一个元素是否在该元组中
print("-------------break-------------")
for i in nations:
    if "瑞士" == i:
        print("瑞士漂亮")
        break
    else:
        print("Sorry")

import time
import random
t = random.randint(1,5)
print(t)
time.sleep(t)

print("-------------continue-------------")
for i in nations:
    if "瑞士" == i:
        print("瑞士漂亮")
        continue
    else:
        print("Sorry")
