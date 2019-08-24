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

file_name_list = common.get_file_name_list(curDir, 'txt')
for num, file_name in enumerate(file_name_list, 1):
    print('下载第' + str(num) + '个文件：' + file_name)
    # with open(curDir + "/2019-08-22_18-57_0.txt", 'r') as fileObject:
    with open(file_name, 'r') as fileObject:
        for num, value in enumerate(fileObject, 1):
            line = value.strip('\n')
            print('第' + str(num) + '行：' + line)
            # 获取当前连接下的 所有的图片的连接
            # url_list = common.get_jh_img_url_list(line)
            url_list = common.get_img_url_list(line)
            imgUrls = url_list[0]
            newTitle = url_list[1]
            if len(imgUrls) == 0:
                os.chdir(curDir)
                common.save_not_down_url(line, newTitle, num)
            else:
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
    os.remove(file_name)
# file.close
print("all over")
