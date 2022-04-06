from tkinter import *
root = Tk()
root.geometry("400x500")

label1 = Label(root,text = "天津", bg = "pink",fg = "red")
label2 = Label(root,text = "泸州", bg = "black",fg = "White")
label3 = Label(root,text = "新疆", bg = "yellow", fg = "purple")

#################### 1. Pack方法 ###################
# TOP 表示方式标签时从最上面开始
# 去掉top也是从顶上开始的，top是默认值
# BOTTOM LEFT RIGHT

# label1.pack(side = TOP)
# label2.pack(side = LEFT)
# label3.pack(side = RIGHT)
label1.pack(side = BOTTOM, fill = X)# fill = X 填充X轴
label2.pack(fill = Y)# 填充Y轴
label3.pack(pady = 100)# Y轴增加100个像素（上下）,padx x轴上增加像素








root.mainloop()