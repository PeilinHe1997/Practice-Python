#rb:read binary
file_r =open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\生活照.jpg","rb")
data = file_r.read()
file_r.close()

#wb:write binary
f =open(r"C:\Users\84021\Desktop\自学\Python.le\第十三章 文件读写\生活照2.jpg","wb")
d = f.write(data)
f.close()


