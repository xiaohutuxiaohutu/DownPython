#!/usr/bin/env python3
import zhihu
from multiprocessing import Process
import threading
import os
import common

userPath = os.path.expanduser('~') + os.sep
down_path = userPath + 'Pictures/zhihu'


# 获取当前保存quest_id对应的文件列表
def get_file_txt(file_type, cur_dir):
  result_map = {}
  for root, dirs, files in os.walk(cur_dir):
    for file in files:

      if os.path.splitext(file)[1] == ('.' + file_type):
        quest_id = int(file.split('_')[0])
        values = result_map.get(quest_id)
        if values is None or values == 'None':
          file_list = [os.path.join(root, file)]
          result_map[quest_id] = file_list
        else:
          values.append(os.path.join(root, file))
          result_map[quest_id] = values
  return result_map


# 下载图片方法
def down_zhihu_pic(down_path, question_id, file_list):
  url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
  soup = common.get_beauty_soup(url)
  title = common.replace_sub(soup.title.string)
  print(title)
  down_path = down_path + os.sep + title
  if not (os.path.exists(down_path)):
    os.makedirs(down_path)
  for num, file_name in enumerate(file_list, 1):
    print('下载第' + str(num) + '个文件：' + file_name)
    with open(file_name, 'r') as fileObject:
      for num, value in enumerate(fileObject, 1):
        print('第%i行' % (num), end=' ; ')
        img_url = value.strip('\n')
        if img_url == '':
          print('当前行为空：%i line' % num)
          continue
        image_name = img_url.split("/")[-1]
        os.chdir(down_path)
        if not os.path.exists(image_name):
          print('下载第%i个：%s' % (num, img_url), end=" ; ")
          common.down_img(img_url)
        else:
          print('第' + str(num + 1) + '个已存在:' + img_url)
      print(file_name + "-----down over----------------")
    print('删除文件：' + file_name)
    os.remove(file_name)
  print("-----***************down all over********************----------------")


if __name__ == '__main__':
  file_map = get_file_txt('txt', os.getcwd())
  if file_map is None or len(file_map) == 0:
    print()
  else:
    for key, value in file_map.items():
      # print(key)
      # print(value)
      # p = Process(target=down_zhihu_pic, args=(down_path, key, value,))
      # p.start()
      # p.join()
      t = threading.Thread(target=down_zhihu_pic, args=(down_path, key, value,))
      t.setDaemon(True)
      t.start()
    t.join()
