
def max_num(a,b):
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b
    
# 位置传参        
m = max_num(12,3)

#关键字传参(无需考虑参数位置)
K = max_num(b = 13, a = 45)

#默认值传参
'''第一位不能使用默认值传参'''
def max_num(a,b = 45):
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b
n = max_num(13)

#可变参数
'''一个*被自动组装为元组，两个**被自动组装为字典'''

def animals(*name):
    print(name)
    print(type(name))
    str_name = ""
    for i in name:
        str_name += i
    return str_name

str_name = animals("小可爱","小笨蛋")
print(str_name)


def animals(**name):
    print(name)
    print(type(name))
    
animals(name1 = "小可爱",name2 = "小笨蛋",name3 = "小苹果")


















