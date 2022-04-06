from tkinter import *
root = Tk()
root.title("button2")
root.geometry("400x500")

button = Button(root,
                text = "夜莺与玫瑰",
                activebackground = "red",
                activeforeground = "White",
                bd = 20,
                bg = "pink",
                fg = "red",
                font = ("黑体",12),
                height = 2,
                width = 10)
# font: 字体名称和大小
# fg: 按钮上字体的颜色
# 当没有图片时候，height 和 width指的是字符长度
button.pack()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [6,7,8,9,10]
plt.plot(x,y)
file = open("buttontest.png","wb")
plt.savefig("buttontest.png")
file.close()

bm = PhotoImage(file = "buttontest.png")
# 可以指定按钮图片的大小
Button(root,
       image = bm,
       height = 50,
       width = 100).pack()

import networkx as nx
edgelist = [(1,1),(1,2),(1,4),(4,2),(1,3)]
G = nx.Graph()
G.add_edges_from(edgelist)


def ButtonPicture():
    edgelist = [(1, 3), (1, 2), (1, 4), (4, 2), (2, 3)]
    G = nx.Graph()
    G.add_edges_from(edgelist)
    nx.draw_networkx(G)
    plt.show()


Button(root,
       command = ButtonPicture,
       text = "Picture").pack()

root.mainloop()