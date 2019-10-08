import os
import sys
import common
import datetime

curDir = os.path.abspath(os.curdir)
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(rootDir)

# ISOTIMEFORMAT = '%Y-%m-%d %X'

userPath = os.path.expanduser('~')  # 获取用户目录、
downFilePath = userPath + '/Pictures/Camera Roll/all/woaiwoqi/'
# downFilePath = 'D:/图片/91porn/ALL/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'
down_param = {
    'cur_dir': curDir,
    'replace_url': 'https://f.wonderfulday29.live/',
    'down_file_path': downFilePath
}
common.down_all_pic(down_param)

# 删除旧的未下载文件
common.del_old_Undown_Text(curDir)
