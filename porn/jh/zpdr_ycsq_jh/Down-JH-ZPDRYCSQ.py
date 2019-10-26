import os
import datetime
import porn
curDir = os.path.abspath(os.curdir)


preUrl = 'https://f.wonderfulday29.live/'
userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
# downFilePath = userPath + '/Pictures/Camera Roll/jh/自拍达人原创申请/'
downFilePath = 'D:/图片/91porn/精华/91自拍达人原创申请/' + (datetime.datetime.now().strftime('%Y-%m-%d')) + '/'

down_param = {
    'cur_dir': curDir,
    'replace_url': 'https://f.w24.rocks/',
    'down_file_path': downFilePath
}
porn.down_all_pic(down_param)

