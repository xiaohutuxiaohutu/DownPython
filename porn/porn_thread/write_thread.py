#!/usr/bin/env python3
import os
import threading
import common
import porn
from furl import furl
import re

cur_dir = os.getcwd() + os.sep
gLock = threading.Lock()


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num, title):
  file_name = '%s-%s_%i.txt' % (title, common.get_datetime('%Y-%m-%d_%H%M'), num // 500)
  with open(file_name, 'a+') as f:
    f.write(file_down_url + '\n')
  # 保存已下载的连接，防止重复下载
  with open(done_down_text, 'a+') as f:
    f.write(pic_href + '\n')


# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_jh_thread(down_url, start_page, end_page, ip_list, readLines, done_file_name):
  temp = 0
  for page_num in range(start_page, end_page):
    print('第 %i 页 ：' % page_num, end=' ')
    # 当前页数不重复的连接：》0读取下一页
    url = porn.pre_url + down_url % page_num
    print(url)
    proxy_ip = common.get_random_ip(ip_list)
    soup = common.get_beauty_soup2(url, proxy_ip)
    title = common.replace_sub(soup.title.string).strip()
    if (title.startswith('91')):
      title = title[2:]
    new_title = title + '_JH'
    print(new_title)
    item_url = soup.select(
      "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")
    print('当前页获取到的连接数：%i' % len(item_url))
    # 当前页不重复的数字
    cur_page_num = 0
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
        print('获取第 %i 个连接: %s ' % ((j + 1), file_url))
        cur_page_num += 1
        save_url_down(done_file_name, file_url, split_, temp, new_title)
    if cur_page_num == 0:
      break
  print("print over ")


# 非精华连接
def write_exclude_jh(down_url, start_page, end_page, ip_list, readLines, done_file_name):
  temp = 0
  for page_num in range(start_page, end_page):
    print('第 %i 页 ：' % page_num, end=' ')
    url = porn.pre_url + down_url % page_num
    print(url)
    soup = common.get_beauty_soup2(url, common.get_random_ip(ip_list))
    title = common.replace_sub(soup.title.string).strip()
    if (title.startswith('91')):
      title = title[2:]
    # 查找所有 id 包含normalthread 的tags
    # 当前页不重复的数字
    cur_page_num = 0
    result_tags = soup.find_all(id=re.compile('normalthread'))
    for tag in result_tags:
      for child in tag.children:
        if len(child) > 1:
          contents1 = child.contents[5]
          contents2 = contents1.contents
          if len(contents2) >= 0:
            flag = True  # 默认不是精华
            for item in range(0, len(contents2)):
              tag_name = contents2[item]
              if tag_name.name in porn.listTagName:
                tag_name_src = tag_name['src']
                rfind = tag_name_src.find('digest_1.gif') >= 0
                if rfind:
                  flag = False
                  break
            contents3 = contents2[3].contents
            if len(contents3) > 0 and flag:
              contents4 = contents3[0]
              pic_href = contents4['href']
              file_down_url = porn.pre_url + pic_href
              split = pic_href.split("&")
              item_name = split[0]
              # contents__string = contents4.string
              name_split = item_name.split("=")
              split_ = name_split[1]
              os.chdir(cur_dir)
              temp += 1
              if split_ not in readLines:
                print('down the %i ge: %s' % (temp, pic_href))
                cur_page_num += 1
                save_url_down(done_file_name, file_down_url, split_, temp, title)
    if cur_page_num == 0:
      break
  print("print over")


def write_common(down_url, start_page, end_page, ip_list):
  gLock.acquire()
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
    readLines = fileObj.read().splitlines()
  if isdigit:
    write_exclude_jh(down_url, start_page, end_page, ip_list, readLines, file_name_list[0])
  else:
    write_jh_thread(down_url, start_page, end_page, ip_list, readLines, file_name_list[0])
  gLock.release()


if __name__ == '__main__':
  ip_list = common.get_ip_list(common.ipUrl)
  down_url = [porn.down_url_zpdr, porn.down_url_zpdr_jh, porn.down_url_wawq, porn.down_url_xqfx]
  threads = []
  for index in range(0, len(down_url)):
    t = threading.Thread(target=write_common, args=(down_url[index], 1, 5, ip_list,))
    t.setDaemon(True)
    threads.append(t)
    t.start()
  for t in threads:
    t.join()

  print("所有线程任务完成")
  # t.join()
