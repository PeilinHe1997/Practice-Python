#有参函数

'''a,b为形参；12,67为实参'''
def max_number(a,b):
    if a > b:
        print("最大值为",a)
    else:
        print("最大值为",b)

max_number(12,67)

#冒泡排序

list1 = [23,45,66,77,88,99,0,4,5,7]

            
def soap_rank(list1):
    for j in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
                if list1[i] > list1[i+1]:
                    list1[i] , list1[i+1] = list1[i+1] , list1[i]
    print(list1)
print("----------冒泡排序-----------")
soap_rank(list1)

def choice_rank(list1):
    for j in range(0,len(list1)-1):
        for i in range(j,len(list1)):
            if list1[i] < list1[j]:
                list1[i],list1[j] = list1[j],list1[i]
    print(list1)
print("----------选择排序-----------")
choice_rank(list1)          



  
    
