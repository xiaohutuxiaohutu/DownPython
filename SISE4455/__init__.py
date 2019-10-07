import common
import datetime
import requests
from bs4 import BeautifulSoup
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

proxy_ip = common.get_ip()


def write_to_txt(params):
    cur_dir = params['cur_dir']
    pre_url = params['pre_url']
    down_url = params['down_url']
    start_page = params['start_page']
    end_page = params['end_page']
    temp = 0
    for i in range(start_page, end_page):
        print('第' + str(i) + '页')
        # url = "https://www.4455sk.com/tupian/list-偷拍自拍-" + str(i) + ".html"
        url = down_url % (i)
        print(url)
        html = requests.get(url, headers=header, proxies=proxy_ip)

        html.encoding = 'utf-8'

        soup = BeautifulSoup(html.text, 'lxml')
        itemUrl = soup.select(
            "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a")

        for j in range(0, len(itemUrl)):
            fileUrl = itemUrl[j].get('href')
            # print('fileUrl:'+fileUrl)
            if fileUrl is not None and fileUrl.find('.html') >= 0:
                fileUrl = pre_url + fileUrl
                temp += 1
                print("fileUrl:" + fileUrl)
                os.chdir(cur_dir)
                file_name = '%s_%i.txt' % (datetime.datetime.now().strftime('%Y-%m-%d'), temp // 500)
                f = open(file_name, 'a+')
                f.write(fileUrl + '\n')
                f.close()
