#类与对象

class Students:#定义学生类
    #定义属性
    name = ""
    age = 0
    gender = ""
    grand = 0
    #定义类的方法
    def learn(self):
        print("学习")
    def play(self):
        print("玩耍")
        
#创建对象
stu1 = Students()
stu2 = Students()
stu3 = Students()

stu1.name = "小张"
stu1.age = 12
stu2.name = "小王"
stu2.age = 14
stu3.name = "小z"
stu3.age = 13


print(stu1.name)
print(stu1.age)
stu1.learn()
