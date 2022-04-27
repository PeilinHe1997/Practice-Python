import re

# case1.判断变量的名称: 由数字、字母、下划线组成，不能以数字作为开头
# [a-zA-Z_][a-zA-Z0-9_]*$
# $表示到结尾
# 注意:如果不加$符号，中间如果有一些不符合字符abc*&就会被匹配掉

result = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$","1name")
print(result)

result = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*","abc*&")
print(result)

result = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*","abcser23445")
print(result)

# case2. 判断4-20位163格式邮箱
# [a-zA-Z0-9_]{4,20}@163\.com$
# \.表示普通的点
# 注意：如果不加$符号，dafsdf@163.com.com也能通过

result = re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$","abcssdfsdf@163.com")
print(result)

# case3. 判断163,126邮箱
# [a-zA-Z0-9_]{4,20}@(163|126)\.com$

result = re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$","abcssdfsdf@126.com")
print(result)