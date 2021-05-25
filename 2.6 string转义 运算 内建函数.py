       #字符串转义

# \n 换行
# \000 空格
# r 取消转义，在字符外面加r

a = "abc\ndef"
print(a)

a = r"abc\ndef"
print(a)

a = "abc\000def"
print(a)

        #字符串运算

# * 重复输出
# in 判断某一个字符是否在string中 True False
# not in
name = "Peilin\n"
print(name*3)
print("e" in name)
print("e" not in name)

        #字符串内建函数
#len()
a = "adCdeFg"
print("原始string为：",a)
num = len(a)
print(num)

#lower() 大写转小写
#upper() 小写转大写
#swapcase() 大小写互相转换
A = a.lower()
b = a.upper()
c = a.swapcase()
print(A)
print(b)
print(c)

#count() 出现次数
cou = a.count("d")
print(cou)

#index(索引)  查找下标
ind = a.index("d")
print(ind)














