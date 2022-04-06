#################### 3. Place方法 ###################
from tkinter import *
root = Tk()
root.geometry("400x500")

label1 = Label(root,text = "天津1", bg = "pink",fg = "red")
label2 = Label(root,text = "泸州1", bg = "black",fg = "White")
label3 = Label(root,text = "新疆1", bg = "yellow", fg = "purple")
# palce表示的是像素单位
label1.place(x = 0,y = 0)
label2.place(x = 30,y = 50)
label3.place(x = 100,y = 200)
root.mainloop()