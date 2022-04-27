import re
# match: 从头进行匹配
# search: 只要字符串中有满足正则表达式就算匹配成功，匹配的顺序是从左到右
# findall: 找到所有满足正则的数据，返回一个列表
# sub: 根据正则匹配成功之后，再进行替换，可以替换很多个

result = re.match(r"[a-bA-C]","你真的好可爱ddddddaaaaesdsfdssgsgisaszdsjccsd")
print(result)

result = re.search(r"[a-bA-C]","你真的好可爱ddddddaaaaesdsfdssgsgisaszdsjccsd")
print(result)

result = re.findall(r"[a-bA-C]","你真的好可爱ddddddaaaaesdsfdssgsgisaszdsjccsd")
print(result)

result = re.sub(r"[a-bA-C]","替换","你真的好可爱ddddddaaaaesdsfdssgsgisaszdsjccsd")
print(result)