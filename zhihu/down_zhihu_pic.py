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
question_id = 313825759
zhihu_url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
soup = common.get_beauty_soup(zhihu_url)
downFilePath = userPath + '/Pictures/'+soup.title.string+'/'
common.create_file(downFilePath)
with open(curDir + "/2019-08-22_17-45_2.txt", 'r') as fileObject:
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
