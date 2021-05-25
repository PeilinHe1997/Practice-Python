
#1.关于字典的描述以下正确的是（）
'''
a.字典是可变的序列；
b.字典的键可以使用任意数据类型表示；
c.字典的每一对的键值对使用逗号隔开；
d.字典的数据结构属于映射；
e.字典不允许重复。
'''

#a-键不可变，值可变
#b-键为字符串类型
#c-每队键值用逗号隔开
#d-数据结构属于映射
#e-键不可重复， 值可重复

#2.请你使用嵌套字典的样式表示以下数据：并将字典的值进行遍历输出
'''
【水果】哈密瓜：12.3/kg  菠萝：21.2/kg   香蕉：19.4 /kg   火龙果 16.2/kg
【青菜】青椒：2.2/kg   黄瓜：3.1/kg  上海青：2.1/kg  鸡蛋 12.4/kg
【干果】冬枣：14.2/kg  木耳 3.4/kg  银耳：4.1/kg   人造肉 4.1/kg
'''
fruit = {"哈密瓜":"12.3/kg","菠萝":"21.2/kg","香蕉":"19.4 /kg","火龙果":"16.2/kg"}
veg ={"青椒":"2.2/kg","黄瓜":"3.1/kg","上海青":"2.1/kg","鸡蛋":"12.4/kg"}
dried = {"冬枣":"14.2/kg","木耳":"3.4/kg","银耳":"4.1/kg","人造肉":"4.1/kg"}

dics = {"水果":fruit,"青菜":veg,"干果":dried}

for key,value in dics.items():
    print("-------------"+str(key)+"-------------")
    for k,v in value.items():
        print(k, v)

#3.总结字典的增删改查的操作？
print("------------增--------------")
#增
'''1、通过赋值；2、setdefault函数'''
fruit.setdefault("蓝莓","30/kg")
fruit["西瓜"] = "16/kg"
for k,v in fruit.items():
        print(k, v)

print("-------------删-------------")        
#删
''' 1、del;2、pop();3、popitem'''
del fruit["蓝莓"]
fruit.pop("西瓜")
fruit.popitem()#删除最后一个键值对
for k,v in fruit.items():
    print(k, v)
fruit.clear()

print("-------------改-------------")   
#改
'''1、通过赋值；2、通过update()函数更新'''
veg["青椒"] = "18.2/kg"
updics = {"小米辣":"14/kg"}
veg.update(updics)
for k,v in veg.items():
    print(k, v)

print("-------------查-------------")
#查
'''
1、通过指定键查找对应值
2、get()函数
3、if .values() .keys()判断
'''
a = dried["木耳"]
print(a)
b = dried.get("木耳")
print(b)
if "14.2/kg" in dried.values():
    print("存在")
else:
    print("不存在")


if "木耳" in dried.keys():
    print("存在")
else:
    print("不存在")











    



