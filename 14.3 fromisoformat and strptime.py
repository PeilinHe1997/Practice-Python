from datetime import datetime
import time 

dn = datetime.today()
dc = datetime.combine(dn.date(),dn.time(),tzinfo = dn.tzinfo)
print(dc)
'''
共同点：都是将日期字符串转换成datetime类型
不同点：fromisoformat里面的date_string格式必须符合yyyy-MM-dd HH:mm:ss.ffffff
        否则会报错。
        strptime是只要date_string 和后面的format一致就行，比如datetime.strptime('2019-08-18')

'''
df = datetime.fromisoformat('2019-11-08 22:01')
print(df)

ds = datetime.strptime('2019年11月08日','%Y年%m月%d日')
print(ds)

dns = dn.strftime('%Y年%m月%d日')
print(dns)
