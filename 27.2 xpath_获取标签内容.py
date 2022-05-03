from lxml import etree

html = etree.parse("http://www.mafengwo.cn/gonglve/ziyouxing/136819.html", etree.HTMLParser()) # 加载html文档，返回值依然是一个特殊的HTML结构
result = etree.tostring(html, encoding = "utf-8").decode() # 转化为普通字符串
print(result)

######### 1. 获取某一类标签内容
#调用xpath函数，参数为字符串类型
# //a表示所有的a标签，//标签名表示：所有的什么标签
r2 = html.xpath("//a")
print(r2)
print(type(r2))
print(r2[0])

r3 = html.xpath("//div//a") #所有div下的a标签
print(r3)

######### 2. 获取指定标签内容
r4 = html.xpath("//div/a[@class='sideR']")
# div表示所有的div标签
# span表示div的子级span标签
# [@属性名 = 属性值]表示筛选条件
print(r4)


######## 3. 获取标签属性
r5 = html.xpath("//div/span/@class")
print("r5",r5)
# //div表示所有的div标签
# /span表示div的子级span标签
# @属性名 表示筛选条件
r6 = html.xpath("//a/@href")
print(r6)

