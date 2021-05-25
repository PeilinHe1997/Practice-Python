# 二维列表，在这个列表中还有二级子列表
list1 = [[1,2,3],[4,5,6],[7,8,9]]
print("list1[1]:",list1[1])
print("list1[1][2]:",list1[1][2])

#遍历列表项
newlist = [23,4555,68,"sdf","12"]
for i in newlist:
    print(i,end = " ")
print("\t")

print("------------------")
#遍历二维列表项
for i in list1:
    for j in i:
        print(j,end =" ")
    print(sep = "|")

