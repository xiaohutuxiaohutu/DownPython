import datetime
import os

import porn

curDir = os.path.abspath(os.curdir)
userPath = os.path.expanduser('~')  # 获取用户目录、
# downFilePath = userPath + '/Pictures/Camera Roll/all/zipaidaren/'
downFilePath = 'D:/图片/91porn/ALL/91自拍达人原创申请/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'
down_param = {
    'cur_dir': curDir,
    'down_file_path': downFilePath
}

porn.down_all_pic(down_param)
