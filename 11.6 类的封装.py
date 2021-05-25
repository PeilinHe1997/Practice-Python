#定义卡类
class Cards:
    def __init__(self,account,password,balance):
        self.account = account
        self.password = password
        self.__balance = balance
    def deposit(self):
        print("进行存款")
    def  getBalance(self,account,password):
        if self.account == account and self.password == password:
            return self.__balance





        
c = Cards("abc123","9999","50000")
b = c.getBalance("abc123","9999")
print(b)
print(c._Cards__balance)

        
