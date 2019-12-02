#!/usr/bin/env python3
import datetime
import os

import xs

curDir = os.path.abspath(os.curdir) + os.sep  # 当前文件路径
# userPath = os.path.expanduser('~')  # 获取用户目录
# down_path = userPath + '/Pictures/Camera Roll/667xs/zfmt/'

# down_path = 'D:/图片/667xs/制服美腿/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'

down_path = curDir + (datetime.datetime.now().strftime('%Y-%m-%d')) + os.sep
xs.xs_down_pic(down_path, curDir, '_制服美腿')
