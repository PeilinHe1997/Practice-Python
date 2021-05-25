#案例
'''
*
**
***
****
*****
******
'''
for i in range(6):
    for j in range(i+1):
        print("*",end = "")
    print("\t")


for i in range(1,10):
    for j in range(i):
        print("*",end = "")
    print("\t")

for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+" = "+str(j*i),end = " ")
    print("\t")
