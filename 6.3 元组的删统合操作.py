# 删除整个元组
'''元组元素删除不合法'''

animal = ("老虎","大象","狮子")
print(animal)
del(animal)
'''print(animal)'''


# 元组的统计
animal = ("老虎","大象","狮子","大象","大象","大象")
print(len(animal))
a = animal.count("大象")
print("大象出现了",a,"次")

# 元组的合并


animal1 = ("老虎","大象","狮子")
animal2 = ("小鸟","猪","天鹅")
new_animal = animal1+animal2
print(new_animal)
