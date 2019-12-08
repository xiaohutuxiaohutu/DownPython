#!/usr/bin/env python3
import datetime
import os

import porn

curDir = os.path.abspath(os.curdir) + os.sep
# 获取用户目录
userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'Pictures/Camera Roll/all/xingqufenxiang/'
downFilePath = 'D:/图片/91porn/ALL/兴趣分享/' + (datetime.datetime.now().strftime('%Y-%m')) + '/'
# downFilePath = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
down_param = {
    'cur_dir': curDir,
    'down_file_path': downFilePath
}

porn.down_pic_inclue_child(down_param)
