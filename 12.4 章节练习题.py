#读取文件
file = None
data = None
try:
    file = open(r"C:\Users\84021\Pictures\证件照.png","rb")
    data = file.read()
except Exception as e:
    print(e)
finally:
    if file:
        file.close()

#写入文件
try:
    file = open(r"C:\Users\84021\Pictures\证件照2.png","wb")
except Exception as e:
    print(e)
finally:
    if file:
        file.close()
#编写一个让用户输入一组数据（带有空格），将所输入的数据转化为列表，然后对列表项进行筛选
        #将列表中整型元素放到一个新列表中，并且判断列表元素中有哪些整数能同时被2和3整除，并对程序异常进行处理
list1 = input("请输入一组带有空格的数据")
list1 = list1.split(" ")
new_list = []
for i in list1:
    try:
        a = int(i)
    except Exception as e:
        print(e)
    else:
        new_list.append(a)
result = []
for i in new_list:
    if i % 6 == 0:
        result.append(i)
        
print(result)
        
    
