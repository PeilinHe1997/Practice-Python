#字典嵌套

#1、嵌套——将字典存储在列表中
import time
stu1 = {"name":"Tom","age":19,"gender":"Male","height":180}
stu2 = {"name":"Riddle","age":25,"gender":"Female","height":168}
stu3 = {"name":"Harry","age":23,"gender":"Male","height":175}
person = [stu1,stu2,stu3]
for i in person:
    for key,value in i.items():
        print(key,value)
    time.sleep(1)
    print("----------")

#2、嵌套——将字典存储在字典中
person = {"stu1":stu1,"stu2":stu2,"stu3":stu3}
for value_stu in person.values():
    for key,value in value_stu.items():
        print(key,value)
    time.sleep(1)
    print("----------")
