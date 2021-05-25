# break 关键字指结束循环执行
# continue关键字跳出本轮循环

# break
a = 0
while True:
    a += 1
    print("我喜欢Python")
    if a > 9:
        break

# continue
for i in range(100):
    if i%2 == 0:
        continue
    #当i%2 == 0时，跳出，从头（for）开始执行
    print(i)
