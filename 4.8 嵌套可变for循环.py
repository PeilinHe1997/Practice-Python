#for 循环使用
'''
****
****
****
'''
#mehod 1
print("------------method1----------")
for i in range(3):
    print("****")


#mehod 2
print("------------method1----------")
for i in range(3):
    for j in range(4):
        print("*",end = "")
    print("\t")
'''内层for循环是每一行有多少列， 外层for指的是行'''

row = int(input("您指定多少行"))
column = int(input("您指定多少列"))
for i in range(row):
    for j in range(column):
        print("*",end = "")
    print("\t")
