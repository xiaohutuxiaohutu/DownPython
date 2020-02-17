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

# curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")

header = common.header
path = os.getcwd()
preUrl = 'https://f.w24.rocks/'
down_url = "https://f.w24.rocks/forumdisplay.php?fid=4&orderby=dateline&filter=2592000&page=%i"
temp = 0
for i in range(1, 13):
    print('第' + str(i) + '页')
    url = down_url % i
    print(url)
    # proxyip = common.get_ip()
    # html = requests.get(url, headers=header, proxies=proxyip)
    # html.encoding = 'utf-8'
    # soup = BeautifulSoup(html.text, 'lxml')
    soup = common.get_beauty_soup(url)
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        # print('fileUrl:'+fileUrl)
        fileUrl = preUrl + fileUrl
        temp += 1
        os.chdir(path)
        # f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
        f = open('%s_%i.txt' % (datetime.datetime.now().strftime('%Y-%m-%d'), temp // 500), 'a+')
        f.write(fileUrl + '\n')
        f.close()
print("打印完成")
