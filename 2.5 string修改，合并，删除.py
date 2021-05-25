#Python 基本数据类型
#string的修改 合并 删除

##   字符串合并

first_name = "Peilin"
last_name = "He"
new_name = first_name+" "+last_name
print(new_name)

##   字符串的修改

new_name1 = new_name[:6]+" "+"python"
print(new_name1)
#通过replace函数修改
new_name2 = new_name1.replace("python","A")
print(new_name2)
# Peilin A


##    字符串的删除
#python 字符串是不可变类型，无法直接删除字符串的某一个字符；
#只能通过修改的方式实现。
del(new_name2)#报错
print(new_name2)
