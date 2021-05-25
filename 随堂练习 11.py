#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,并打印输出信息
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print("姓名：",self.name)
        print("年龄：",self.age)
        print("性别：",self.gender)

#2、创建Farmers农民类，继承Person类，属性有工作job,工作地place,
    #重写父类personInfo方法，并将重写后的方法将农民的工作、地点打印出来
    #创建方法cultivation耕耘，打印输出：我的工作是***
    #定义Scientist 科学家类，打印输出科学家的信息，定义科学家invention发明的方法：
    #"袁隆平发明了杂交水稻" 并将其打印出来。
class Farmers(Person):
    def __init__(self,job,place):
        self.job = job
        self.place = place
    def personInfo(self):
        print("我是农民，我的工作是"+self.job+"\n我的工作地点是"+self.place)
    def cultivation(self):
        print("我的工作是"+self.job)


class Scientists(Person):
    def invention(self):
        print("袁隆平发明了杂交水稻")

f = Farmers("种田","四川")
f.personInfo()
s = Scientists("袁隆平",90,"男")
s.personInfo()
s.invention()
        
