import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

temp = 0
preUrl = 'https://f.wonderfulday30.live/'

for i in range(1, 3):
    print('第' + str(i) + '页')
    url = "https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=" + str(i)
    print(url)
    proxyIp = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyIp)

    html.encoding = 'utf-8'

    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        fileUrl = preUrl + fileUrl
        temp += 1
        os.chdir(curDir)
        f = open('jh-' + datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
        f.write(fileUrl + '\n')
        f.close()
print("打印完成")
