#!/usr/bin/env python3

import porn

# 获取用户目录、
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'Pictures/Camera Roll/all/woaiwoqi/'
downFilePath = 'D:/图片/91porn/ALL/我爱我妻'
down_param = {
    'down_file_path': downFilePath
}
porn.down_pic_include_child(down_param)
