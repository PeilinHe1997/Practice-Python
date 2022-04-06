#################### 2. Grid方法 ###################
from tkinter import *
root = Tk()
root.geometry("400x500")

label1 = Label(root,text = "天津1", bg = "pink",fg = "red")
label2 = Label(root,text = "泸州1", bg = "black",fg = "White")
label3 = Label(root,text = "新疆1", bg = "yellow", fg = "purple")
# row从1开始，column从0开始
label1.grid(row = 1, column = 0)
label2.grid(row = 1, column = 1,columnspan = 2) # columnspan(跨列), rowspan(跨行),这里占用了第二列
label3.grid(row = 1, column = 2)


label4 = Label(root,text = "天津2", bg = "pink",fg = "red")
label5 = Label(root,text = "泸州2", bg = "black",fg = "White")
label6 = Label(root,text = "新疆2", bg = "yellow", fg = "purple")
label4.grid(row = 2, column = 0)
label5.grid(row = 2, column = 1)
label6.grid(row = 2, column = 2,rowspan = 3)




root.mainloop()