import os
import sys
import datetime
import common

curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)
# ISOTIMEFORMAT = '%Y-%m-%d %X'

preUrl = 'https://f.wonderfulday29.live/'
userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
# downFilePath = userPath + '/Pictures/Camera Roll/jh/自拍达人原创申请/'
downFilePath = 'D:/图片/91porn/精华/91自拍达人原创申请/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'

down_param = {
    'cur_dir': curDir,
    'replace_url': 'https://f.wonderfulday29.live/',
    'down_file_path': downFilePath
}
common.down_all_pic(down_param)

common.del_old_Undown_Text(curDir)
