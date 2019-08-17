import datetime
import os
import sys
import requests
import common
from bs4 import BeautifulSoup

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)  # 将项目目录添加到系统路径，才能引入common

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
url = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=2'
url1 = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&filter=2592000&orderby=dateline'
print(url)
proxyIp = common.get_ip()
html = requests.get(url, headers=header, proxies=proxyIp)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, 'lxml')
print(soup)
os.chdir(curDir)
f = open('all-' + datetime.datetime.now().strftime('%Y-%m-%d') + '_home.html', 'a+')
f.write(html.text)
f.close()
print("打印完成")
