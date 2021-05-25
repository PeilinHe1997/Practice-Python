'''
import turtle
t = turtle.Turtle() #创建一个海归对象
for i in range(0,100,4): #从0循环到99，步进为4
    t.forward(i)
    t.left(90)
'''

from turtle import *
bgcolor("black")#背景颜色
color = ["red","yellow","blue","white","green","purple"]
for i in range(0,150,5):
    pencolor(color[i%6])
    fd(i)
    lt(60)
