#!/usr/bin/env python3
import os
import threading
import common
import porn
from furl import furl

down_param = {
  'down_url': porn.down_url_zpdr_jh,
  'start_page': 1,
  'end_page': 3
}
cur_dir = os.getcwd() + os.sep


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num, title):
  file_name = '%s-%s_%i.txt' % (title, common.get_datetime('%Y-%m-%d_%H%M'), num // 500)
  with open(file_name, 'a+') as f:
    f.write(file_down_url + '\n')
  # 保存已下载的连接，防止重复下载
  with open(done_down_text, 'a+') as f:
    f.write(pic_href + '\n')


# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_jh_thread(down_url, start_page, end_page, proxy_ip_list):
  f = furl(down_url)
  filter_ = f.args['filter']
  fid_ = f.args['fid']  # 分类
  isdigit = str(filter_).isdigit()  # False  精华 True 普通
  file_dir = ''
  if fid_ == '19' and not isdigit:
    file_dir = '..\jh\zpdr_ycsq_jh'
  elif fid_ == '19' and isdigit:
    file_dir = '../all/zpdr_ycsq_all'
  elif fid_ == '21' and not isdigit:
    file_dir = '..\jh\wawq_jh'
  elif fid_ == '21' and isdigit:
    file_dir = '../all/wawq_all'
  elif fid_ == '33':
    file_dir = '../all/xqfx'
  file_name_list = common.get_file_name_list(file_dir, 'text')
  if file_name_list is None and len(file_name_list) == 0:
    return
  with open(file_name_list[0]) as fileObj:
    # readLines = fileObj.readlines()
    readLines = fileObj.read().splitlines()

  temp = 0

  for i in range(start_page, end_page):
    print('Page' + str(i) + ':')
    url = porn.pre_url + down_url % i
    # print(url)
    proxy_ip = common.get_random_ip(ip_list)
    soup = common.get_beauty_soup(url,proxy_ip)
    title = common.replace_sub(soup.title.string).strip()
    new_title = title if isdigit else title + '_JH'
    print(new_title)
    item_url = soup.select(
      "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(item_url)):
      sort_href = item_url[j].get('href')
      # print(sort_href)
      file_url = porn.pre_url + sort_href
      split = sort_href.split("&")
      item_name = split[0]
      name_split = item_name.split("=")
      split_ = name_split[1]
      temp += 1
      os.chdir(cur_dir)
      # print(item_name)
      if split_ not in readLines:
        print('down the %i : %s ' % ((j + 1), file_url))
        save_url_down(file_name_list[0], file_url, split_, temp, new_title)
      else:
        print('the ' + str(j + 1) + ' is exist:' + file_url)

  print("print over ")


if __name__ == '__main__':
  ip_list = common.get_ip_list(common.ipUrl)
  down_url = [porn.down_url_zpdr, porn.down_url_zpdr_jh, porn.down_url_wawq, porn.down_url_xqfx]
  for index in range(0, len(down_url)):
    t = threading.Thread(target=write_jh_thread, args=(down_url[index], 1, 5, ip_list,))
    t.setDaemon(True)
    t.start()
  t.join()
