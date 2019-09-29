import requests
from bs4 import BeautifulSoup
import os
import sys
import re
import datetime
import common

curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

file = open(curDir + "/2019-08-13_0.txt")
preUrl = 'https://f.wonderfulday30.live/'

userPath = os.path.expanduser('~')  # 获取用户目录
downFilePath = userPath + '/Pictures/Camera Roll/jh/自拍达人原创申请/'
# 获取总行数
for num, value in enumerate(file, 1):
    print('第' + str(num) + '行：')
    line = value.strip('\n')
    print(line)
    # 获取代理服务器
    proxyIp = common.get_ip()
    html = requests.get(line, headers=header, proxies=proxyIp)
    html.encoding = 'utf-8'
    itemSoup = BeautifulSoup(html.text, 'lxml')
    newTitle = common.replaceAndSub(itemSoup.title.string)
    print(str(newTitle.strip()))
    imgUrls = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    imgUrls2 = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    imgUrls1 = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    imgUrls4 = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    imgUrls.extend(imgUrls1)
    imgUrls.extend(imgUrls2)
    imgUrls.extend(imgUrls4)
    print('图片数量：' + str(len(imgUrls)))
    if len(imgUrls) == 0:
        if not (os.path.exists(downFilePath)):
            os.makedirs(downFilePath)
        os.chdir(downFilePath)
        f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.txt', 'a+')
        f.write('第' + str(num) + '行：' + line + ',' + newTitle + '\n')
        f.close()
    else:
        # path = downFilePath + datetime.datetime.now().strftime('%Y-%m-%d') + '/' + str(newTitle.strip()) + '/'
        path = downFilePath + str(newTitle.strip()) + '/'
        if not (os.path.exists(path)):
            os.makedirs(path)
        os.chdir(path)
        for i in range(0, len(imgUrls)):
            fileUrl = imgUrls[i].get('file')
            fileUrl = fileUrl.replace('http://pic.w26.rocks/', preUrl)
            image_name = fileUrl.split("/")[-1]
            # 判断文件或文件夹是否存在
            if not os.path.exists(image_name):
                print('下载第' + str(i + 1) + '个:' + fileUrl)
                imageUrl = requests.get(fileUrl, headers=header)
                f = open(image_name, 'wb')
                f.write(imageUrl.content)
                f.close()
            else:
                print(image_name + "-已存在")
    print("-----down over----------------")
file.close
print("all over")