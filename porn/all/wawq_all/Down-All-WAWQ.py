#!/usr/bin/env python3
import datetime
import os

import porn

curDir = os.path.abspath(os.curdir) + os.sep

userPath = os.path.expanduser('~') + os.sep  # 获取用户目录、
# downFilePath = userPath + 'Pictures/Camera Roll/all/woaiwoqi/'
downFilePath = 'D:/图片/91porn/ALL/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m')) + '/'
# downFilePath = curDir + (datetime.datetime.now().strftime('%Y-%m')) + os.sep
down_param = {
    'cur_dir': curDir,
    'down_file_path': downFilePath
}
porn.down_pic_inclue_child(down_param)
