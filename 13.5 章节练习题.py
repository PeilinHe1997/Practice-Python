#第一题
file_r =open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\poetry.txt","w",encoding = 'utf-8')
poetry = file_r.write("我爱他\n轰轰烈烈最疯狂\n我的梦\n狠狠碎过却不会忘")
print(poetry)
file_r.close()

f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\poetry.txt","a",encoding = 'utf-8')
d = f.write("\n源自歌手丁当")
f.close()

#第二题：从键盘输入一个字符串，将小写字母全部转换为大写字母，然后输出到一个文件名为Capital.txt
str1 =input("请输入一个字符串")
list1 = []#用来存储字符串
list2 = []#用来存储整型数据
for i in str1:
    if i.isdigit() == True:
        list2.append(int(i))
    else:
        list1.append(i.upper())
print(list1)
print(list2)

f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\Capital.txt","w")
for i in list1:
    f.write(i)
f.close()
