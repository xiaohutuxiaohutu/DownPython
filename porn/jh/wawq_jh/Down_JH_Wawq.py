#!/usr/bin/env python3
import datetime
import os

import porn

# 或缺当前文件目录
curDir = os.path.abspath(os.curdir)
# 获取用户目录
userPath = os.path.expanduser('~') + os.sep
# 文件下载保存路径
# downFilePath = userPath + 'Pictures/Camera Roll/jh/woaiwoqi/'
downFilePath = 'D:/图片/91porn/精华/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m')) + os.sep
# downFilePath = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
down_param = {
    'cur_dir': curDir,
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)
