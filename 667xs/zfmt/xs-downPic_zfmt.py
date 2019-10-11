import datetime
import os
import common
curDir = os.path.abspath(os.curdir)  # 当前文件路径

down_path = 'D:/图片/667xs/制服美腿/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'

common.xs_down_pic(down_path, curDir, '_制服美腿')
common.del_old_Undown_Text(curDir)
print("all over")
