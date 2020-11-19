#!/usr/bin/env python3
import os
import threading
import common

# import porn
# from furl import furl
# from pypinyin import pinyin, lazy_pinyin, Style
import pypinyin
from pypinyin import Style

user_dir = os.path.expanduser('~') + os.sep;

down_path_c = user_dir + 'Pictures/Camera Roll/PORN/'
if not os.name == 'nt':
    down_file_path = '/usr/local/src/PORN/'

# 获取当前月份
cur_month = os.sep + common.get_datetime('%Y-%m') + os.sep
cur_dir = os.getcwd() + os.sep

gLock = threading.Lock()


def down_all_pic(category_name, file_list, ip_list):
    gLock.acquire()
    print("---------------- 所有文件下载完毕 -------------------")
    gLock.release()


if __name__ == '__main__':
    file_map = {}
    ip_list = common.get_ip_list(common.ipUrl)
    threads = []
    for key, value in file_map.items():
        t = threading.Thread(target=down_all_pic, args=(key, value, ip_list,))
        t.setDaemon(True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("所有线程任务完成")
