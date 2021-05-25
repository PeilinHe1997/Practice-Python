'''
创建一个电脑的类Computers
电脑的属性：品牌、价格、颜色、大小
电脑的方法：打字、安装软件
并尝试调用输出电脑的属性和方法
'''
class Computers:
    #初始化属性
    def __init__(self,brand,price,color,size):
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size
    #定义方法
    def type(self):
        print("打字")

    def software(self,chip):
        print(self.brand+"安装软件"+chip)

c = Computers("HUAWEI",3999,"purple",14)
c.price = 1988
print(c.price)
c.type()
c.software("麒麟")
        
