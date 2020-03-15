#!/usr/bin/env python3
# coding=UTF-8
import os

import porn

# curDir = os.path.abspath(os.curdir) + os.sep
#     return curDir  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")
# down_file_path = porn.DOWN_PATH_WAWQ_D
# down_file_path = porn.DOWN_PATH_WAWQ_F
down_file_path = porn.DOWN_PATH_WAWQ_OS
if os.name == 'nt':
    print(u'windows system')
else:
    print(u'linux')
    down_file_path = porn.DOWN_PATH_WAWQ_Linux
porn.down_pic_include_child(down_file_path)
