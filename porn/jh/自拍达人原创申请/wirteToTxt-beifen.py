import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
import common

curDir = os.path.abspath(os.curdir)  # 当前文件路径
sys.path.append(r"C:\workspace\GitHub\DownPython")
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
path = 'C:/workspace/GitHub/DownPython/porn/jh/自拍达人原创申请/'
preUrl = 'http://f.w24.rocks/'

# 用get方法打开url并发送headers
temp = 0
doneDownPath = curDir + '/doneDown.text'
if not (os.path.exists(doneDownPath)):
    os.makedirs(doneDownPath)
with open(doneDownPath) as fileObj:
    readLines = fileObj.readlines()
for i in range(1, 3):
    print('第' + str(i) + '页')
    url = "http://f.w24.rocks/forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=" + str(i)
    print(url)
    proxyIp = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxyIp)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    itemUrl = soup.select(
        "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")
    for j in range(0, len(itemUrl)):
        sortHref = itemUrl[j].get('href')
        fileUrl = preUrl + sortHref
        temp += 1
        os.chdir(path)
        if (sortHref + '\n' not in readLines):
            # f = open('jh-' + datetime.datetime.now().strftime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+')
            with open('jh-' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '_' + str(temp // 500) + '.txt',
                      'a+') as f:
                f.write(fileUrl + '\n')
            with open(doneDownPath, 'a+') as f:
                f.write(sortHref + '\n')
print("打印完成")
