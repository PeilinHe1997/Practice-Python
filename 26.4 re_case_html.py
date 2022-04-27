import re

# 1.匹配：<h1>sdfsdfg</h1>
# <>和/括号还用他们自身匹配
# \w可以匹配数字、字母、下划线、希腊字母、俄文字母等
# . 匹配任意单字符（除了\n）
# * 表示至少有0个

str = "<h1>python01</h1>"
result = re.match(r"<\w*>.*</\w*>",str)
print(result)


# 2.匹配：<h1>sdfsdfg</h1>
# ()表示组
# (\w*)表示有内容的一个组
# \1表示第一组，和前面的\w*是一样的同一组

str = "<h1>python01</h1>"
result = re.match(r"<(\w*)>.*</\1>",str)
print(result)

# 3.匹配：<body><h1>sdfsdfg</h1></body>
# 找到组的一一对应关系，从左往右数组数从1开始然后组别进行匹配
str = "<body><h1>sdfsdfg</h1></body>"
result = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",str)
print(result)

str2 = "<high><h1>sdfsdfg</h1></high>"
result = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",str2)
print(result)

# 4.匹配:"<body><h1>sdfsdfg</h1></body>"
# ?P<n1>表示给组设置变量名，将其定义在组内
# (?P=n1)
str = "<body><h1>sdfsdfg</h1></body>"
result = re.match(r"<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>",str)
print(result)
