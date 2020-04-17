#!/usr/bin/env python3
# coding=UTF-8
import os

# curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")
import porn

# down_file_path = porn.DOWN_PATH_JH_ZPDR_D
# down_file_path= porn.DOWN_PATH_JH_ZPDR_F
down_file_path = porn.DOWN_PATH_JH_ZPDR_OS
if os.name != 'nt':
    down_file_path = porn.DOWN_PATH_JH_ZPDR_Linux

# https://f.w24.rocks/viewthread.php?tid=371539&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest 20200417 未下载连接
# porn.down_all_pic(down_file_path)
# 下载指定连接的区间图片
porn.down_appoint_url("https://f.w24.rocks/viewthread.php?tid=371539&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest", down_file_path, 40, 61)
