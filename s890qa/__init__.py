import datetime
import os
import sys

import requests
from bs4 import BeautifulSoup

import common

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
proxy_ip = common.get_ip()


def write_txt(params):
    pre_url = params['pre_url']
    done_down_txt = os.getcwd() + os.sep + params['done_down_txt']
    start_page = params['start_page']
    end_page = params['end_page']
    down_url = params['down_url']
    with open(done_down_txt, 'a+') as fileObj:
        read_lines = fileObj.read().splitlines()
    temp = 0
    for i in range(start_page, end_page):
        print('第' + str(i) + '页')
        url = down_url % i

        if i == 1:
            # url = "https://www.790nd.com/piclist5/index.html"
            url = url.split('_')[0] + '.html'
        print(url)
        html = requests.get(url, headers=header, proxies=proxy_ip)

        html.encoding = 'utf-8'

        soup = BeautifulSoup(html.text, 'lxml')
        itemUrl = soup.select(
            "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='list'] table[class='listt'] tbody tr td[class='listtitletxt'] a")

        for j in range(0, len(itemUrl)):
            file_url = itemUrl[j].get('href')
            print('file_url:' + file_url)
            if file_url.startswith("http"):
                continue
            else:
                os.chdir(os.getcwd())
                url_num = file_url.split('piclist5')[1].split('.')[0].split('/')[1]
                if url_num not in read_lines:
                    with open(done_down_txt, 'a+') as downObj:
                        downObj.write(url_num + '\n')
                    fileUrl = pre_url + file_url
                    temp += 1
                    with open('tpzp-%s-%i.text' % (common.get_datetime('%Y-%m-%d'), temp // 500), 'a+') as f:
                        f.write(fileUrl + '\n')
    print("打印完成")
