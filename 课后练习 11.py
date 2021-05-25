#1.使用视觉化的表达方式对类、对象、属性、方法进行总结梳理。

#类
class Animals:
    #属性
    def __init__(self,color,gender):
        self.__color = color
        self.gender = gender
    #方法
    def type(self):
        print("可可爱爱")
    def getColor(self,color):
        if color == self.__color:
            return self.__color
        
#对象
c = Animals("white","male")
print(c.getColor("white"))
print(c._Animals__color)
        
    
    
#2．下列不属于面向对象编程的特性的是()。

#A．封装                         B．继承

#C．抽象                         D．多态

'''C'''

#3．下列类的声明中不合法的是（    ）。

#A．class Flower:

#B．class 狗类：

#C．class Flower(object):

'''B'''

#4.根据所学的知识创建一个父类和多个子类，子类继承父类，并且对属性方法和普通方法进行调用,在不断的强化练习中增加对知识点的掌握。
'''
import abc
class Person(metaclass=abc.ABCMeta):
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    @abc.abstractmethod
    def outer(self):
        print("他/她是"+self.name)


class Farmer(Person):
    def __init__(self,job,place):
        self.job = job
        self.place = place
    def outer(self):
        print("他/她的工作是"+self.job+"\n工作的地点是"+self.place)


a = Farmer("科学家","China")
a.outer()
'''
class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def outer(self):
        print("他/她是"+self.name)


class Farmer(Person):
    def __init__(self,job,place):
        self.job = job
        self.place = place
    def outer(self):
        print("他/她的工作是"+self.job+"\n工作的地点是"+self.place)

class Scientists(Person):
    def outer(self):
        print("他是科学家")

a = Farmer("Sci","China")
a.outer()
b = Scientists("袁隆平","男",90)
b.outer()
