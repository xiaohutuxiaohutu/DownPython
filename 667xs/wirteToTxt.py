import requests
from bs4 import BeautifulSoup
import os
import sys
import imghdr
import time
import datetime
import random
from urllib.request import Request
from urllib.request import urlopen
import common

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
path = 'G:/down/667xs/自拍偷拍/'

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)
proxy_ip = common.get_ip()

# 用get方法打开url并发送headers
temp = 0
for i in range(1, 51):
    print('第' + str(i) + '页')
    url = "https://www.790nd.com/piclist3/index_" + str(i) + ".html"
    if (i == 1):
        url = "https://www.790nd.com/piclist3/index.html"
    print(url)
    html = requests.get(url, headers=header, proxies=proxy_ip)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='list'] table[class='listt'] tbody tr td[class='listtitletxt'] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        print('fileUrl:' + fileUrl)
        if fileUrl.startswith("http"):
            continue
        else:
            fileUrl = "https://www.667xs.com" + fileUrl
            temp += 1
            os.chdir(path)
            f = open('667xs_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
            f.write(fileUrl + '\n')
            f.close()
print("打印完成")
