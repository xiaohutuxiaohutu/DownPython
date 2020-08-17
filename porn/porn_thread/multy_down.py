import os
import math
import requests
from time import time
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent import futures
import common
import porn

url = 'https://f.w24.rocks/viewthread.php?tid=385747&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3D2592000'

header = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
  'cookie': '__utmz=195573755.1597541171.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __cfduid=d315cceb3f0dfb6e1169003a060204f531597541175; CzG_fid33=1597557901; CzG_visitedfid=33D19; __utmc=195573755; cf_chl_prog=a15; CzG_oldtopics=D385755D385741D; CzG_fid4=1597570556; __utma=195573755.313373389.1597541171.1597567719.1597570801.8; __utmt=1; cf_clearance=5f14198c9ba8a9cef5324ed7acc0624b59311a26-1597570805-0-1z1613443dzd8af122eze2608030-150; CzG_sid=saTzeJ; __utmb=195573755.2.10.1597570801'

}


def Tmp_get_list_url(self, tmp_url):
  try:

    soup = common.get_beauty_soup2(url)
    title = soup.title.string
  except:
    return [[], 'none']

  new_title = common.replace_sub(title)
  img_url_list = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
  img_url_list_2 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
  img_url_list_3 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
  img_url_list_1 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
  img_url_list.extend(img_url_list_2)
  img_url_list.extend(img_url_list_3)
  img_url_list.extend(img_url_list_1)
  # print('----------- 去重 ------------------')
  new_list = common.list_distinct(img_url_list)
  # print('去重后图片数量：' + str(len(new_list)))
  return [new_list, new_title]


def get_list_url(self):
  fs = []
  print('正在调用多线程获取所有的图集连接,请稍后。。。。。。')
  for tmp in self.url_list[:self.page_u_want]:
    # 提交任务到线程池
    f = executor.submit(self.Tmp_get_list_url, tmp)
    fs.append(f)
  # 等待这些任务全部完成
  futures.wait(fs)
  res = []
  for f in fs: res += f.result()
  return res


def get_img_url_list(url):
  try:
    soup = common.get_beauty_soup(url)
    title = soup.title.string
  except:
    return [[], 'none']

  new_title = common.replace_sub(title)
  img_url_list = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
  img_url_list_2 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
  img_url_list_3 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
  img_url_list_1 = soup.select(
    "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
  img_url_list.extend(img_url_list_2)
  img_url_list.extend(img_url_list_3)
  img_url_list.extend(img_url_list_1)
  # print('----------- 去重 ------------------')
  new_list = common.list_distinct(img_url_list)
  # print('去重后图片数量：' + str(len(new_list)))
  return [new_list, new_title]


if __name__ == '__main__':
  ip_list = common.get_ip_list('https://www.kuaidaili.com/free/intr/')
  img_url_list = get_img_url_list(url)
  executor = futures.ThreadPoolExecutor(max_workers=5)
  print('正在调用多线程，下载全部图片')
  fs = []
  for img_url in img_url_list[0]:
    file_url = img_url.get('file')
    print("fileurl:   " + file_url)
    image_name = file_url.split("/")[-1]
    f = executor.submit(common.down_img2(img_url, common.get_random_ip(ip_list)))
    fs.append(f)
  futures.wait(fs)


def Tmp_download_image(self, url):
  res = self.sesn.get(url)
  with open(self.path1 + '/' + ('_'.join(url.split('/')[-2:])), 'wb') as file:
    # 将数据的二进制形式写入文件中
    file.write(res.content)


def download_image(self):
  urls_list = self.get_download_url()
  print('正在调用多线程，下载全部图片')
  fs = []
  for url in urls_list:
    f = executor.submit(self.Tmp_download_image, url)
    fs.append(f)
  futures.wait(fs)
