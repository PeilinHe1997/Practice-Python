class Computers:#定义电脑的类
    #定义类变量
    price = 5998

    #定义类的属性,实例变量
    def __init__(self,brand,color,size):
        self.brand = brand
        self.color = color
        self.size = size

    #定义方法
    def type(self):
        print("打字")

    def software(self,chip):
        print(self.brand+"安装软件"+chip)



''''只要类变量改变，都改变'''

c = Computers("HUAWEI","purple",14)
print(c.price)

d = Computers("DELL","red",12)
print(d.price)
        
