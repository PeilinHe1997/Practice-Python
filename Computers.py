class Computers:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
         
        
    def rank(self,list1):
        for j in range(0,len(list1)-1):
            for i in range(0,len(list1)-1):
                if list1[i] >= list1[i+1]:
                    list1[i],list1[i+1] = list1[i+1],list1[i]
        return list1

