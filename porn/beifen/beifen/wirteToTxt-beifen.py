import datetime
import os
import sys

import requests
from bs4 import BeautifulSoup

import common

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

# 用get方法打开url并发送headers
temp = 0
preUrl = 'https://f.wonderfulday30.live/'
listTagName = ['img']
# print(curDir)
for i in range(49, 50):
    print('第' + str(i) + '页')
    url = "http://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=" + str(i)
    print(url)
    proxyIp = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyIp)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        # print('fileUrl:'+fileUrl)
        fileUrl = preUrl + fileUrl
        temp += 1
        os.chdir(curDir)
        f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
        f.write(fileUrl + '\n')
        f.close()
print("打印完成")
