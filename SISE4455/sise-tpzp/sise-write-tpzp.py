import os
import SISE4455

curDir = os.path.abspath(os.curdir)  # 当前文件路径
params = {
    'cur_dir': curDir,
    'pre_url': 'https://www.6677zi.com',
    'down_url': 'https://www.6677zi.com/tupian/list-偷拍自拍-%i.html',
    'start_page': 1,
    'end_page': 65
}
SISE4455.write_to_txt(params)
print("打印完成")
