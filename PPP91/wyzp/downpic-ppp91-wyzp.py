import datetime
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
import common
import PPP91

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)
if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'
down_path = 'D:/图片/PPP91/网友自拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'

name_list = common.get_file_name_list(curDir, 'txt')
for index, file_name in enumerate(name_list, 1):
    print('下载第' + str(index) + '个文件：' + file_name)
    with open(file_name) as file:
        for num, value in enumerate(file, 1):
            line = value.strip('\n')
            print('第%i行:%s' % (num, line))
            img_urls = PPP91.get_img_urls(line, num)
            path = down_path + img_urls[0] + '/'
            PPP91.down_pic(img_urls[1], path, num)
            # # 获取代理服务器
            # proxy_ip = common.get_ip()
            # try:
            #     html = requests.get(line, headers=header, proxies=proxy_ip, timeout=10)
            #     html.encoding = 'utf-8'
            #     itemSoup = BeautifulSoup(html.text, 'lxml')
            #     title = itemSoup.title.string
            #     title = common.replace_special_char(title)
            #     ind = title.index('-')
            #     newTitle = title[0:ind]
            #     imgUrls = itemSoup.select("body div[class='main'] div[class='contentList'] div[class='content'] p img")
            #
            #     print('name：%s；图片个数：%s' % (str(newTitle.strip()), str(len(imgUrls))))
            #     path = down_path + str(newTitle.strip()) + '/'
            #     PPP91.down_pic(imgUrls, path, num)
            # except requests.exceptions.RequestException:
            #     print('第%i行:%s---连接超时' % (num, line))

    os.remove(file_name)
print("all over")
