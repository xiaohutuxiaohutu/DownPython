import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
import common

sys.path.append(r"C:\workspace\GitHub\DownPython\common")
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

path = 'C:/workspace/GitHub/DownPython/porn/all/我爱我/'
preUrl = 'https://f.wonderfulday30.live/'
temp = 0
for i in range(1, 7):
    print('第' + str(i) + '页')
    url = "https://91dizhi-at-gmail-com-0201.p17.rocks/forumdisplay.php?fid=21&orderby=dateline&filter=2592000&page=" + str(
        i)
    print(url)
    proxyip = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyip)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        # print('fileUrl:'+fileUrl)
        fileUrl = preUrl + fileUrl
        temp += 1
        # print(temp)
        # print("fileUrl:"+fileUrl)
        os.chdir(path)
        f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
        f.write(fileUrl + '\n')
        f.close()
print("打印完成")
