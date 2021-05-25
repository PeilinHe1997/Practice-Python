#增加列表项
'''
1、使用append()函数增加列表项,默认添加到最后一位
2、使用extend()函数增加多个列表项
3、使用insert()函数增加制定列表项
4、使用+进行合并操作
'''
# append()
animal = ["老虎","狮子","大象","老鹰"]
animal.append("骆驼")
print(animal)

# extend()只能以列表格式添加[]，把字符串转变为列表
animal.extend(["双子","蚂蚁"])
print(animal)

# insert() 添加指定下标的列表项
animal.insert(2,"射手")
print(animal)

# +
animal1 = ["双鱼","水瓶"]
animal += animal1
print(animal)
