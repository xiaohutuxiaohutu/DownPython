import os
import common
import requests
import sys
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)


def down_pic(img_urls, down_file_path, row_num):
    total_num = len(img_urls)
    if total_num > 1:
        if not os.path.exists(down_file_path):
            os.makedirs(down_file_path)
        os.chdir(down_file_path)
        proxy_ip = common.get_ip()
        for i in range(0, total_num):
            img_url = img_urls[i].get('src')
            image_name = img_url.split("/")[-1]

            try:
                imageUrl = requests.get(img_url, headers=header, proxies=proxy_ip, timeout=15)
                if imageUrl.status_code == 200:
                    if not os.path.exists(image_name):
                        print('下载第' + str(row_num) + '行； 第' + str(i + 1) + '  / ' + str(total_num) + '  个: ' + img_url)
                        with open(image_name, 'wb') as f:
                            f.write(imageUrl.content)
                    else:
                        print(
                            '第' + str(row_num) + '行； 第' + str(i + 1) + '  / ' + str(total_num) + '  个 已存在: ' + img_url)
            except requests.exceptions.RequestException:
                print('--第%i行：第%i / %i 个-- %s连接错误----' % (row_num, i + 1, total_num, img_url))
                # print('尝试第%i次连接'%restart)
        print("---------------------")


def get_img_urls(url, row_num):
    proxy_ip = common.get_ip()
    try:
        html = requests.get(url, headers=header, proxies=proxy_ip, timeout=10)
        html.encoding = 'utf-8'
        itemSoup = BeautifulSoup(html.text, 'lxml')
        title = itemSoup.title.string
        title = common.replace_special_char(title)
        ind = title.index('-')
        new_title = title[0:ind]
        img_url_list = itemSoup.select("body div[class='main'] div[class='contentList'] div[class='content'] p img")
        img_url_list_1 = itemSoup.select("body div[class='main'] div[class='contentList'] div[class='content'] img")
        img_url_list.extend(img_url_list_1)
        # print('----------- 去重 ------------------')
        new_list = common.list_distinct(img_url_list)
        # print('去重后图片数量：' + str(len(new_list)))
        return [new_title, new_list]
    except requests.exceptions.RequestException:
        print('第%i行:%s---连接超时' % (row_num, url))
