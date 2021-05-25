# 有返回值的函数创建

def max_num(a,b):
    if a > b:
        return a
    else:
        return b
n = max_num(23,67)
print(n)


#筛选出一个给定列表的偶数
list1 = [23,44,67,88,90,57]

def oushu_list(list1):
    new_list = []
    for i in list1:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
new_list = oushu_list(list1)
print(new_list)
            
            
