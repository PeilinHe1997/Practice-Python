import re
import requests
import urllib.request
import urllib.parse

url = "https://lms.uzh.ch/raw/591d754:591d7541dac63c9456a1ec0abaf19b660b8072e5/themes/olat/images/logo-2x.png"
headers = {"Cookie":'_ga=GA1.2.43608171.1645536747; JSESSIONID=A69FCC56CC58AADF5B2E7001BDF78351; QueueITAccepted-SDFrts345E-V3_lmsprod=EventId=lmsprod&QueueId=2bc0fd58-3252-4d7e-aee7-f52d90974c57&RedirectType=safetynet&IssueTime=1652883402&Hash=15ada552a4d7a8ada04708d8d2760ea6a4b5deb1ab26c8ecb7b49f9bcfd2f653; _shibsession_64656661756c7468747470733a2f2f6c6d732e757a682e63682f73686962626f6c657468=_e3b5b8cec460962eb9ff550025676ee4'}
res = requests.get(url,headers = headers)
print(res.text)# 打印一个图片

print("-------------这是一条分割线------------------")


url2 = "https://www.douban.com/note/808856021/"
headers2 = {"Cookie":'ll="108242"; bid=DSFV75YXnwM; __utmc=30149280; __utmz=30149280.1652882205.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.8cb4=4a9af580b856803c.1643852331.3.1652884841.1652882202.; _pk_ses.100001.8cb4=*; __utma=30149280.1206754914.1652882205.1652882205.1652884846.2; __utmt=1; __utmb=30149280.1.10.1652884846'}
res2 = requests.get(url2,headers = headers2)
print(res2.text)
