#!/usr/bin/env python3
import os

import zhihu

userPath = os.path.expanduser('~') + os.sep
downFilePath = userPath + 'Pictures/zhihu'
down_param = {
    'question_id': 316954079,

    'down_path': downFilePath
}
zhihu.down_zhihu_pic(down_param)
