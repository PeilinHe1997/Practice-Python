# 递归函数：一个函数内部调用它自己（次数过多会导致栈溢出）
'''
1、必须有一个明确的结束条件；
2、每次进入更深一层递归时，问题规模相比上次递归都应有所减少；
3、相邻两次重复之间有紧密的联系，前一次要为后一次做准备；
   通常前一次的输出作为后一次的输入


return的两个作用:
1.用来返回一个值给函数
2.用来结束函数
'''
def summ(num):
    print(num)
    if num == 1:
        return num
    else:
        summ(num - 1)
summ(3)
#递归求sum = n + (n - 1) + (n - 2)...1
#方式一：

def summ1(n):
    if n >= 1:
        return n + summ1(n - 1)
    else:
        return 0

print(summ1(3))

#方式二：
def summ1(n):
    if n == 1:
        return 1
    else:
        return n + summ1(n-1)
print(summ1(3))

#递归求n! = 1x2x3x...x(n-1)n 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))












