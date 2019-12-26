#!/usr/bin/env python3

import os
import sys

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

import porn

down_param = {
    'done_down_text': 'DoneDown-JH-zipaidaren.text',
    'down_url': "forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=%i",
    'start_page': 1,
    'end_page': 3
}
porn.write_to_text_include_jh(down_param)
