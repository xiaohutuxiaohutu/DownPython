#!/usr/bin/env python3

import os
import sys

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

import porn

down_param = {
    'done_down_text': 'Down-Done-WAWQ.text',
    'down_url': 'forumdisplay.php?fid=21&orderby=dateline&filter=2592000&page=%i',
    'start_page': 1,
    'end_page': 5
}
porn.write_to_text_exclude_jh(down_param)
