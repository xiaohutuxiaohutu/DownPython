#!/usr/bin/env python3
import os

import zhihu

userPath = os.path.expanduser('~') + os.sep
downFilePath = userPath + 'Pictures/zhihu'
down_param = {
  # 'question_id': 318927654,
  'question_id': 278164241,

  'down_path': downFilePath
}
zhihu.down_zhihu_pic(down_param)
