from tkinter import *

# 1.1 Button的简单使用
# 定义Button的回调函数（就是当时间启动所做的事情）
def helloButton():
    print("我是一名汉服爱好者")
root = Tk()
root.title("你好")
root.geometry("400x500")

Button(root,
       text = "Hello Button",
       command = helloButton).pack()
# 通过command属性来指定Button的回调函数
# 每点击一次，回调函数就使用一次

# 1.2 Button的属性介绍
# 更改属性的第一种方式，在构造函数中修改
Button(root,
       text = "Hello Button",
       command = helloButton,
       activebackground = "red",
       activeforeground = "White",
       bd = 4,
       bg = "Purple").pack()
# 1 activebackground: 鼠标点击的时候，按钮的背景色
# 2 activeforeground: 鼠标点击的时候，字体的颜色
# 3 bd: 按钮框的粗细，默认为两个像素
# 4 bg: 按钮的背景颜色

# 更改属性的第二种方式
'''
方式1:组件对象["关键字参数"] = 所要修改的值
方式2: 组件对象.config(关键字参数=所要修改的值)
'''
# 111111
def helloButton():
    button["text"] = "中国人"
    print("我是一名汉服爱好者")
button = Button(root,
       text = "Hello Button",
       command = helloButton,
       activebackground = "red",
       activeforeground = "White",
       bd = 4,
       bg = "yellow")
button.pack()

# 222222
def helloButton1():
    button1.config(text = "I love you")
    print("我是一名汉服爱好者")

button1 = Button(root,
       text = "Hello Button",
       command = helloButton1,
       activebackground = "red",
       activeforeground = "White",
       bd = 4,
       bg = "Purple")
button1.pack()

root.mainloop()# 窗口持续执行
