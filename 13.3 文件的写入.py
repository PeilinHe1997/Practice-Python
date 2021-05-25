
#重新写入 "w"
#f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\myfile.txt","w")


#添加 "a"
f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\myfile.txt","a",encoding = 'utf-8')
d = f.write("\n  长亭外  古道边")
f.close()

#复制文件
file_r = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\myfile.txt","r",encoding = 'utf-8')
data = file_r.read()
file_r.close()
f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\myfile2.txt","w")
e = f.write(data)
f.close()
