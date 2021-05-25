from turtle import *

args = {(-126,162):65,(-58,55):65,(-58,-48):65,(-126,-162):65,(-300,50):120}

bgcolor("red") #background color
setup(800,500)# setup(width, height)
speed(10)#加速绘图

def star(tuples,size):
    #tuples: (x,y)
    #size:size of star
    up()#Pull the pen up – no drawing when moving.
        #down() Pull the pen down – drawing when moving.


    color("yellow","yellow")#(海龟的颜色，填充颜色）
    goto(tuples[0],tuples[1])#坐标
    begin_fill()
    for i in range(5):
        fd(size)
        rt(144)
    end_fill()
    up()
    goto(0,0)


if __name__ == "__main__":
    for key,value in args.items():
        star(key,value)
    hideturtle()#隐藏箭头(海龟)        
        
