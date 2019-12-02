#!/usr/bin/env python3
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
# path = 'G:/down/667xs/自拍偷拍/'

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)
proxy_ip = common.get_ip()
print(curDir)
pre_url = 'https://www.790nd.com'
# 用get方法打开url并发送headers
temp = 0
os.chdir(curDir)
with open(curDir + '/done_down_mrqc.txt', 'a+') as fileObj:
    read_lines = fileObj.readlines()

for i in range(1, 572):
    print('第' + str(i) + '页')
    url = "https://www.790nd.com/piclist4/index_" + str(i) + ".html"
    if i == 1:
        url = "https://www.790nd.com/piclist4/index.html"
    print(url)
    html = requests.get(url, headers=header, proxies=proxy_ip)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='list'] table[class='listt'] tbody tr td[class='listtitletxt'] a")

    for j in range(0, len(itemUrl)):
        file_url = itemUrl[j].get('href')
        print('file_url:' + file_url)
        if file_url.startswith("http"):
            continue
        else:
            url_num = file_url.split('piclist4')[1].split('.')[0].split('/')[1]
            if url_num not in read_lines:
                with open(curDir + '/done_down_mrqc.txt', 'a+') as downObj:
                    downObj.write(url_num + '\n')
                fileUrl = pre_url + file_url
                temp += 1
                # os.chdir(path)
                f = open('mrqc-' + datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.text',
                         'a+')
                f.write(fileUrl + '\n')
                f.close()
print("打印完成")
