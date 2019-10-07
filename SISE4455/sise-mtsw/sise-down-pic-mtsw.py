import datetime
import os
import re
import common
import sys
import requests.packages.urllib3.util.ssl_
from bs4 import BeautifulSoup

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

down_path = 'D:/图片/四色AV/自拍偷拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
proxy_ip = common.get_ip()
file_path = curDir + '/2019-01-27_1.txt'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

with open(file_path) as file:
    for num, value in enumerate(file, 1):
        line = value.strip('\n')
        print('第' + str(num) + '行： ' + line)
        # 获取代理服务器
        html = requests.get(line, headers=header, proxies=proxy_ip)
        # html = requests.get(line, headers=header)
        html.encoding = 'utf-8'
        itemSoup = BeautifulSoup(html.text, 'lxml')
        title = itemSoup.title.string
        title = common.replace_special_char(title).strip()
        new_title = title.split('www')[-1]
        print(new_title)

        imgUrls = itemSoup.select("body div[class='maomi-content'] main[id='main-container'] div[class='content'] img")
        img_urls = common.list_distinct(imgUrls)
        print('去重后图片数量：' + str(len(img_urls)))
        s = len(img_urls)
        if s > 1:
            path = down_path + str(new_title) + '/'
            if not (os.path.exists(path)):
                os.makedirs(path)
            os.chdir(path)
            for i in range(0, len(img_urls)):
                img_url = img_urls[i].get('data-original')
                image_name = img_url.split("/")[-1]
                if not os.path.exists(image_name):
                    print('下载第' + str(num) + '行； 第' + str(i + 1) + '  / ' + str(s) + '  个: ' + img_url)
                    imageUrl = requests.get(img_url, headers=header, verify=True)
                    with open(image_name, 'wb') as f:
                        f.write(imageUrl.content)
        print("-----down over----------------")

os.remove(file_path)
print("all over")
