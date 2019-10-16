import datetime
import os
import PPP91
import threading

curDir = os.path.abspath(os.curdir)  # 当前文件路径
down_path = 'D:/图片/PPP91/美腿/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))
userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
# down_path = userPath + '/Pictures/Camera Roll/PPP91/meitui/'
file_name = curDir + '/2019-10-07_4.txt'
with open(file_name) as file:
    for num, value in enumerate(file, 1):
        line = value.strip('\n')
        print('第%i行:%s' % (num, line))
        img_urls = PPP91.get_img_urls(line, num)
        path = down_path + img_urls[0] + '/'
        PPP91.down_pic(img_urls[1], path, num)
os.remove(file_name)
