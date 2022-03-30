from tkinter import *
import matplotlib.pyplot as plt

root = Tk()
root.geometry("300x500")
# 创建一个label
label = Label(root,
              text = "Hello Tkinter")
# 参数一：指的是我们要将这个标签文字放置在哪个地方，肯定是窗口中了，所以写root
# 参数二: 指的是我们要放置的内容，这里使用了关键字参数

# label仅仅是一个返回的对象，如果要显示，需要把这个对象包装显示。
label.pack()

# 可以设置字体的颜色
label = Label(root,
              fg = "White",
              bg = "Red",
              text = "我爱中国",
              width = 10,
              height = 5)
label.pack()
# fg:字体本身的颜色
# bg: 字体的背景颜色
# width,height: 有多少个字符的高度宽度，不是像素单位，而是字符单位


# 也可以一次性创建多个label对象
Label(root, text = "dog", bg = "green").pack()
Label(root, text = "happy", bg = "blue").pack()
Label(root, text = "cat", bg = "purple").pack()

# 显示多行文本
Label(root,
      text = "There it was, hanging in the sky above the school: "
                   "the blazing green skull with a serpent tongue, "
                   "the mark Death Eaters left behind where they had entered a building "
                   "... wherever they had murdered",
      width = 50,
      height = 5,
      wraplength = 300,
      justify = "left",
      bg = "black",
      fg = "White").pack()
# wraplength: 指定多少单位后开始换行，单位是屏幕单元，就是我们所说的屏幕像素。
# justify: 对齐方式


# anchor 指定文本或图像在Label中的显示位置，值所在的布局如下所示：
# nw     n     ne
# w   center    e
# sw     s     se
Label(root,
      text = "I love Mallorca",
      bg = "purple",
      fg = "yellow",
      width = 5,
      height = 5,
      anchor = "nw").pack()

##### Label的图片属性 ######

# 在label上使用内置图片，使用bitmap方法
Label(root,bitmap = "error").pack()
Label(root,bitmap = "hourglass").pack()
Label(root,bitmap = "info").pack()
Label(root,bitmap = "question").pack()
Label(root,bitmap = "questhead").pack()
Label(root,bitmap = "warning").pack()
Label(root,bitmap = "gray12").pack()
Label(root,bitmap = "gray25").pack()

# 使用image属性显示图片
x = [i for i in range(10)]
y = [2*i  for i in range(10)]
plt.plot(x,y)
plt.savefig('./line.png')
file3 = open(r"line.png","rb")
data3 = file3.read()
file3.close()

bm = PhotoImage(file = r"./line.png")
label = Label(root, image = bm, width = 100, height = 100)
label.pack()


###### 同时使用图像与文本  ###########
# Compound: 指定文本与图像是如何在Label上显示的
# left:图像居左
# right: 图像居右
# top: 图像居上
# bottom: 图像居下
# center: 图像居中
Label(root,
      text = "bottom",
      compound = "bottom",
      bitmap = "error").pack()





root.mainloop()



