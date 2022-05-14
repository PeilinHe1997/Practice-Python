import urllib.request
import urllib.parse
import re
import random


ugList = ["Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/543.50",
          "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
          "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"]

header = {"User-Agent":random.choice(ugList)}
print(header)

'''
https://tieba.baidu.com/f?kw=%E9%9B%85%E6%80%9D&ie=utf-8&pn=0  # 第一页 (1-1)*50
https://tieba.baidu.com/f?kw=%E9%9B%85%E6%80%9D&ie=utf-8&pn=50 # 第二页 (2-1)*50
https://tieba.baidu.com/f?kw=%E9%9B%85%E6%80%9D&ie=utf-8&pn=100 # 第三页 (3-1)*50
https://tieba.baidu.com/f?kw=%E9%9B%85%E6%80%9D&ie=utf-8&pn=150 # 第四页 (4-1)*50
https://tieba.baidu.com/f?kw=%E9%9B%85%E6%80%9D&ie=utf-8&pn=200 # 第五页 (5-1)*50

'''
def loadpage(allurl):
    print("---------正在下载---------")
    urr = urllib.request.Request(allurl, headers = header)
    response = urllib.request.urlopen(urr).read() # response为html页面内容,未被解码,bytes格式
    return response


def savepage(html,fileName):
    print("---------正在保存---------")
    f = open(fileName,"wb")
    f.write(html)    # 将html写入file里面
    f.close()

def getallurl(url, keyvalue, startpage,endpage):
#获取所有页的url
    for i in range(startpage,endpage+1):
        allurl = url + keyvalue + "&pn=" + str((i-1)*50)
        print(allurl)
        # 定义输出文件的路径
        fileName = r"C:\Users\84021\Desktop\PythonLearning_zhou\29 爬虫——百度贴吧\\" + r"\第"+ str(i) + "页爬虫.html"
        # loadpage函数
        html = loadpage(allurl)
        savepage(html,fileName)


# 第二步:输出指定页
# 程序执行的入口
if __name__ == "__main__":
    kw = input("请输入贴吧:")
    startpage = int(input("请输入起始页码:"))
    endpage = int(input("请输入终止页码:"))
    url = "https://tieba.baidu.com/f?"
    keyvalue = urllib.parse.urlencode({"kw":kw})#解码拼装
    print(keyvalue)
    # 输出指定页
    getallurl(url, keyvalue, startpage, endpage)