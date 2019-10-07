import datetime
import os
import sys
import requests
from bs4 import BeautifulSoup

import common

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

pre_url = 'http://www.h7j2.com'
# 用get方法打开url并发送headers
temp = 0
for i in range(1, 400):
    print('第' + str(i) + '页')
    url = ''
    'http://www.h7j2.com/AAtupian/AAAtb/zipai/index-2.html'
    if (i == 1):
        url = 'http://www.h7j2.com/AAtupian/AAAtb/zipai/'
    else:
        url = "http://www.h7j2.com/AAtupian/AAAtb/zipai/index-" + str(i) + ".html"
    print(url)
    proxy_ip = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxy_ip)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select("body div[class='main'] li a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        fileU = pre_url + fileUrl
        temp += 1
        print("fileUrl:" + fileUrl)
        os.chdir(curDir)
        with open(datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+') as f:
            f.write(fileU + '\n')
print("打印完成")
