#!/usr/bin/env python3

import os
import sys

# curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)
#
# sys.path.append(r"C:\workspace\GitHub\DownPython")

import porn

down_param = {
    'down_url': porn.down_url_zpdr_jh,
    'start_page': 1,
    'end_page': 3
}
porn.write_to_text_include_jh(down_param)
