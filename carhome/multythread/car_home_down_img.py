#!/usr/bin/env python3
import io
import os
from concurrent import futures
import time
import requests
from bs4 import BeautifulSoup

import carhome
import common

executor = futures.ThreadPoolExecutor(max_workers=5)

user_dir = os.path.expanduser('~') + os.sep

down_path = user_dir + 'Pictures' + os.sep + 'carhome' + os.sep + '%s'


# 获取当前链接的所有图片链接
def get_img_url(url):
    html = requests.get(url, headers=carhome.header, proxies=carhome.proxy_ip)
    # html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    title = common.replace_special_char(soup.title.string)
    print('title: %60s' % title, end=';')
    results = soup.select("div[class='conmain'] div div div div[class='conttxt'] div div[class='tz-figure'] img")
    if len(results) == 0:
        results = soup.select("div[class='topic_detail_main'] div[id='content'] div[class='conmain'] div[id='maxwrap-maintopic'] div div div[class='rconten'] div[class='conttxt'] div p span[class='x-loaded'] img")
        print(len(results))

    if len(results) > 0:
        fs = []
        # print('正在调用多线程获取所有的图片,请稍后。。。。。。')
        path = down_path % title
        print('   图片数量：%3i ' % len(results), end=";   ")
        start = int(time.time() * 1000)
        for index in range(0, len(results)):
            img_url = 'https:'
            src = results[index].get('src')
            if 'lazyload.png' in src:
                src = results[index].get('src9')
            if 'smiles' in src:
                continue
            # 提交任务到线程池
            f = executor.submit(down_img, img_url + src, path)
            fs.append(f)
        # 等待这些任务全部完成
        futures.wait(fs)
        end = int(time.time() * 1000)
        print('用时：%.2f 秒' % ((end - start) / 1000))

    else:
        print('   图片数量：%i ;' % len(results))


# 根据图片链接下载图片
def down_img(img_url, path):
    # print(path)
    common.create_file(path)
    os.chdir(path)
    image_name = img_url.split("/")[-1]
    if not os.path.exists(image_name):
        get_request = requests.get(img_url, headers=carhome.header, proxies=carhome.proxy_ip)
        image = get_request.content
        image_b = io.BytesIO(image).read()
        # print(' 图片大小 : %i kb' % (len(image_b) / 1000))
        if len(image_b) > 0:
            with open(image_name, 'wb') as f:
                f.write(image)


if __name__ == '__main__':
    cur_dir = os.getcwd() + os.sep
    file_list = carhome.get_file_list(cur_dir, 'txt')
    print(file_list)
    for index, file_name in enumerate(file_list, 1):
        print('读取第 %i 个文件： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                if line == '':
                    print('当前行为空：%i line' % num)
                    continue
                print('第 %3i 行： %90s  ' % (num, line), end=';  ')
                get_img_url(line)
        os.remove(file_name)
