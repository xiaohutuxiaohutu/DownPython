import os

import requests
from bs4 import BeautifulSoup

import common

curDir = os.getcwd()
url = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=2'
url1 = 'https://f.wonderfulday30.live/forumdisplay.php?fid=19&filter=2592000&orderby=dateline'
print(url)
proxyIp = common.get_ip()

html = requests.get(url, headers=common.header, proxies=proxyIp)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, 'lxml')
print(soup)
os.chdir(curDir)
with open('all-%s_home.html' % common.get_datetime('%Y-%m-%d'), 'a+') as f:
    f.write(html.text)
print("打印完成")
