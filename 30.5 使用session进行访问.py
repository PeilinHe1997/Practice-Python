import requests
# cookies:用户ID,用户密码,浏览的网页,停留时间等信息

url = "https://www.douban.com/"
# 创建session对象
session = requests.session()
# 构造登录所需要的参数
# 查询data的方法：右键inspect----elements(鼠标跟随模式)-----可以看到信息
data = {"username":"13398268812","password":"qaz321123"}
# 提交数据，获取cookie
session.post(url,data = data)

#让session再次进行请求
res = session.get(url)
print(res.text)

