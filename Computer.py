class Computers:
    #初始化属性
    def __init__(self,brand,price,color,size):
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size

    #定义方法
    def print_word(self):
        print("打字")
    def install_software(self,chip):
        print(self.brand + "安装软件" + chip)

c = Computers("HUAWEI",2000,"black",14)
c.price = 1988
print(c.price)
c.install_software("麒麟")
