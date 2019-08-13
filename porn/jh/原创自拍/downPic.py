import requests
from bs4 import BeautifulSoup
import os
import sys
import imghdr
import time
import io
import re
import datetime
import common

sys.path.append(r"C:\workspace\GitHub\DownPython\common")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

file = open("D:/TP/91/jhy/原创自拍/2019-03-09_0.txt")

preUrl = 'https://f.wonderfulday30.live/'
osPrePath = 'C:/Users/23948/Pictures/Camera Roll/jh/'

# 获取总行数
for num, value in enumerate(file, 1):
    print('第' + str(num) + '行：')
    line = value.strip('\n')
    print(line)
    # 获取代理服务器
    proxyip = common.get_ip()
    print('proxyip:' + str(proxyip))

    html = requests.get(line, headers=header, proxies=proxyip)
    html.encoding = 'utf-8'
    itemSoup = BeautifulSoup(html.text, 'lxml')
    title = itemSoup.title.string
    title = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+', '', title)
    ind = title.index('-')
    newTitle = title[0:ind]

    print(str(newTitle.strip()))
    # print(title)
    imgUrls = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    imgUrls2 = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    imgUrls1 = itemSoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    print('图片数量：' + str(len(imgUrls)))
    print('图片数量1：' + str(len(imgUrls1)))
    print('图片数量2：' + str(len(imgUrls2)))
    if len(imgUrls) == 0 and len(imgUrls1) == 0 and len(imgUrls2) == 0:
        if not (os.path.exists(osPrePath)):
            os.makedirs(osPrePath)
        os.chdir(osPrePath)
        f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.txt', 'a+')
        f.write('第' + str(num) + '行：' + line + ',' + newTitle + '\n')
        f.close()
    else:
        path = osPrePath + datetime.datetime.now().strftime('%Y-%m-%d') + '/' + str(newTitle.strip()) + '/'
        if not (os.path.exists(path)):
            os.makedirs(path)
        os.chdir(path)
        for i in range(0, len(imgUrls)):
            fileUrl = imgUrls[i].get('file')
            fileUrl = preUrl + fileUrl

            image_name = fileUrl.split("/")[-1]
            # 判断文件或文件夹是否存在
            if not os.path.exists(image_name):
                print('下载第' + str(i + 1) + '个:' + fileUrl)
                imageUrl = requests.get(fileUrl, headers=header)
                f = open(image_name, 'wb')
                f.write(imageUrl.content)
                f.close()
            else:
                print(image_name + "-1已存在")
        for i in range(0, len(imgUrls1)):
            fileUrl1 = imgUrls1[i].get('file')
            fileUrl1 = preUrl + fileUrl1
            print('fileUrl1:' + fileUrl1)
            image_name1 = fileUrl1.split("/")[-1]
            # 判断文件或文件夹是否存在
            if not os.path.exists(image_name1):
                print('下载第' + str(i + 1) + '个:' + fileUrl)
                imageUrl = requests.get(fileUrl, headers=header)
                f = open(image_name1, 'wb')
                f.write(imageUrl.content)
                f.close()
            else:
                print(image_name1 + "-1已存在")
        for i in range(0, len(imgUrls2)):
            fileUrl2 = imgUrls2[i].get('file')
            fileUrl2 = preUrl + fileUrl2
            image_name2 = fileUrl2.split("/")[-1]
            # 判断文件或文件夹是否存在
            if not os.path.exists(image_name2):
                print('下载第' + str(i + 1) + '个:' + fileUrl)
                imageUrl = requests.get(fileUrl, headers=header)
                f = open(image_name2, 'wb')
                f.write(imageUrl.content)
                f.close()
            else:
                print(image_name2 + "-1已存在")
    print("-----down over----------------")
file.close
print("all over")
