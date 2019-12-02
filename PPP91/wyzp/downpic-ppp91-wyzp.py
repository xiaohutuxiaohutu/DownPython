#!/usr/bin/env python3
import datetime
import os

import PPP91

# 当前文件路径
curDir = os.path.abspath(os.curdir) + os.sep
# down_path = 'D:/图片/PPP91/网友自拍/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))

# 文件下载保存路径
# 获取用户目录
# userPath = os.path.expanduser('~')
# down_path = userPath + '/Pictures/Camera Roll/PPP91/wyzp/'
down_path = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
down_param = {
    'cur_dir': curDir,
    'down_path': down_path
}
PPP91.down_image(down_param)
