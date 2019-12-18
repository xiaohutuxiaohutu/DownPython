import os
import re

from bs4 import BeautifulSoup

if os.name == 'nt':
    print(u'windows 系统')
else:
    print(u'linux')
curDir = os.getcwd()
print(curDir)

with open(curDir + "/home.html", 'r', encoding='utf8') as f:
    htmlFile = f.read()
    itemSoup = BeautifulSoup(htmlFile, 'lxml')
    resultAll = itemSoup.find_all(id=re.compile('normalthread'))
os.chdir(curDir)
listTagName = ['img']
for i in range(0, len(resultAll)):
    tag = resultAll[i]
    for child in tag.children:
        if len(child) > 1:
            contents1 = child.contents[5]
            contents2 = contents1.contents
            if len(contents2) >= 16:
                flag = False
                for item in range(0, len(contents2)):
                    item_ = contents2[item]
                    # print(item_.name)
                    if item_.name in listTagName:
                        # print(item_)
                        src_ = item_['src']
                        rfind = src_.find('digest_1.gif') >= 0
                        if rfind:
                            flag = True
                            print(rfind)
                contents3 = contents2[3].contents
                if len(contents3) > 0 and flag:
                    contents4 = contents3[0]
                    href_ = contents4['href']
                    contents__string = contents4.string
                    os.chdir(curDir)
                    f = open('jh-home-result.txt', 'a+', encoding='utf - 8')
                    f.write(str(href_) + ';' + str(contents__string) + '\n')
                    f.write('*******************************************************' + '\n')
                    f.close()
                # print('*****************************************************')
            '''
            if (len(child.contents[5]) != 18):
                print(len(child.contents[1]))
                contents1 = child.contents[1]

                if (len(contents1) == 3):
                    contents2 = contents1.contents[1]
                    print(contents2['href'])

    # f = open('jh-home-select.txt', 'a+', encoding='utf - 8')
    # f.write(str(i_) + '\n')
    # f.write('*******************************************************' + '\n')
    # f.close()

# print(itemUrl)
# print(len(itemUrl))
# for i in range(0, len(itemUrl)):
#     fileUrl = itemUrl[i].get('href')
# print(fileUrl)
# if (fileUrl != None and fileUrl.find('.html') >= 0):
#     fileUrl = "https://www.4455sk.com/" + fileUrl
# print(fileUrl)
'''
print("打印完成")
