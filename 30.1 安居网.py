# 数据挖掘: urllib(python自带的库) 无需安装
#         requests库(第三方库) 需要下载安装
# 数据清洗: Python 正则表达式，比较常用的有BeautifulSoup框架和scrapy框架

# 安居客 案例
import requests
import random
import re

ugList = ["Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/543.50",
          "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
          "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"]

header = {"User-Agent":random.choice(ugList)}



# r = requests.get("https://tianjin.anjuke.com/?",headers = header)

# print(r.text) # 打印text形式的数据
# print(r.content)# 打印二进制数据

wd = {"wd":"万达"}
r = requests.get("https://tj.fang.anjuke.com/loupan/s?",headers = header,params = wd)
# https://tj.fang.anjuke.com/loupan/s?kw=%E4%B8%87%E8%BE%BE 搜索万达出现的网址
try:
    print(r.text)
except ConnectionError: # 断网
    print("停止输出")

