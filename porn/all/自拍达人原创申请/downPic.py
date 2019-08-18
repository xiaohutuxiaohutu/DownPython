import os
import sys
import common

curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

preUrl = 'https://f.wonderfulday30.live/'
userPath = os.path.expanduser('~')  # 获取用户目录、
downFilePath = userPath + '/Pictures/Camera Roll/all/zipaidaren/'
# 打开文件
file_obj = open(curDir + "/2019-08-18_21-06_0.txt")
for num, value in enumerate(file_obj, 1):
    print('第' + str(num) + '行：')
    line = value.strip('\n')
    print(line)
    # 获取除了JH外的所有图片连接
    url_list = common.get_exclude_jh_image_url_list(line)
    imgUrls = url_list[0]
    newTitle = url_list[1]
    if len(imgUrls) == 0:
        # os.chdir(curDir)
        common.save_not_down_url(curDir, line, newTitle, num)
    else:
        path = downFilePath + str(newTitle.strip()) + '/'
        common.create_file(path)
        os.chdir(path)
        for i in range(0, len(imgUrls)):
            file_url = imgUrls[i].get('file')
            fileUrl = file_url.replace('http://pic.w26.rocks/', preUrl)
            # image_name = fileUrl.split("/")[-1]
            print('下载第' + str(i + 1) + '个:' + file_url)
            common.down_img(fileUrl)

    print("-----down over----------------")
# file_obj.close
print("all over")
