from turtle import *

print(position())
forward(-75)#前进
print(position())

backward(-75)#后退
print(position())

rt(90)#箭头右转90度
print(position())

goto(100,200)#去某个位置position
print(position())

#箭头朝向：
setheading(180)
print(position())
'''to_angle标准模式：0-东；90-北；180-西；270-南'''

#home 返回原点
#circle 画圆
circle(radius = 100, extent = None, steps = None)

#undo 撤销
#lt箭头左转

for i in range(4):
    fd(50)
    lt(80)
#执行次数为2*4 = 8
for i in range(8):
    undo()

