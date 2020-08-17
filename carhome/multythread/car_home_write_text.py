#!/usr/bin/env python3
import os
from concurrent import futures

import requests
from bs4 import BeautifulSoup

import carhome
import common


def get_page_list(page_url):
    html = requests.get(page_url, headers=carhome.header, proxies=carhome.proxy_ip)
    # html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.title.string
    results = soup.select("body div div[class='choise-con'] ul[class='content'] li div[class='pic-box'] a")
    print('当前页获取到的连接数：%i' % len(results))
    # 写入文件
    num = 0
    if len(results) > 0:
        for index in range(0, len(results)):
            result = 'https:%s' % results[index].get('href')
            if result in done_list:
                print("当前链接已下载")
                continue
            else:
                num += 1
                file_name = '%s-%s_%i.txt' % (title, common.get_datetime('%Y-%m-%d_%H%M'), num // 500)
                with open(file_name, 'a+') as fileObj:
                    fileObj.write(result + '\n')
                # 保存已下载的连接，防止重复下载
                with open('car_home_done.text', 'a+') as fileO:
                    fileO.write(result + '\n')


# 获取已下载文件李斌的连接，防止重复下载
def get_done_list():
    os.chdir(os.getcwd())
    with open('car_home_done.text') as doneObj:
        readiness = doneObj.read().splitlines()
        return readiness


done_list = get_done_list()

if __name__ == '__main__':
    fs = []
    print('正在调用多线程获取当前页面的所有连接,请稍后。。。。。。')
    executor = futures.ThreadPoolExecutor(max_workers=5)
    for i in range(10, 20):
        cur_page = 'https://club.autohome.com.cn/JingXuan/104/%i' % i
        print(cur_page)
        # 提交任务到线程池
        f = executor.submit(get_page_list, cur_page)
        fs.append(f)
        # 等待这些任务全部完成
    futures.wait(fs)
    # as_completed 接收一个future 列表，返回值是一个迭代器，在运行结束后产出future
    for future in futures.as_completed(fs):
        res = future.result()
        msg = '{} result: {!r}'
        print(msg.format(future, res))
