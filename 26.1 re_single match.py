import re

result = re.match(r"python","python is good")
result2 = re.match(r"ython","python is good")

# result = re.match(r"正则表达式",要匹配的字符串)
# 参数1： 写正则表达式
# 参数2： 要匹配的字符串，前者是规范，后者要匹配
# <re.Match object; span=(0, 6), match='python'> span表示匹配到的下标，match表示匹配成功的内容

print(result)
print(result2)
print(result.group()) # 显示匹配成功的字符串
# 'NoneType' object has no attribute 'group'


#### 1.2 正则表达式匹配单个字符 ####
print("==========1.2 正则表达式匹配单个字符============")

# \d表示0-9的数字，只匹配一个
r1 = re.match(r"\d","2python")
print(r1)
r11 = re.match(r"\d","python2")# 前面没匹配就是None
print(r11)

# [12345678]表示任选其中一个元素
# [1-8]表示1到8任选其中一个元素
# [1-35-8]表示1到3,5到8任选一个元素
r2 = re.match(r"[12345678]","4python")
print(r2)
r22 = re.match(r"[1-35-8]","4python")
print(r22)

# 匹配单字符-字母
# [a-z]a到z的小写字母任选一个元素
# [A-Z]A到Z的大写字母任选一个元素
# [1-35-8a-zA-Z]1到3，5到8，a到z,A到Z任选其中一个元素,匹配任意单字符，除了\n
r3 = re.match(r"[a-z]","python2")
print(r3)
r33 = re.match(r"[1-35-8a-zA-Z]","I LIKE THAT")
print(r33)

# \w可以匹配数字、字母、下划线、希腊字母、俄文字母等（中文字符也可以）
# \s可以匹配空白字符（空格，table键）
# 所有使用大写字母表示的都是相反的
r4 = re.match(r"\w","你好Roma2")
print(r4)
r44 = re.match(r"\s","     3 python")
print(r44)
r444 = re.match(r"\S","     3 python")# 不可以匹配空格字符，table键
print(r444)