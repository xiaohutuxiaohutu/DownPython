import datetime
import os
import PPP91
import threading

curDir = os.path.abspath(os.curdir)  # 当前文件路径
down_path = 'D:/图片/PPP91/美腿/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))
down_param = {
    'cur_dir': curDir,
    'down_path': down_path
}
PPP91.down_image(down_param)
# p1 = threading.Thread(target=PPP91.down_image, args=(down_param,))
# p2 = threading.Thread(target=PPP91.down_image, args=(down_param,))
# p1.start()
# p2.start()
