import re
import requests
import urllib.request
import urllib.parse
url = "https://www.iqianyue.com/mypost"
response = urllib.request.urlopen(url).read().decode()
print(response)
# 可以从response中看到用户名为“name”,密码为“pass”
print("-------------------------")


data_dic = {"name":"hero","pass":"password"}# 不同网址用户名和密码有不同字段
res = requests.post(url,data = data_dic)
print(res.text)
