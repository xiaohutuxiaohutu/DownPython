import os
import SISE4455

curDir = os.path.abspath(os.curdir)  # 当前文件路径
params = {
    'cur_dir': curDir,
    'pre_url': 'https://www.6677xr.com',
    'down_url': 'https://www.6677xr.com/tupian/list-偷拍自拍-%i.html',
    'start_page': 1,
    'end_page': 5,
    'done_down_text': curDir+'/sise-down-text.text'
}
SISE4455.write_to_txt(params)
print("打印完成")
