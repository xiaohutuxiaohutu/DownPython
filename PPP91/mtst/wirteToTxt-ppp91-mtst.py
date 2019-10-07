import os

import PPP91

curDir = os.path.abspath(os.curdir)  # 当前文件路径
params = {
    'cur_dir': curDir,
    'down_url': 'http://www.h7j2.com/AAtupian/AAAtb/meitui/index-%i.html',
    'done_down_txt': curDir + '/ppp91_done_down_meitui.txt',
    'pre_url': 'http://www.h7j2.com',
    'start_page': 1,
    'end_page': 194

}
PPP91.write_txt(params)
print("打印完成")
