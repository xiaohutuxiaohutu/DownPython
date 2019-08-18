# from . import common
from bs4 import BeautifulSoup
import os
import random
from urllib.request import Request

from urllib.request import urlopen
import imghdr
import time
import io
import re

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'


# 替换特殊字符
def replaceSpecelChar(oldStr):
    newstr = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+', '', oldStr)
    return newstr


# 获取代理IP
def get_ip_list(ipUrl):
    request = Request(ipUrl, headers=header)
    response = urlopen(request)
    obj = BeautifulSoup(response, 'lxml')
    # ip_text = obj.findAll('tr', {'class': 'odd'})
    ip_text = obj.findAll('tr')
    ip_list = []
    if (len(ip_text) > 0):
        for i in range(len(ip_text)):
            ip_tag = ip_text[i].findAll('td')
            if (len(ip_tag) > 0):
                ip_port = ip_tag[0].get_text() + ':' + ip_tag[1].get_text()
                ip_list.append(ip_port)
    # 检测IP是否可用
    if (len(ip_list) > 0):
        for ip in ip_list:
            try:
                proxy_host = 'https://' + ip
                proxy_temp = {"https:": proxy_host}
                res = urllib.urlopen(url, proxies=proxy_temp).read()
            except Exception as e:
                ip_list.remove(ip)
                continue
    return ip_list


# 从IPlist中获取随机地址
def get_random_ip(ip_list):
    # ip_list = get_ip_list(bsObj)
    random_ip = 'http://' + random.choice(ip_list)
    proxy_ip = {'http:': random_ip}
    return proxy_ip


ipList = []


def get_ip():
    global ipList
    if (len(ipList) == 0):
        ipList = get_ip_list(ipUrl)
    randomip = get_random_ip(ipList)
    return randomip


# 获取header
def get_header():
    return header


def fileSize():
    i = Image.open(StringIO(imageUrl.content))
    print(i.size)
    return i.size


# 判断文件或文件夹是否存在
def fileExist(fileName):
    return os.path.exists(fileName)


# 判断文件是否存在
def isFile(fileName):
    return os.path.isfile(fileName)
