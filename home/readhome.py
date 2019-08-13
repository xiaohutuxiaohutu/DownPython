from bs4 import BeautifulSoup
import os

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

f = open("C:/Users/xiaohutu/Downloads/home.html", 'r', encoding='utf8')
# coding=utf-8
htmlFile = f.read()
itemSoup = BeautifulSoup(htmlFile, 'lxml')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

itemName = itemSoup.select(
    "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a")

path = 'c:/liwenqin/'
print(len(itemName))
for i in range(0, len(itemName)):
    fileUrl = itemName[i].get('href')
    print(fileUrl)
    if (fileUrl != None and fileUrl.find('.html') >= 0):
        fileUrl = "https://www.4455sk.com/" + fileUrl

print("打印完成")
