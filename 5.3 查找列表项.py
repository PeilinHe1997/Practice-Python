#查找列表项

'''
1、使用index()查找列表项
2、成员运算符查找：in
3、通过for循环挨个对比，每次取一个元素
'''
#通过index()
star = ["双子","水瓶","射手"]
i = star.index("双子")
print(i)

# in
a = "射手" in star
print(a)

#for循环
'''
for i in range(3):
    if star[i] == "水瓶":
        print("水瓶")
        break
    else:
        continue
        '''

for i in star:
    if i == "水瓶":
        print("存在")
        break
        
    
    
    
