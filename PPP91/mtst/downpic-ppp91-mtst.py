#!/usr/bin/env python3
import datetime
import os

import PPP91

# 当前文件路径
# curDir = os.path.abspath(os.curdir) + os.sep
# cur_dir = os.getcwd()
# 获取用户目录
down_path = 'D:/图片/PPP91/美腿'
# 文件下载保存路径
# userPath = os.path.expanduser('~')
# down_path = userPath + '/Pictures/Camera Roll/PPP91/meitui'
down_param = {
    'down_path': down_path
}
PPP91.down_image(down_param)
# p1 = threading.Thread(target=PPP91.down_image, args=(down_param,))
# p2 = threading.Thread(target=PPP91.down_image, args=(down_param,))
# p1.start()
# p2.start()
