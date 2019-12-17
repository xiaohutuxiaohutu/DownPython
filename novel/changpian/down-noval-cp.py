#!/usr/bin/env python3
import os
import novel

# 获取用户目录
# userPath = os.path.expanduser('~') + os.sep
# downFilePath = userPath + 'noval/changpian'
downFilePath = 'D:/noval/changpian'
down_param = {
    'down_file_path': downFilePath,
    'require_pre_url': True,
    'pre_url': 'http://www.ve2s.com',
    'select_str': "body div[class='main'] div[class='contentList'] div[class='content'] p"

}
novel.down_noval(down_param)
