import os
import porn

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# pre_url = 'https://f.w24.rocks/'
down_param = {
    'cur_dir': curDir,
    # 'pre_url': pre_url,
    'done_down_text': curDir + '/down-done.text',
    'down_url': 'forumdisplay.php?fid=33&orderby=dateline&filter=2592000&page=%i',
    'start_page': 1,
    'end_page': 5
}
porn.write_to_text_exclude_jh(down_param)
