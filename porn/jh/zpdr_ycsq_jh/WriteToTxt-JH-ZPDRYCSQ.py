import os
import sys

import common
import porn
curDir = os.path.abspath(os.curdir)  # 当前文件路径

down_param = {
    'cur_dir': curDir,
    'pre_url': 'https://f.w24.rocks/',
    'done_down_text': curDir + '/DoneDown-JH-zipaidaren.text',
    'down_url': "https://f.w24.rocks/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=%i",
    'start_page': 1,
    'end_page': 2
}
porn.write_to_text_include_jh(down_param)
