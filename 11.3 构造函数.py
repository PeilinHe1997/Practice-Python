class Students:#定义学生类
    #初始化属性
    def __init__(self,name,age,gender,grand):
        self.name = name
        self.age = age
        self.gender = gender
        self.grand = 3



    #定义方法
    def learn(self):
        print("我喜欢学习")
#对象是谁，self就是谁
stu1 = Students("小王",12,"男",3)#这里self指的是stu1
stu1.learn()
