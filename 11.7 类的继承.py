#动物类
class Animal:
    def __init__(self,gender,color):
        self.gender = gender
        self.color = color
    def eat(self):
        print("动物要吃饭")
    def play(self):
        print("动物们喜欢玩耍")

class Cat(Animal):
    pass
#实例化对象
bosi_cat = Cat("female","orange")
bosi_cat.play()
    
