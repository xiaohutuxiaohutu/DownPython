import os

from bs4 import BeautifulSoup

if os.name == 'nt':
    print(u'windows 系统')
else:
    print(u'linux')
userPath = os.path.expanduser('~')
curDir = os.getcwd()
print(curDir)
f = open(curDir + "/page.html", 'r', encoding='utf8')
# coding=utf-8
htmlFile = f.read()
itemSoup = BeautifulSoup(htmlFile, 'lxml')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

itemName = itemSoup.select("body div[class='maomi-content'] main[id='main-container'] div[class='content'] p")
print(len(itemName))
print(itemName)
title = itemSoup.title.string
title = title.split('www')[-1]
print(title)
path = userPath + '/Pictures/Camera Roll/' + title + '/'

for i in range(0, len(itemName)):
    text = itemName[i].text

    print(text)
    '''
    imageUrl=requests.get(fileUrl,headers=header)
    if not(os.path.exists(path)):
        os.makedirs(path)
    os.chdir(path)
    f=open(image_name,'wb')
    f.write(imageUrl.content)
    f.close()
    '''
print("打印完成")
