import datetime
import os
import PPP91

curDir = os.path.abspath(os.curdir)  # 当前文件路径
ISOTIMEFORMAT = '%Y-%m-%d %X'
# down_path = 'D:/图片/PPP91/网友自拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
down_path = 'D:/图片/PPP91/网友自拍/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))
down_param = {
    'cur_dir': curDir,
    'down_path': down_path
}
PPP91.down_image(down_param)

