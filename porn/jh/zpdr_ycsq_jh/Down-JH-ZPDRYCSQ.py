#!/usr/bin/env python3
import os

import porn

# 获取用户目录
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'Pictures/Camera Roll/jh/自拍达人原创申请'
downFilePath = 'D:/图片/91porn/精华/91自拍达人原创申请'
down_param = {
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)
