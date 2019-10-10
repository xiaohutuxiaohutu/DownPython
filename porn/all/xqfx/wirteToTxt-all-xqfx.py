import os

import common

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径

down_param = {
    'cur_dir': curDir,
    'pre_url': 'https://f.wonderfulday29.live/',
    'done_down_text': curDir + '/down-done.text',
    'down_url': 'https://f.wonderfulday29.live/forumdisplay.php?fid=33&orderby=dateline&filter=2592000&page=%i',
    'start_page': 1,
    'end_page': 4
}
common.write_to_text_exclude_jh(down_param)
