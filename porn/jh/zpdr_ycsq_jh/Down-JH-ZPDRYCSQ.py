#!/usr/bin/env python3
import os

import porn

# curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# # sys.path.append(r"C:\workspace\GitHub\DownPython")
# sys.path.append(rootDir)

# 获取用户目录
userPath = os.path.expanduser('~') + os.sep
downFilePath = userPath + 'Pictures/Camera Roll/jh/自拍达人原创申请'
# downFilePath = 'F:/图片/91porn/精华/91自拍达人原创申请'
down_param = {
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)
