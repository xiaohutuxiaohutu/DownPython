import os

import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径

down_param = {
    'cur_dir': curDir,
    'pre_url': 'https://f.wonderfulday29.live/',
    'done_down_text': curDir + '/DoneDown-JH-WAWQ.text',
    'down_url': 'https://f.wonderfulday29.live/forumdisplay.php?fid=21&orderby=dateline&filter=digest&page=',
    'start_page': 1,
    'end_page': 2
}
common.write_to_text_include_jh(down_param)
