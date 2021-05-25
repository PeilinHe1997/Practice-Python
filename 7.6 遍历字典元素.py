# 遍历字典
'''鉴于字典可能会包含大量的数据，python支持对字典的遍历
对字典的遍历一般包括：
   遍历字典的键值对
   遍历值
   遍历键
'''
import time
#1、遍历键值对
stu1 = {"kiki":24,"yuna":19,"Tom":22,"Chir":23}
for key,value in stu1.items():
    print(key,value)
time.sleep(1)

for k,v in stu1.items():
    print(k,v)
time.sleep(1)

#2、keys()遍历键
#   values()遍历值
for key in stu1.keys():
    print(key)
time.sleep(1)
for values in stu1.values():
    print(values)
