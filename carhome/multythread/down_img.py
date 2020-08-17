import os
import math
import requests
from time import time
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent import futures
import common
import re
import io
import carhome


# 获取当前链接的所有图片链接
def get_img_url(url):
  html = requests.get(url, headers=carhome.header, proxies=carhome.proxy_ip)
  # html.encoding = 'utf-8'
  soup = BeautifulSoup(html.text, 'lxml')
  title = soup.title.string
  results = soup.select("div[class='conmain'] div div div div[class='conttxt'] div div[class='tz-figure'] img")
  print('当前行图片数量为：%i' % len(results))
  if len(results) > 0:
    fs = []
    print('正在调用多线程获取所有的图片,请稍后。。。。。。')
    executor = futures.ThreadPoolExecutor(max_workers=5)
    for index in range(0, len(results)):
      img_url = 'https:'
      src = results[index].get('src')
      if 'lazyload.png' in src:
        src = results[index].get('src9')
      if 'smiles' in src:
        continue
      # 提交任务到线程池
      f = executor.submit(down_img, img_url + src, 'C:\\Users\\xiaohutu\\Pictures\\carhome\\', title)
      fs.append(f)
    # 等待这些任务全部完成
    futures.wait(fs)


# 根据图片链接下载图片
def down_img(img_url, down_path, title):
  # print(img_url)
  path = down_path + title + '/'
  print(path)
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
        print('第 %i 行： %s ' % (num, line), sep=';')
        get_img_url(line)
    os.remove(file_name)
