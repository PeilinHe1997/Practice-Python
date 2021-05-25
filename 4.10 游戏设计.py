# case:猜数字游戏


#random
'''random：一个产生随机数的函数
randint(10,20):随机生成10-20之间的随机整数
uniform(10,20):随机生成10-20之间的随机浮点数
random():随机生成01之间的随机浮点数
'''

#time
'''
time:模块提供各种时间相关的功能
time.sleep(secs) 让程序休眠多少秒
'''

import random
import time
print("----------------猜数字游戏-------------")
time.sleep(1)
print("----------------开始啦-------------")
for i in range(3):
    time.sleep(1)
    print(str(i+1))
num = random.randint(0,9)
print("随机数已经出现了")
for i in range(3):
    a = int(input("请输入您所猜的数字"))
    if a > num:
        print("您猜大了")
    elif a < num:
        print("您猜小了")
    else:
        print("恭喜您猜测对了，您真聪明")
        break


















