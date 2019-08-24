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
userPath = os.path.expanduser('~')  # 获取用户目录

question_id = 267285465
url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
soup = common.get_beauty_soup(url)
downFilePath = userPath + '/Pictures/' + soup.title.string + '/'
common.create_file(downFilePath)

# 获取当前目录下所有的待下载txt
file_name_list = common.get_file_name_list(curDir, 'txt')
# print(name_list)
for num, file_name in enumerate(file_name_list, 1):
    print('下载第' + str(num) + '个文件：' + file_name)
    with open(file_name, 'r') as fileObject:
        for num, value in enumerate(fileObject, 1):
            # print('第' + str(num) + '行：')
            img_url = value.strip('\n')
            image_name = img_url.split("/")[-1]
            os.chdir(downFilePath)
            if not os.path.exists(image_name):
                print('下载第' + str(num + 1) + '个:' + img_url)
                common.down_img(img_url)
            else:
                print('第' + str(num + 1) + '个已存在:' + img_url)
        print(file_name + "-----down over----------------")
    print('删除文件：' + file_name)
    os.remove(file_name)
print("-----***************down all over********************----------------")

'''''
with open(curDir + "/2019-08-23_13-37_0.txt", 'r') as fileObject:
    for num, value in enumerate(fileObject, 1):
        print('第' + str(num) + '行：')
        img_url = value.strip('\n')
        image_name = img_url.split("/")[-1]
        os.chdir(downFilePath)
        if not os.path.exists(image_name):
            print('下载第' + str(num + 1) + '个:' + img_url)
            common.down_img(img_url)
        else:
            print('第' + str(num + 1) + '个已存在:' + img_url)
    print("-----down over----------------")
'''''
