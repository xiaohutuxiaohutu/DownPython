import os
import sys
import common
import datetime
import porn
curDir = os.path.abspath(os.curdir)


userPath = os.path.expanduser('~')  # 获取用户目录、
# downFilePath = userPath + '/Pictures/Camera Roll/all/xingqufenxiang/'
downFilePath = 'D:/图片/91porn/ALL/兴趣分享/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'

down_param = {
    'cur_dir': curDir,
    'replace_url': 'https://f.wonderfulday29.live/',
    'down_file_path': downFilePath
}

porn.down_all_pic(down_param)

common.del_old_Undown_Text(curDir)
