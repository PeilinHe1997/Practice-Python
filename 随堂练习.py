#1.程序包括哪三种基本结构？
'''分支结构；循环结构；顺序结构'''

#2、python基础语法中是如何进行缩进的？
'''一个table键相当于4个空格'''

#3、写出elif是如何进行演变出来的？并将它演变的过程通过代码梳理出来。
'''课堂上得
if 条件：
else:
    if 条件：
    else:
        '''
#转换为：
'''
if 条件：
elif 条件：
elif 条件：
else:
'''
a = 10
b = int(input())
if a > b:
    print(">")
else:
    if a == b:
        print("=")
    else:
        print("<")

if a > b:
    print(">")
elif a == b:
        print("=")
else:
    print("<")

#7、尝试使用循环输出以下星号：

for i in range(9,0,-1):
    for j in range(i):
        print("*",end = "")
    print("\t")







        
