#!/usr/bin/env python3
import os
import novel

# 获取用户目录
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'noval/xiaoyuan'
downFilePath = 'D:/noval/xiaoyuan'
down_param = {
    'down_file_path': downFilePath,
    'require_pre_url': False,
    'pre_url': 'http://www.ve2s.com',
    'select_str': "body div[class='maomi-content'] main[id='main-container'] div[class='content']"

}
novel.down_noval(down_param)
