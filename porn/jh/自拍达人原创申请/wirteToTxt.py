import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
sys.path.append(r"C:\workspace\GitHub\DownPython")
import common

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
path = 'C:/workspace/GitHub/DownPython/porn/jh/自拍达人原创申请/'
preUrl = 'http://f.w24.rocks/'

# 用get方法打开url并发送headers
temp = 0
for i in range(1, 3):
    print('第' + str(i) + '页')
    url = "http://f.w24.rocks/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=" + str(i)
    print(url)
    proxyip = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyip)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        # print('fileUrl:'+fileUrl)
        fileUrl = preUrl + fileUrl
        temp += 1
        # print(temp)
        # print("fileUrl:"+fileUrl)
        os.chdir(path)
        f = open('jh-' + datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
        f.write(fileUrl + '\n')
        f.close()
print("打印完成")
