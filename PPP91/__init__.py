import os
import common
import requests
import sys
from bs4 import BeautifulSoup
import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}


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
                        print('下载第%i 行； 第 %i  / %i 个： %s' % (row_num, i + 1, total_num, img_url))
                        with open(image_name, 'wb') as f:
                            f.write(imageUrl.content)
                    else:
                        print('第%i 行； 第 %i  / %i 个 已存在： %s' % (row_num, i + 1, total_num, img_url))
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


def down_image(params):
    cur_dir = params['cur_dir']
    down_path = params['down_path']
    # print(cur_dir)
    name_list = common.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(name_list, 1):
        print('下载第' + str(index) + '个文件：' + file_name)
        with open(file_name) as file:
            for num, value in enumerate(file, 1):
                line = value.strip('\n')
                print('第%i行:%s' % (num, line))
                img_urls = get_img_urls(line, num)
                path = down_path + img_urls[0] + '/'
                down_pic(img_urls[1], path, num)
        os.remove(file_name)


def write_txt(params):
    cur_dir = params['cur_dir']
    pre_url = params['pre_url']
    down_url = params['down_url']
    start_page = params['start_page']
    end_page = params['end_page']
    done_down_txt = params['done_down_txt']
    with open(done_down_txt, 'a+') as downObj:
        readlines = downObj.read().splitlines()
    # 用get方法打开url并发送headers
    temp = 0
    for i in range(start_page, end_page):
        print('第' + str(i) + '页')
        url = ''
        if i == 1:
            url = down_url.split('-')[0] + '.html'
        else:
            url = down_url % i
        print(url)
        proxy_ip = common.get_ip()
        html = requests.get(url, headers=header, proxies=proxy_ip)

        html.encoding = 'utf-8'

        soup = BeautifulSoup(html.text, 'lxml')
        itemUrl = soup.select("body div[class='main'] li a")

        for j in range(0, len(itemUrl)):
            fileUrl = itemUrl[j].get('href')
            # print('fileUrl:' + fileUrl)
            fileU = pre_url + fileUrl
            temp += 1
            # print("fileUrl:" + fileUrl)
            os.chdir(cur_dir)
            file_num = fileUrl.split('/')[3].split('.')[0]
            if file_num not in readlines:
                with open(datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+') as f:
                    f.write(fileU + '\n')
                with open(done_down_txt, 'a+') as f:
                    f.write(file_num + '\n')
    print("打印完成")
