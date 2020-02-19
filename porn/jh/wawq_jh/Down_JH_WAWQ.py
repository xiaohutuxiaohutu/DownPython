#!/usr/bin/env python3
# coding=UTF-8

# curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")
import porn

down_file_path = porn.DOWN_PATH_JH_WAWQ_D
# down_file_path = porn.DOWN_PATH_JH_WAWQ_Linux
# down_file_path = porn.DOWN_PATH_JH_WAWQ_F
# down_file_path = porn.DOWN_PATH_JH_WAWQ_OS

porn.down_all_pic(down_file_path)
