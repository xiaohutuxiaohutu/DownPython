#!/usr/bin/env python3
import datetime
import os
import sys

import common
import xs

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

proxyipurl = 'http://www.xicidaili.com/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'
curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

down_path = 'D:/图片/667xs/自拍偷拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'

xs.xs_down_pic(down_path, curDir, '_自拍偷拍')
common.del_old_Undown_Text(curDir)
print("all over")
