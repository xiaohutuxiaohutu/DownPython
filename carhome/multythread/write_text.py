import os
import math
import requests
from time import time
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent import futures
import common
import re
import carhome

page_url = 'https://club.autohome.com.cn/JingXuan/104/%i'


#
# header = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#
#   'cookie': 'fvlid=1597625585953zQdtJ1EJ4L; sessionip=61.144.97.195; sessionid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; autoid=ac8e7bc62f1d44610e0ccf927310f83b; sessionvid=EF01FBFB-A52F-4D65-A006-FF0739E0F586; area=440113; ahpau=1; __ah_uuid_ng=c_E554438A-793F-4510-A2D6-7E3FC7DEA18E; sessionuid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; pvidchain=6842494,3311253; ahpvno=5; v_no=5; visit_info_ad=E554438A-793F-4510-A2D6-7E3FC7DEA18E||EF01FBFB-A52F-4D65-A006-FF0739E0F586||-1||-1||5; ahrlid=1597625641002gTVBP9NgZm-1597625642889; ref=www.baidu.com%7C0%7C0%7C0%7C2020-08-17+08%3A54%3A03.773%7C2020-08-17+08%3A53%3A06.504'
# }


def get_page_list(page_url):
  # proxy_ip = common.get_ip()
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
        with open('done.text', 'a+') as fileO:
          fileO.write(result + '\n')
      # print(results[index].get('href'))


# 获取已下载文件李斌的连接，防止重复下载
def get_done_list():
  os.chdir(os.getcwd())
  with open('done.text') as doneObj:
    readlines = doneObj.read().splitlines()
    # readlines = doneObj.readlines()
    # print(readlines)
    return readlines


done_list = get_done_list()

if __name__ == '__main__':
  fs = []
  print('正在调用多线程获取所有的图集连接,请稍后。。。。。。')
  executor = futures.ThreadPoolExecutor(max_workers=5)
  for i in range(1, 10):
    cur_page = page_url % i
    print(cur_page)
    # 提交任务到线程池
    f = executor.submit(get_page_list, cur_page)
    fs.append(f)
    # 等待这些任务全部完成
  futures.wait(fs)
