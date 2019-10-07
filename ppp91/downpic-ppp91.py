import datetime
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
import common

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
down_path = 'D:/图片/PPP91/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
file_path = curDir + '/zipai_2018-09-01_0.txt'
file = open(file_path)
# 获取总行数
for num, value in enumerate(file, 1):
    # print('第'+str(num)+'行：')
    line = value.strip('\n')
    print('第%i行:%s' % (num, line))
    # 获取代理服务器
    proxy_ip = common.get_ip()
    try:
        html = requests.get(line, headers=header, proxies=proxy_ip, timeout=10)
        html.encoding = 'utf-8'
        itemSoup = BeautifulSoup(html.text, 'lxml')
        title = itemSoup.title.string
        title = common.replace_special_char(title)
        ind = title.index('-')
        newTitle = title[0:ind]
        imgUrls = itemSoup.select("body div[class='main'] div[class='contentList'] div[class='content'] p img")

        print('name：%s；图片个数：%s' % (str(newTitle.strip()), str(len(imgUrls))))
        total_num = len(imgUrls)
        if total_num > 1:
            path = down_path + str(newTitle.strip()) + '/'
            if not os.path.exists(path):
                os.makedirs(path)
            os.chdir(path)
            for i in range(0, total_num):
                img_url = imgUrls[i].get('src')
                image_name = img_url.split("/")[-1]
                print('下载第' + str(num) + '行； 第' + str(i + 1) + '  / ' + str(total_num) + '  个: ' + img_url)
                try:
                    imageUrl = requests.get(img_url, headers=header, proxies=proxy_ip, timeout=15)
                    if imageUrl.status_code == 200:
                        if not (os.path.exists(path)):
                            os.makedirs(path)
                        os.chdir(path)
                        f = open(image_name, 'wb')
                        f.write(imageUrl.content)
                        f.close()
                except requests.exceptions.RequestException:
                    # restart+=1
                    print('--第%i：---%s连接错误----' % (i + 1, img_url))
                    # print('尝试第%i次连接'%restart)
            print("---------------------")
    except requests.exceptions.RequestException:
        print('第%i行:%s---连接超时' % (num, line))
file.close
os.remove(file_path)
print("all over")