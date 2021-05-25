f = open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\myfile.txt", "r",encoding = 'utf-8')
d = f.read()
print(d)
print(f)
#关闭通道，不关闭通道有可能报异常
f.close()
