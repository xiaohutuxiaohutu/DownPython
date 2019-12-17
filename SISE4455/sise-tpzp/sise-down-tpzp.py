#!/usr/bin/env python3
import datetime
import os

import requests.packages.urllib3.util.ssl_

import SISE4455

# 当前文件路径
curDir = os.path.abspath(os.curdir) + os.sep

down_path = 'D:/图片/四色AV/自拍偷拍'
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
params = {
    'cur_dir': curDir,
    'down_path': down_path
}
SISE4455.down_pic(params)
print("all over")
