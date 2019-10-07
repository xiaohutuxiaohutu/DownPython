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
ISOTIMEFORMAT = '%Y-%m-%d %X'

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

down_path = 'D:/图片/667xs/自拍偷拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
proxy_ip = common.get_ip()
file_path = curDir + '/667xs_2019-02-24_0.txt'
file = open(file_path)
# 获取总行数
for num, value in enumerate(file, 1):
    line = value.strip('\n')
    print('第' + str(num) + '行： ' + line)
    html = requests.get(line, headers=header, proxies=proxy_ip)
    html.encoding = 'gb2312'
    itemSoup = BeautifulSoup(html.text, "lxml")
    title = itemSoup.title.string
    posi = title.index('_自拍偷拍')
    title = title[0:posi]
    new_title = common.replace_special_char(title).strip()
    print(new_title)
    # print(title)
    imgUrls = itemSoup.select(
        "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='content'] div div[class='n_bd'] img")
    print('图片数量：' + str(len(imgUrls)))
    path = down_path + str(new_title) + '/'
    s = len(imgUrls)
    if len(imgUrls) > 1:
        for i in range(0, len(imgUrls)):
            img_url = imgUrls[i].get('src')
            if img_url.startswith('http://tu.2015img.com'):
                image_name = img_url.split("/")[-1]

                print('下载第' + str(num) + '行； 第' + str(i + 1) + '  / ' + str(s) + '  个: ' + img_url)
                imageUrl = requests.get(img_url, headers=header)
                if not os.path.exists(path):
                    os.makedirs(path)
                os.chdir(path)
                if not os.path.exists(image_name):
                    f = open(image_name, 'wb')
                    f.write(imageUrl.content)
                    f.close()
    print("-----down over----------------")

file.close
os.remove(file_path)
print("all over")
