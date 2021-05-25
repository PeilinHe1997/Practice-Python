#抽象类
'''父类强制要求子类做某件事情'''
"""
一、为什么要创建抽象类？
要求子类提供具体的实现内容

二、抽象类的特点：
1、只能被继承，不能实例化（创建对象）
2、抽象类中有抽象方法，子类继承抽象类父类，必须要实现父类的抽象方法
3、定义抽象类导入abc模块：
   import abc
   格式如下：
   class 类名(metaclass = abc.ABCMeta):
   定义方法，无方法体，需要加上@abstractmethod
   @abc.abstractmethod
   def 方法名(self):pass

   TypeError:Can't instantiate abstract class dogs with abstract methods eat.

"""
'''
#创建父类——animals
class animals:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    #定义普通方法
    def eat(self):
        print("寻找食物")

#创建子类——猫类
class cats(animals):
    def eat(self):
        print("吃鱼")

#创建子类——狗类
class dogs(animals):
    def eat(self):
        print("吃骨头")

d = dogs("大黄","black")
d.eat()
'''
import abc

class animals(metaclass=abc.ABCMeta):
    #普通方法
    def __init__(self,name,color):
        self.name = name
        self.color = color
    #抽象方法
    @abc.abstractmethod
    def eat(self):
        pass

'''父类中有抽象方法eat,子类中也必须要有'''
#创建子类——狗类
class dogs(animals):
    def eat(self):
        print("吃骨头")
        
d = dogs("大黄","black")








