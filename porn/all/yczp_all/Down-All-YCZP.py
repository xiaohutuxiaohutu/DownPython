import requests
from bs4 import BeautifulSoup
import os
import sys
import re
import datetime
import common
import porn
# curDir = os.path.abspath(os.curdir) + os.sep
#     return curDir  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")
# down_file_path = porn.DOWN_PATH_YCZP_D
# down_file_path = porn.DOWN_PATH_YCZP_F
down_file_path = porn.DOWN_PATH_YCZP_OS
if not os.name == 'nt':
    down_file_path = porn.DOWN_PATH_WAWQ_Linux

preUrl = 'https://f.wonderfulday30.live/'
# 文件下载保存路径
osPrePath = down_file_path
if not (os.path.exists(osPrePath)):
    os.makedirs(osPrePath)
header = common.header
file_list = common.get_file_name_list(os.getcwd(), 'txt')
for index, file_name in enumerate(file_list, 1):
    print('down the %i file： %s' % (index, file_name))
    # 打开文件
    with open(file_name) as file:
        for num, value in enumerate(file, 1):
            print('第' + str(num) + '行：')
            line = value.strip('\n')
            if line == '':
                continue
            print(line)
            # 获取代理服务器
            proxyip = common.get_ip()

            html = requests.get(line, headers=header, proxies=proxyip)
            html.encoding = 'utf-8'
            itemSoup = BeautifulSoup(html.text, 'lxml')
            title = itemSoup.title.string
            title = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+', '', title)
            ind = title.index('-')
            newTitle = title[0:ind]

            print(str(newTitle.strip()))

            imgUrls = itemSoup.select(
                "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td p font img[file]")
            imgUrls2 = itemSoup.select(
                "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
            imgUrls1 = itemSoup.select(
                "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
            print('图片数量：' + str(len(imgUrls)))
            print('图片数量1：' + str(len(imgUrls1)))
            print('图片数量2：' + str(len(imgUrls2)))
            if len(imgUrls) == 0 and len(imgUrls1) == 0 and len(imgUrls2) == 0:
                os.chdir(osPrePath)
                fc = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.txt', 'a+')
                fc.write(line + '\n')
                fc.close()
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
                        print(image_name + "-已存在")
                    # time.sleep(5)
                for i in range(0, len(imgUrls1)):
                    print(i)
                    fileUrl1 = imgUrls1[i].get('file')
                    fileUrl1 = preUrl + fileUrl1
                    image_name1 = fileUrl1.split("/")[-1]

                    # 判断文件或文件夹是否存在
                    if not os.path.exists(image_name1):
                        print('下载第' + str(i + 1) + '个:' + fileUrl1)
                        imageUrl1 = requests.get(fileUrl1, headers=header)
                        f = open(image_name1, 'wb')
                        f.write(imageUrl1.content)
                        f.close()
                    else:
                        print(image_name1 + "-1已存在")
                for i in range(0, len(imgUrls2)):
                    fileUrl2 = imgUrls2[i].get('file')
                    fileUrl2 = preUrl + fileUrl2
                    image_name2 = fileUrl2.split("/")[-1]
                    # 判断文件或文件夹是否存在
                    if not os.path.exists(image_name2):
                        print('下载第' + str(i + 1) + '个:' + fileUrl2)
                        imageUrl2 = requests.get(fileUrl2, headers=header)
                        f = open(image_name2, 'wb')
                        f.write(imageUrl2.content)
                        f.close()
                    else:
                        print(image_name2 + "-2已存在")
                print("-----down over----------------")

print("all over")
