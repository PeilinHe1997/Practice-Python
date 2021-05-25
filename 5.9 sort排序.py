# sort排序

num1 = [2,335,66,7,88,94,74,0,12]
str1 = ["and","Tfb","Jack","Herolong","long"]
'''
#1、sort(reverse = False)/sort()升序排序
num1.sort()
str1.sort(reverse = False)
print(num1)
print(str1)

#2、sort(reverse = True)降序排序
num1.sort(reverse = True)
str1.sort(reverse = True)
print(num1)
print(str1)

#3、反向排序reverse()函数进行排序
num1.reverse()
str1.reverse()
print(num1)
print(str1)

#4、使用sorted(需要排序的序列)返回新的升序列表,原来的列表不发生改变
new_num = sorted(num1)
new_str = sorted(str1)
print(new_num)
print(new_str)
'''
#5、使用sort(key = len)按照字符串长度从短到长排序
str1.sort(key = len,reverse = False)
print(str1)

#6、使用sort(key = str.lower)大写转小写再排序 upper 小写转大写
str1.sort(key = str.upper)
print(str1)
















