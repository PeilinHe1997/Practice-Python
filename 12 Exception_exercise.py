# 练习:1. 编写一个复制和粘贴视频文件的程序，并且对程序进行异常处理

file = None
data = None
file1 = None
# 读取文件
# 正确语句 file = open(r"C:\Users\84021\Desktop\罗马\TicketsColo.pdf","rb")
try:
    file = open(r"C:\Users\84021\Desktop\TicketsColo.pdf","rb")
    data = file.read()
except Exception as e:
    print(e)
finally:
    if file:# 如果file不是空的，执行
        file.close()

# 写入文件
try:
    file1 = open(r"C:\Users\84021\Desktop\test1.pdf","wb")
    data = file1.write(data)
except Exception as e:
    print(e)
finally:
    if file1:
        file1.close()
