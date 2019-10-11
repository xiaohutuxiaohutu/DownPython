import datetime
import os
import PPP91

curDir = os.path.abspath(os.curdir)  # 当前文件路径
down_path = 'D:/图片/PPP91/网友自拍/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))
userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
# down_path = userPath + '/Pictures/Camera Roll/PPP91/meitui/'
down_param = {
    'cur_dir': curDir,
    'down_path': down_path
}
PPP91.down_image(down_param)

