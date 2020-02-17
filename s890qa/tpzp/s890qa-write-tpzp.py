import os
import s890qa

# curDir = os.path.abspath(os.curdir)  # 当前文件路径
params = {
    'down_url': 'https://www.790nd.com/piclist5/index_%i.html',
    'pre_url': 'https://www.890qa.com',
    'start_page': 12,
    'end_page': 1052

}
s890qa.write_txt(params)

print("打印完成")
