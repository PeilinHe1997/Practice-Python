#datetime
'''
lib库：library 的缩写，放置库。datetime模块，存放于其中，主要提供了关于时间的功能
'''
#datetime类使用方法
'''第一个datetime指模块，第二个指类,第三个指类中的方法/函数'''
from datetime import datetime
import time

#返回指定时间
'''tzinfo 时区'''
'''datetime.datetime(year,month,day,hour = 0, minute = 0,second = 0,microsecond = 0,tzinfo = None,*,fold = 0))'''
   #定义类datetime属性
dd = datetime(2021,5,13,hour = 12, minute = 23,second = 45)
print(dd)

#返回今日的时间
     #方法一，调用类datetime里的today方法
dt = datetime.today()
'''与datetime.fromtimestamp(time.time)相同'''
print(dt)

     #方法二：调用datetime里的fromtimestamp方法
print(time.time())
de = datetime.fromtimestamp(time.time())
print(de)
     #方法三：调用datetime里的now方法
dn = datetime.now()
print(dn)

#返回世界时间
dw = datetime.utcnow()
print(dw)

print(dn.date())
print(dn.time())
print(datetime.combine(dn.date(),dn.time(),tzinfo = dn.tzinfo))
















