for i in range(10):
    print("我喜欢Python")

print(range(10))

#range（9）并不等效于列表[1,2,3,4,5,6,7,8,9,10]
#他们两个没有任何关系，range(9)仅仅返回一个可迭代的对象


'''
range(10)——可以理解为[0,1,2,3,4,5,6,7,8,9]
'''
for i in range(2,5):
    print(i)

for i in range(2,10,2):
    print(i)
'''
range(4)-[0,1,2,3]
range(2,5)-[2,3,4]
range(1,10,2)——步进为2，[1,3,5,7,9]
