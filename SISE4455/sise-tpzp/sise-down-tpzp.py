import datetime
import os
import SISE4455
import requests.packages.urllib3.util.ssl_

curDir = os.path.abspath(os.curdir)  # 当前文件路径

down_path = 'D:/图片/四色AV/自拍偷拍/%s/' % datetime.datetime.now().strftime('%Y-%m-%d')

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
params = {
    'cur_dir': curDir,
    'down_path': down_path
}
SISE4455.down_pic(params)
print("all over")
