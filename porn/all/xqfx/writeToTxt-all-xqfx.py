#!/usr/bin/env python3
import os

import porn

# 获取当前文件路径
curDir = os.path.abspath(os.curdir) + os.sep
down_param = {
    'cur_dir': curDir,
    'done_down_text': curDir + 'down-done.text',
    'down_url': 'forumdisplay.php?fid=33&orderby=dateline&filter=2592000&page=%i',
    'start_page': 1,
    'end_page': 5
}
porn.write_to_text_exclude_jh(down_param)