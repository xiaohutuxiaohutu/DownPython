import os
import sys
import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)

temp = 0
preUrl = 'https://f.wonderfulday29.live/'
doneDownPath = curDir + '/DoneDown-JH-WAWQ.text'
with open(doneDownPath) as fileObj:
    # readLines = fileObj.readlines()
    readLines = fileObj.read().splitlines()
for i in range(1, 3):
    print('第' + str(i) + '页')
    url = "https://f.wonderfulday30.live/forumdisplay.php?fid=21&orderby=dateline&filter=digest&page=" + str(i)
    print(url)
    soup = common.get_beauty_soup(url)
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        sort_href = itemUrl[j].get('href')
        file_url = preUrl + sort_href
        split = sort_href.split("&")
        item_name = split[0]
        name_split = item_name.split("=")
        split_ = name_split[1]
        print(split_)
        temp += 1
        os.chdir(curDir)
        if split_ not in readLines:
            print('下载第' + str(j + 1) + '个:' + file_url)
            common.save_url_down(doneDownPath, file_url, split_, temp)
        else:
            print('第' + str(j + 1) + '个已存在:' + file_url)
print("打印完成")
