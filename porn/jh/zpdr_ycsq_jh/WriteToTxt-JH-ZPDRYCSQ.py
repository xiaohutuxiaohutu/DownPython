import os
import sys

import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

down_param = {
    'cur_dir': curDir,
    'pre_url': 'https://f.wonderfulday29.live/',
    'done_down_path': curDir + '/DoneDown-JH-zipaidaren.text',
    'down_url': "https://f.wonderfulday29.live/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=",
    'start_page': 1,
    'end_page': 2
}
common.write_to_text_include_jh(down_param)
