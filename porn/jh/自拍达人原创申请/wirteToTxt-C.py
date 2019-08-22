import os
import sys
import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

temp = 0
preUrl = 'https://f.wonderfulday30.live/'
doneDownPath = curDir + '/doneDown.text'
common.create_file(doneDownPath)
with open(doneDownPath) as fileObj:
    readLines = fileObj.readlines()
for i in range(1, 4):
    print('第' + str(i) + '页')
    url = "https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=" + str(i)
    print(url)
    soup = common.get_beauty_soup(url)
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        sort_href = itemUrl[j].get('href')
        fileUrl = preUrl + sort_href
        split = sort_href.split("&")
        temp += 1
        os.chdir(curDir)
        if (split[0] + '\n') not in readLines:
            common.save_url_down(doneDownPath, fileUrl, split, temp)
print("打印完成")
