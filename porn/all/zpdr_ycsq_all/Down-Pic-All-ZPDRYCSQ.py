#!/usr/bin/env python3
import os

import porn

getcwd = os.getcwd()
print(getcwd)
# curDir = os.path.abspath(os.curdir) + os.sep
# 获取用户目录、
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + '/Pictures/Camera Roll/all/zipaidaren'
downFilePath = 'D:/图片/91porn/ALL/91自拍达人原创申请'
down_param = {
    'down_file_path': downFilePath
}

porn.down_all_pic(down_param)
