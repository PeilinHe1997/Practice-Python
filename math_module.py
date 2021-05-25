
#筛选出一个给定列表的偶数
def oushu_list(list1):
    new_list = []
    for i in list1:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
#冒泡排序
def soap_rank(list1):
    for j in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
                if list1[i] > list1[i+1]:
                    list1[i] , list1[i+1] = list1[i+1] , list1[i]
    return list1
    print(list1)
#比较大小
def max_number(a,b):
    if a > b:
        print("最大值为",a)
    else:
        print("最大值为",b)
