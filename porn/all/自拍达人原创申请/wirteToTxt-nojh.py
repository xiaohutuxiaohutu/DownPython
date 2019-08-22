import os
import re
import sys
import common

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

# 用get方法打开url并发送headers
temp = 0
preUrl = 'https://f.wonderfulday30.live/'
listTagName = ['img']
# 保存已下载的连接
doneDownPath = curDir + '/down-done.txt'
common.create_file(doneDownPath)
with open(doneDownPath) as fileObj:
    readLines = fileObj.readlines()
print(len(readLines))
for i in range(1, 4):
    print('第' + str(i) + '页')
    url = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=' + str(i)
    print(url)
    soup = common.get_beauty_soup(url)
    resultTags = soup.find_all(id=re.compile('normalthread'))
    for ii in range(0, len(resultTags)):
        tag = resultTags[ii]
        for child in tag.children:
            if len(child) > 1:
                contents1 = child.contents[5]
                contents2 = contents1.contents
                if len(contents2) >= 0:
                    flag = True
                    for item in range(0, len(contents2)):
                        tag_name = contents2[item]
                        if tag_name.name in listTagName:
                            tag_name_src = tag_name['src']
                            rfind = tag_name_src.find('digest_1.gif') >= 0
                            if rfind:
                                flag = False
                                break
                    contents3 = contents2[3].contents
                    if len(contents3) > 0 and flag:
                        contents4 = contents3[0]
                        pic_href = contents4['href']
                        file_down_url = preUrl + pic_href
                        split = pic_href.split("&")
                        # contents__string = contents4.string
                        os.chdir(curDir)
                        if (split[0] + '\n') not in readLines:
                            common.save_url_down(doneDownPath, file_down_url, split, temp)
print("打印完成")
