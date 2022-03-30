from tkinter import *
root = Tk() # 创建一个窗口对象
# root 叫根窗口，在这个基础上可以创建n多个窗口，和n多个组件
# root.mainloop() # 让程序继续执行，点击窗口的关闭按钮才能关闭程序

## 窗口的属性和方法设置
# 1，设置窗口的标签
root.title("phe的第一个窗口")
# 2. 表示宽度为300，高度为500像素的窗口大小
root.geometry("300x500")
# 3. 只能将窗口拖拽扩大 400x500的大小
root.maxsize(400,500)
# 4. 只能将窗口拖拽缩小 200x300的大小
root.minsize(200,300)
# 5. 更改窗口的背景颜色，可以是颜色名称，也可以是16进制颜色
root.configure(bg = "red")
# 6. 不可更改窗口大大小
root.resizable(0,0)
# 7. 最大化窗口
root.state("zoomed")
# 8. 最小化窗口
root.iconify()
# 9. 更改默认图标
# root.iconbitmap("文件路径")# .ico文件
root.mainloop()