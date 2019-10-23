import os
import sys
import datetime
import common
import porn
curDir = os.path.abspath(os.curdir)
# rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# # sys.path.append(r"C:\workspace\GitHub\DownPython")
# sys.path.append(rootDir)

# ISOTIMEFORMAT = '%Y-%m-%d %X'

userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
# downFilePath = userPath + '/Pictures/Camera Roll/jh/woaiwoqi/'
downFilePath = 'D:/图片/91porn/精华/我爱我妻/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'
down_param = {
    'cur_dir': curDir,
    'replace_url': 'https://f.w24.rocks/',
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)

common.del_old_Undown_Text(curDir)
print("all over")
