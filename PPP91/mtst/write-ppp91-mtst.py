#!/usr/bin/env python3

import PPP91

params = {
    'down_url': 'http://www.h7j2.com/AAtupian/AAAtb/meitui/index-%i.html',
    'pre_url': 'http://www.h7j2.com',
    'start_page': 1,
    'end_page': 194

}
PPP91.write_txt(params)
print("打印完成")
