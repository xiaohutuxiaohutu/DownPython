import os
import common

userPath = os.path.expanduser('~')  # 获取用户目录
curDir = os.path.abspath(os.curdir)  # 当前文件路径

# down_path = 'D:/图片/667xs/美乳清纯/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
down_path = userPath + '/Pictures/Camera Roll/667xs/meiruqingchun/'
common.xs_down_pic(down_path, curDir, '_美乳清纯')
common.del_old_Undown_Text(curDir)
print("all over")
