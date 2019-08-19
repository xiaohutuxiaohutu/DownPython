import os
import sys

import common

curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

preUrl = 'https://f.wonderfulday30.live/'
userPath = os.path.expanduser('~')  # 获取用户目录
# 文件下载保存路径
downFilePath = userPath + '/Pictures/Camera Roll/jh/自拍达人原创申请/'
with open(curDir + "/2019-08-19_09-21_0.txt", 'r') as fileObject:
    # readlines = fileObject.readlines() # 读取整个文档
    # print(len(readlines))
    for num, value in enumerate(fileObject, 1):
        print('第' + str(num) + '行：')
        line = value.strip('\n')
        # 获取当前连接下的 所有的图片的连接
        url_list = common.get_jh_img_url_list(line)
        imgUrls = url_list[0]
        newTitle = url_list[1]
        if len(imgUrls) == 0:
            os.chdir(curDir)
            common.save_not_down_url(line, newTitle, num)
        else:
            # path = downFilePath + datetime.datetime.now().strftime('%Y-%m-%d') + '/' + str(newTitle.strip()) + '/'
            path = downFilePath + str(newTitle.strip()) + '/'
            # 如果文件不存在，就创建
            common.create_file(path)
            os.chdir(path)
            for i in range(0, len(imgUrls)):
                file_url = imgUrls[i].get('file')
                fileUrl = file_url.replace('http://pic.w26.rocks/', preUrl)
                image_name = fileUrl.split("/")[-1]
                if not os.path.exists(image_name):
                    print('下载第' + str(i + 1) + '个:' + file_url)
                    common.down_img(fileUrl)
                else:
                    print('第' + str(i + 1) + '个已存在:' + file_url)
        print("-----down over----------------")
# file.close
print("all over")
