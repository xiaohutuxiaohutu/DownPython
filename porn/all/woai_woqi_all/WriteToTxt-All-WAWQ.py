import os
import re
import sys
import common

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

temp = 0
preUrl = 'https://f.wonderfulday30.live/'
listTagName = ['img']
# 保存已下载的连接
doneDownPath = curDir + '/Down-Done-WAWQ.text'  # 文件不需要创建，当open是如果不存在会自动打开
with open(doneDownPath) as fileObj:
    readLines = fileObj.read().splitlines()
for i in range(1, 10):
    print('第' + str(i) + '页')
    url = 'https://f.wonderfulday30.live/forumdisplay.php?fid=21&orderby=dateline&filter=2592000&page=' + str(i)
    print(url)
    soup = common.get_beauty_soup(url)
    # 查找所有 id 包含normalthread 的tags
    resultTags = soup.find_all(id=re.compile('normalthread'))
    for tag in resultTags:
        for child in tag.children:
            if len(child) > 1:
                contents1 = child.contents[5]
                contents2 = contents1.contents
                if len(contents2) >= 0:
                    flag = True  # 默认不是精华
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
                        item_name = split[0]
                        # contents__string = contents4.string
                        os.chdir(curDir)
                        temp += 1
                        if item_name not in readLines:
                            print('下载第' + str(temp) + '个'+pic_href)
                            common.save_url_down(doneDownPath, file_down_url, item_name, temp)
                        else:
                            print('第' + str(temp) + '已存在')
print("打印完成")
