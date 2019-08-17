from bs4 import BeautifulSoup
import os
import re
import string

re.compile("stickthread")
if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')
curDir = os.path.abspath(os.curdir)
print(curDir)

f = open(curDir + "/home.html", 'r', encoding='utf8')
htmlFile = f.read()
itemSoup = BeautifulSoup(htmlFile, 'lxml')
resultAll = itemSoup.find_all(id=re.compile('normalthread'))
# print(len(resultAll))
os.chdir(curDir)
# f = open('jh-home-select.txt', 'a+')
listTagName = ['img']
preUrl = 'https://f.wonderfulday30.live/'
for i in range(0, len(resultAll)):
    tag = resultAll[i]
    for child in tag.children:
        if (len(child) > 1):
            contents1 = child.contents[5]
            contents2 = contents1.contents
            if (len(contents2) >= 16):
                flag = False
                for item in range(0, len(contents2)):
                    item_ = contents2[item]
                    if (item_.name in listTagName):
                        src_ = item_['src']
                        rfind = src_.find('digest_1.gif') >= 0
                        if (rfind):
                            flag = True
                            break
                contents3 = contents2[3].contents
                if (len(contents3) > 0 and flag):
                    contents4 = contents3[0]
                    href_ =preUrl+ contents4['href']
                    contents__string = contents4.string
                    os.chdir(curDir)
                    f = open('jh-home-result.txt', 'a+', encoding='utf - 8')
                    f.write(str(href_) + '\n')
                    f.close()
                # print('*****************************************************')
print("打印完成")
