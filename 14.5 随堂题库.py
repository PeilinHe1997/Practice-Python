'''
1.自定义一个类，类名为Computers，并将这个类放在一个一个computers文件夹中，在这个类中封装几个数学处理的函数
（可以自定义几个关于数学的函数）
尝试创建一个text.py文件，通过这个文件访问调用Computers，模块中的方法。
'''
import computers.Computers as com

c = com.Computers("HUAWEI",1988)
list1 = [33,45,6,6,323]
d = c.rank(list1)
print(d)
'''
2.尝试输出当前如下格式日期：
比如：2019年 12 月12 日
'''
from datetime import datetime
dn = datetime.now()
dns = dn.strftime('%Y年%m月%d日')
print(dns)

'''
3.尝试自我学习random模块
'''
import random
import time
print("---------------开始学习random模块------------")
time.sleep(1)

random.seed(3) 
print("------------随机生成a,b之间的整数-----------")
b = random.randint(3, 9)
print(b,sep = ",")
time.sleep(1)

print("------------随机生成a,b之间的整数,间隔为c-----------")
c = random.randrange(3, 12, 3)
print(c)
time.sleep(1)


print("-----------------随机抽样,population 抽出长度为3的样本----------------")
list1 = [3,45,632,567,333,56]
sample1 = random.sample(list1, 3)
print(sample1)
time.sleep(1)

print("-----------------高斯分布，mu,sigma----------------")
gauss_dist = random.gauss(0, 1)
print(gauss_dist)








