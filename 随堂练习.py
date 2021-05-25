#1.序列包含哪些基本的数据结构？
'''
字符串;元组;字典;集合;列表
'''

#2.关于列表的描述以下正确的是（）
#a.列表是可变的序列；
#b.列表可存储任意数据类型；
#c.列表的元素使用顿号分开；
#d.列表每个元素都对应一个下标，并且是从0开始的
#e.列表项不允许重复。
'''
a,b,d
'''

#3.请对列表的基础操作——增删改查进行总结，编程一个大的总结表格，梳理清晰，达到一目了然的目的
'''
增加：
append();extend();+; insert()
'''
star = ["双子","金牛","双鱼"]
star.append("射手")
print(star)

star.extend(["水瓶","巨蟹"])
print(star)

star2 = ["天秤","处女"]
star += star2
print(star)

star.insert(2,"超级无敌小可爱")
print(star)

'''删除:
clear() pop()神枪手;remove();del
'''
star.remove("超级无敌小可爱")
print(star)

star.pop(3)
print(star)

del star[2:4]
print(star)

star.clear()
print(star)

'''修改'''

animal = ["狮子","大象","长颈鹿"]
animal[2] = "猪猪"
print(animal)

'''查询：
index()
for 循环
'''
for i in animal:
     if i == "猪猪":
         print("存在")
     else:
         continue
i = animal.index("大象")
print(i)
    
     
#4.分别使用冒泡排序、选择排序、sort排序对以下列表按照从小到大的顺序进行排列
list1 = [12,34,45,6,77,8997,5,12,4556]

'''冒泡排序'''
'''
for j in range(0,len(list1)-1):
    for i in range(0,len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
print(list1)
'''

'''选择排序'''
'''
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
                list1[i],list1[j] = list1[j],list1[i]

print(list1)
'''

'''sort排序'''
i = sorted(list1)
print(i)
list1.sort(reverse = False)
print(list1)
list1.sort(reverse = True)
print(list1)
list1.reverse()
print(list1)

#5.请对列表分片、二维列表、列表解析、列表遍历进行总结。

'''列表分片'''
clip = list1[:3]
print(clip)
'''二维列表'''
list2 = [[1,2,3],[4,5,6],[77,8,9]]
for i in list2:
    for j in i:
        print(j, end = " ")
newlist = [value**3+12345 for value in range(0,5)]
print(newlist)

