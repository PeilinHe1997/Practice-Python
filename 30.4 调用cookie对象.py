import re
import requests

url = "https://www.douban.com/"
res = requests.get(url)
# 获取返回的cookies对象
cookiesjar = res.cookies
# 将cookiejar转化为字典
cookdic = requests.utils.dict_from_cookiejar(cookiesjar)
print(cookiesjar)