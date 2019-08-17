import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
import common
import re

curDir = os.path.abspath(os.curdir)  # 获取当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

# 用get方法打开url并发送headers
temp = 0
preUrl = 'https://f.wonderfulday30.live/'
listTagName = ['img']
re.compile("stickthread")
for i in range(1, 2):
    print('第' + str(i) + '页')
    url = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=' + str(i)
    # url = "http://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=" + str(i)
    print(url)
    proxyIp = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyIp)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    resultTags = soup.find_all(id=re.compile('normalthread'))
    for i in range(0, len(resultTags)):
        tag = resultTags[i]
        for child in tag.children:
            if (len(child) > 1):
                contents1 = child.contents[5]
                contents2 = contents1.contents
                if (len(contents2) >= 0):
                    flag = True
                    for item in range(0, len(contents2)):
                        item_ = contents2[item]
                        if (item_.name in listTagName):
                            src_ = item_['src']
                            rfind = src_.find('digest_1.gif') >= 0
                            if (rfind):
                                flag = False
                                break
                    # print(flag)
                    contents3 = contents2[3].contents
                    if (len(contents3) > 0 and flag):
                        contents4 = contents3[0]
                        href_ = preUrl + contents4['href']
                        contents__string = contents4.string
                        os.chdir(curDir)
                        f = open(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '_' + str(temp // 500) + '.txt',
                                 'a+')
                        f.write(str(href_) + '\n')
                        print(contents__string.strip())

                        # f = open(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '_name.txt', 'a+', encoding="utf-8")
                        # f.write(contents__string.strip() + '\n')
                        # f.close()
print("打印完成")
