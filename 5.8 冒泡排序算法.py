#冒泡排序
'''每轮都会将较大的数往前移'''

'''
第一轮判断两两相邻的数字，将较大的更换位置
重复这样的操作，一共进行了列表长度-1轮

'''
num = [7,34,25,15,68,5,5,6,6,788]

for j in range(0,len(num)-1):
    for i in range(0,len(num)-1):
        if num[i] < num[i+1]:
            num[i],num[i+1] = num[i+1],num[i]

print(num)
