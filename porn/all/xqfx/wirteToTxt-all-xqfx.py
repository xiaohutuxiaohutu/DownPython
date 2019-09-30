import os
import sys

import common

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)

down_param = {
    'cur_dir': curDir,
    'pre_url': 'https://f.wonderfulday29.live/',
    'done_down_path': curDir + '/down-done.text',
    'down_url': 'https://f.wonderfulday29.live/forumdisplay.php?fid=33&orderby=dateline&filter=2592000&page=',
    'start_page': 1,
    'end_page': 5
}
common.write_to_text_exclude_jh(down_param)