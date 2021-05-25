'''条件成立则一直执行
while True:
    print("我喜欢Python")
'''
flag = True
a = 0
while flag:
    a += 1 #a = a+1
    print("我喜欢Python")
    if a > 9:
        flag = False
    
