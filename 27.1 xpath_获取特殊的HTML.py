# Xpath 全称XML Path Language即XML路径语言，是一门xml文档中查找数据信息的语言。
# 最初是用来搜寻XML文档的，但同样适用于HTML文档的搜索，所以在做爬虫的时候完全可由XPath提取信息。

# lxml是一个HTML/XML的解析器，主要的功能是如何解析和提取HTML/XML数据
# lxml和正则一样，是用C实现的，是一款高性能的解析器，不过在Python中属于第三方模块，需要进行安装

# import lxml

# 1获取特殊的HTML
from lxml import etree

text = "sdfsdgfdgfdg lalalalalalallaqw  路飞  one piece"

html = etree.HTML(text)
# 将用来解析字符串格式的HTML文档对象转变为特殊的html文档，
# 特殊包含3处：
# 1. 会额外添加一些标签（补充标签）、
# 2. 转化为二进制字节码（中文转化为二进制字节码）
# 3. 对格式进行处理（将格式进行对其）

result = etree.tostring(html, encoding = "utf-8").decode()
# 将特殊的HTML文档转化为字符串格式，才能够输出打印
print(result)
