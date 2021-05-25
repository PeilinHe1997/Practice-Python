strs = input("请输入一组带有空格的数字")
lists = strs.split(" ")
'''
if len(lists) >= 5:
    print(lists)
else:
    #创建异常对象
    e = Exception("列表长度小于5")
    #抛出异常
    raise e
'''
new_lists = [] #创建空列表
for i in lists:
    try:
        element = int(i)
    except Exception as e:
        print(e)
    else:
        new_lists.append(element)
print(new_lists)
