# 关于如何读取文件
# io： Input和Output
from matplotlib import pyplot as plt
# 读取text文件 textI/O
f = open("abc.txt", "r", encoding="utf-8") # r：“read”
d = f.read()
print(d)
print("=============================")

file = open(r"abc.txt","w")
data = file.write("I like coffee")# 重新写入，原来的内容被覆盖
file.close()
f = open("abc.txt", "r", encoding="utf-8") # r：“read”
d = f.read()
print(d)
print("=============================")


file = open(r"abc.txt","a")
data = file.write("This is a table")# 加入新内容
file.close()
f = open("abc.txt", "r", encoding="utf-8") # r：“read”
d = f.read()
print(d)
print("=============================")


# 创建新文件
f2 = open(r"newfile.txt","w")
d_new = f2.write(d)# 将文件abc中的内容添加进newfile里面
f2.close()
f2 = open("newfile.txt", "r", encoding="utf-8")
d_new_r = f2.read()
print(d_new_r)


# 二进制文件的读和写
# “rb”, “wb”
plt.scatter(3,5)
plt.savefig('./dot.png')
file3 = open(r"dot.png","rb")
data3 = file3.read()
file3.close()

file4 = open(r"dot2.png","wb")
file4.write(data3)# 复制粘贴
file4.close()