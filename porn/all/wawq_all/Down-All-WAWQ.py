#!/usr/bin/env python3
import datetime
import os

import porn

curDir = os.path.abspath(os.curdir)

userPath = os.path.expanduser('~')  # 获取用户目录、
# downFilePath = userPath + '/Pictures/Camera Roll/all/woaiwoqi/'
# downFilePath = 'D:/图片/91porn/ALL/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'
downFilePath = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
down_param = {
    'cur_dir': curDir,
    'down_file_path': downFilePath
}
porn.down_pic_inclue_child(down_param)
