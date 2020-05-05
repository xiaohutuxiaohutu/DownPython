import datetime
import io
import os
import random
import re
# from urlparse import urlsplit
from urllib.request import Request
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径

header = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
# pre_url = 'https://f.w24.rocks/'

from common import DoConfig
import sys



class DownPic():
  """下载公共方法"""

  def __init__(self, start_page, end_page, down_path):
    config = DoConfig.DoConfig(sys.path[1] + os.sep + 'common' + os.sep + 'config.ini')
    porn_dict = config.get_dict('porn')
    self.start_page = start_page
    self.end_page = end_page
    self.down_path = down_path
    self.ip_list = []
    self.proxy_url = porn_dict.get('proxy_url')
    self.pre_url = porn_dict.get('pre_url')

  def get_proxy_ip_list(self):
    request = Request(self.proxy_url, headers=header)
    response = urlopen(request)
    obj = BeautifulSoup(response, 'lxml')
    # ip_text = obj.findAll('tr', {'class': 'odd'})
    ip_text = obj.findAll('tr')

    if len(ip_text) > 0:
      for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        if len(ip_tag) > 0:
          ip_port = ip_tag[0].get_text() + ':' + ip_tag[1].get_text()
          self.ip_list.append(ip_port)
    # 检测IP是否可用
    # print(ip_list)
    if len(self.ip_list) > 0:
      for ip in self.ip_list:
        try:
          proxy_host = 'https://' + ip
          proxy_temp = {"https:": proxy_host}
          # res = urllib.urlopen(proxy_host, proxies=proxy_temp).read()
          request = Request(proxy_temp, headers=header)
          response = urlopen(request).read()
        except Exception as e:
          self.ip_list.remove(ip)
          continue

  def get_file_name_list(self, file_dir, file_pattern):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
      for file in files:
        if os.path.splitext(file)[1] == ('.' + file_pattern):
          file_name_list.append(os.path.join(root, file))
    return file_name_list

  def get_datetime(self, template):
    return datetime.datetime.now().strftime(template)

  # 判断文件夹是否存在，不存在则创建
  def create_file(self, file_path):
    if not (os.path.exists(file_path)):
      os.makedirs(file_path)

  def get_cur_file_list(self, file_type, pattern):
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

  def write_to_done_log(self, line, new_title):
    done_file_list = self.get_cur_file_list('log', 'done.log')
    if len(done_file_list) == 0:
      done_log = 'done.log'
    else:
      done_log = done_file_list[0]
      print("done.log:" + done_log)
    with open(done_log, 'a+', encoding='utf-8') as f:
      f.write('%s:[%s,%s]\n' % (self.get_datetime('%Y/%m/%d %H:%M'), line, new_title))

  def get_random_ip(self):
    # ip_list = get_ip_list(bsObj)
    random_ip = 'http://' + random.choice(self.ip_list)
    proxy_ip = {'http:': random_ip}
    return proxy_ip

  # 替换特殊字符
  def replace_special_char(self, old_str):
    if old_str is not None:
      new_str = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|：+|:+|【+|】+|\.+|~+|\*+|\.\.\.+|\�+|�+|\？+', '', old_str)
      return new_str.strip()
    else:
      return old_str.strip()

  # 替换并截取名字-porn使用
  def replace_sub(self, old_str):
    title = self.replace_special_char(old_str)
    ind = title.index('-')
    return title[0:ind]

  def list_distinct(self, old_list):
    new_list = list(set(old_list))
    # 按照原来顺序去重
    new_list.sort(key=old_list.index)
    return new_list

  def get_beauty_soup(self, url):
    proxy_ip = self.get_random_ip
    html = requests.get(url, headers=header, proxies=proxy_ip)
    html.encoding = 'utf-8'
    return BeautifulSoup(html.text, 'lxml')

  def get_img_url_list(self, url):
    try:
      soup = self.get_beauty_soup(url)
      title = soup.title.string
    except:
      return [[], 'none']

    new_title = self.replace_sub(title)
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
    new_list = self.list_distinct(img_url_list)
    # print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]

  # 根据图片连接保存图片
  def down_img(self, file_url):
    image_name = file_url.split("/")[-1]
    if not os.path.exists(image_name):
      proxy_ip = self.get_random_ip()
      # print(file_url)
      get_request = requests.get(file_url, headers=header, proxies=proxy_ip)
      image = get_request.content
      image_b = io.BytesIO(image).read()
      # print(' size : %i kb' % (len(image_b) / 1000))
      print(' 图片大小 : %i kb' % (len(image_b) / 1000))
      if len(image_b) > 0:
        with open(image_name, 'wb') as f:
          f.write(image)

  def save_not_down_url(self, line, new_title, num):
    # name_list = common.get_file_name_list(cur_dir, "log")
    name_list = self.get_file_name_list('log', "un_down.log")
    if len(name_list) == 0:
      file_name = 'un_down.log'
    else:
      file_name = name_list[0]
      print('un_down_file:' + file_name)
    with open(file_name, 'a+', encoding='utf-8') as f:
      # f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n')
      f.write('%s:[%s,%s]\n' % (self.get_datetime('%Y/%m/%d %H:%M'), line, new_title))

  def down_pic(self):
    # 获取当前月份
    cur_month = os.sep + self.get_datetime('%Y-%m') + os.sep
    cur_dir = os.getcwd()
    path_ = self.down_path + cur_month
    if not (os.path.exists(path_)):
      os.makedirs(path_)
    file_name_list = self.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(file_name_list, 1):
      # print('down the %i file： %s' % (index, file_name))
      print('读取第 %i 个文件： %s' % (index, file_name))
      # 打开文件
      with open(file_name) as file_obj:
        for num, value in enumerate(file_obj, 1):
          line = value.strip('\n')
          if line == '':
            print('当前行为空：%i line' % num)
            continue
          # print('the %i line： -%s- ' % (num, line), end=' ;')
          print('第 %i 行： -%s- ' % (num, line), end=' ;')
          # 获取所有图片连接
          url_list = self.get_img_url_list(line)
          img_urls = url_list[0]
          # print(' image num： %i ' % l)
          print(' 图片数量： %i ' % len(img_urls))
          new_title = url_list[1]

          if len(img_urls) < 2:
            os.chdir(cur_dir)
            self.save_not_down_url(line, new_title, num)
          else:
            path = path_ + str(new_title.strip()) + os.sep
            self.create_file(path)
            os.chdir(path)
            for i in range(0, len(img_urls)):
              file_url = img_urls[i].get('file')
              # if not ('http://' in file_url or 'https://' in file_url):
              if not file_url.startswith('http'):
                print('in:' + file_url)
                file_url = self.pre_url + file_url
              # fileUrl = file_url.replace('http://pic.w26.rocks/', pre_url)
              image_name = file_url.split("/")[-1]
              if not os.path.exists(image_name):
                # print('the %i line：the %i  / %i ge : %s' % (num, i + 1, l, file_url), end=' ;')
                print('第 %i 行：第 %i / %i 个 : %s' % (num, i + 1, len(img_urls), file_url), end=' ;')
                self.down_img(file_url)
          # print("-----down over----------------")
          print('第 %i 行： %s 下载完毕 ' % (num, line))
          # 保存所有的下载链接
          os.chdir(cur_dir)
          self.write_to_done_log(line, new_title)
      print('第 %i 个文件： %s 下载完毕，开始删除...' % (index, file_name))
      os.remove(file_name)
      print('第 %i 个文件： %s 删除成功，开始读取下一个文件' % (index, file_name), end=";")
    # print("down all over----------------start delete old undown text-------------------")
    print("---------------- 所有文件下载完毕 -------------------")
    # common.del_old_Undown_Text(cur_dir)
