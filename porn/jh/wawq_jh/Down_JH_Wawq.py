#!/usr/bin/env python3
import datetime
import os

import porn

# 获取用户目录
# 文件下载保存路径
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'Pictures/Camera Roll/jh/woaiwoqi/'
downFilePath = 'D:/图片/91porn/精华/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m')) + os.sep
# downFilePath = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
down_param = {
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)
