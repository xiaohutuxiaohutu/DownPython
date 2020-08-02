import datetime
import io
import os
import random
import re
import urllib.parse
import urllib.request
# from urlparse import urlsplit
from os.path import basename
from urllib.request import Request
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

if os.name == 'nt':
  print(u'windows system')
else:
  print(u'linux')

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'

# header = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

header = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

  'cookie': '__cfduid=dd258a623447213e3ddb4f6e75ef300071596203860; __utmz=195573755.1596203862.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=195573755; cf_clearance=c1970678bb0d6d407efc03fe125804bd8c252544-1596335014-0-1z79fa549dz49af16edz49fae42c-150; CzG_sid=NuQXci; CzG_fid19=1596334125; __utma=195573755.856032112.1596203862.1596331933.1596335045.7; __utmt=1; CzG_oldtopics=D383959D383873D383858D; CzG_fid33=1596333799; CzG_visitedfid=33D19; __utmb=195573755.2.10.1596335045'
}
default_time_format = '%Y-%m-%d %X'


# 替换特殊字符
def replace_special_char(old_str):
  if old_str is not None:
    new_str = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|：+|:+|【+|】+|\.+|~+|\*+|\.\.\.+|\�+|�+|\？+', '', old_str)
    return new_str.strip()
  else:
    return old_str.strip()


# 替换并截取名字-porn使用
def replace_sub(old_str):
  title = replace_special_char(old_str)
  print('title:' + title)
  ind = title.index('-')
  return title[0:ind]


# 代理地址集合-全局变量
ipList = []


# 获取代理IP
def get_ip_list(proxy_url):
  ip_list = []
  # print(proxy_url)
  request = Request(proxy_url, headers=header)
  response = urlopen(request)
  obj = BeautifulSoup(response, 'lxml')
  # ip_text = obj.findAll('tr', {'class': 'odd'})
  ip_text = obj.findAll('tr')

  if len(ip_text) > 0:
    for i in range(len(ip_text)):
      ip_tag = ip_text[i].findAll('td')
      if len(ip_tag) > 0:
        ip_port = ip_tag[0].get_text() + ':' + ip_tag[1].get_text()
        ip_list.append(ip_port)
  # 检测IP是否可用
  # print(ip_list)
  if len(ip_list) > 0:
    for ip in ip_list:
      try:
        proxy_host = 'https://' + ip
        proxy_temp = {"https:": proxy_host}
        # res = urllib.urlopen(proxy_host, proxies=proxy_temp).read()
        request = Request(proxy_temp, headers=header)
        response = urlopen(request).read()
      except Exception as e:
        ip_list.remove(ip)
        continue
  # print(ip_list)
  return ip_list


# get_ip_list(ipUrl)


# 从IPlist中获取随机地址
def get_random_ip(ip_list):
  # ip_list = get_ip_list(bsObj)
  random_ip = 'http://' + random.choice(ip_list)
  proxy_ip = {'http:': random_ip}
  return proxy_ip


# 从代理地址列表中获取一个随机IP
def get_ip():
  global ipList
  if len(ipList) == 0:
    print("get proxy_ip list ：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    ipList = get_ip_list(ipUrl)
  random_ip = get_random_ip(ipList)
  return random_ip


test_image_url = [
  'http://pic.w26.rocks/attachments//1908131105d9a99e769a3ff3d4.jpg',
  'http://pic.w26.rocks/attachments//1908131059de4602941152bcd6.jpg'
]


def get_cur_dir():
  # 当前文件路径
  # curDir = os.path.abspath(os.curdir) + os.sep
  curDir = os.getcwd() + os.sep
  return curDir


def get_datetime(template):
  return datetime.datetime.now().strftime(template)


# 获取指定目录下 指定类型的文件
def get_file_name_list(file_dir, file_type):
  file_name_list = []
  for root, dirs, files in os.walk(file_dir):
    for file in files:
      if os.path.splitext(file)[1] == ('.' + file_type):
        file_name_list.append(os.path.join(root, file))
  return file_name_list


def image_size(image_url):
  image = requests.get(image_url).content
  image_b = io.BytesIO(image).read()
  size = len(image_b) / 1000
  print(size)
  return size


def file_size(url):
  request = Request(url, headers=header)
  response = urlopen(request).read()
  size = len(response) / 1000
  print(size)
  return size


# 判断文件或文件夹是否存在
def file_exist(file_path):
  return os.path.exists(file_path)


# 判断文件夹是否存在，不存在则创建
def create_file(file_path):
  if not (os.path.exists(file_path)):
    os.makedirs(file_path)


# 根据图片连接保存图片
def down_img(file_url):
  image_name = file_url.split("/")[-1]
  if not os.path.exists(image_name):
    proxy_ip = get_ip()
    # print(file_url)
    get_request = requests.get(file_url, headers=header, proxies=proxy_ip)
    image = get_request.content
    image_b = io.BytesIO(image).read()
    # print(' size : %i kb' % (len(image_b) / 1000))
    print(' 图片大小 : %i kb' % (len(image_b) / 1000))
    if len(image_b) > 0:
      with open(image_name, 'wb') as f:
        f.write(image)
  # else:
  #     print(image_name + "已存在")


# 根据图片连接保存图片
def down_img2(file_url, proxy_ip):
  image_name = file_url.split("/")[-1]
  if not os.path.exists(image_name):
    # proxy_ip = get_ip()
    # print(file_url)
    get_request = requests.get(file_url, headers=header, proxies=proxy_ip)
    image = get_request.content
    image_b = io.BytesIO(image).read()
    # print(' size : %i kb' % (len(image_b) / 1000))
    print(' 图片大小 : %i kb' % (len(image_b) / 1000))
    if len(image_b) > 0:
      with open(image_name, 'wb') as f:
        f.write(image)
  # else:
  #     print(image_name + "已存在")


def down_img_2(img_url, down_path, index):
  response = requests.get(img_url)  # , stream=True
  if response.status_code == 200:
    image = urllib.request.urlopen(img_url).read()
    # response = requests.get(image_url, stream=True) #
    # image = response.content
    try:
      # file_name = dir_name + os.sep + basename(urlsplit(image_url)[2])
      file_name = basename(urllib.parse.urlsplit(img_url)[2])

      with open(down_path + os.sep + '%d.jpg' % index, "wb") as picture:
        picture.write(image)
        print("下载 {} 完成!".format(picture))
    except IOError:
      print("IO Error\n")
      # continue
    finally:
      picture.close
  else:
    print()
    # continue


def mkdir(path):
  if not os.path.exists(path):
    print('新建文件夹:', path)
    os.makedirs(path)
    return True
  else:
    # print("图片存放于:", os.getcwd() + os.sep + path)
    print("图片存放于:", path)
    return False


# 判断文件是否存在
def is_file(file_name):
  return os.path.isfile(file_name)


def get_beauty_soup(url):
  proxy_ip = get_ip()
  html = requests.get(url, headers=header, proxies=proxy_ip)
  html.encoding = 'utf-8'
  return BeautifulSoup(html.text, 'lxml')


def get_beauty_soup2(url, proxy_ip):
  # html = requests.get(url, headers=header, proxies=proxy_ip)
  html = requests.get(url, headers=header)
  # html = requests.get(url, headers=header, timeout=(3.05, 27))
  html.encoding = 'utf-8'
  return BeautifulSoup(html.text, 'lxml')


def get_beauty_soup_encoding(url, encoding):
  proxy_ip = get_ip()
  html = requests.get(url, headers=header, proxies=proxy_ip)
  html.encoding = encoding
  return BeautifulSoup(html.text, 'lxml')


# 排序
def list_distinct(old_list):
  new_list = list(set(old_list))
  # 按照原来顺序去重
  new_list.sort(key=old_list.index)
  return new_list


def get_title(url):
  soup = get_beauty_soup(url)
  new_title = replace_sub(soup.title.string)
  return new_title


def del_old_Undown_Text(file_dir):
  file_list = []
  for root, dirs, files in os.walk(file_dir):
    for file in files:
      if file.endswith('未下载.text'):
        file_list.append(os.path.join(root, file))
    # if len(file_list) >= 2:

    # 删除所有未下载记录文件
    for f in file_list:
      print('删除***未下载.text:' + f)
      os.remove(f)

    # 删除当前日期之前的未下载记录文件
    '''
    file_name = get_datetime('%Y-%m-%d') + '_未下载.text'
        
        
    for f in file_list:
        split = f.split('\\')
        L = len(split) - 1
        if split[L] != file_name:
            print('删除***未下载.text:' + f)
            os.remove(f)
    '''


# 获取当前指定类型的文件
def get_cur_file_list(file_type, pattern):
  file_name_list = []
  for root, dirs, files in os.walk(os.getcwd()):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
      # print(file)
      if os.path.splitext(file)[1] == ('.' + file_type) and pattern in file:
        file_name_list.append(os.path.join(root, file))
  return file_name_list


# 获取当前指定类型的文件
def get_cur_file_list2(file_type, pattern, file_dir):
  file_name_list = []
  for root, dirs, files in os.walk(file_dir):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
      # print(file)
      if os.path.splitext(file)[1] == ('.' + file_type) and pattern in file:
        file_name_list.append(os.path.join(root, file))
  return file_name_list
