# from . import common
from bs4 import BeautifulSoup
import os
import random
from urllib.request import Request
import datetime
from urllib.request import urlopen
import imghdr
import time
import io
import re
import requests

if (os.name == 'nt'):
    print(u'windows 系统')
else:
    print(u'linux')

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'

# 代理地址集合-全局变量
ipList = []


# 替换特殊字符
def replaceSpecelChar(oldStr):
    newstr = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+', '', oldStr)
    return newstr


# 替换并截取名字-porn使用
def replaceAndSub(oldStr):
    title = replaceSpecelChar(oldStr)
    ind = title.index('-')
    return title[0:ind]


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


# 从代理地址列表中获取一个随机IP
def get_ip():
    global ipList
    if (len(ipList) == 0):
        print("请求代理地址列表：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        ipList = get_ip_list(ipUrl)
    randomip = get_random_ip(ipList)
    return randomip


def fileSize():
    i = Image.open(StringIO(imageUrl.content))
    print(i.size)
    return i.size


# 判断文件或文件夹是否存在
def fileExist(fileName):
    return os.path.exists(fileName)


# 判断文件是否存在，不存在则创建
def create_file(filePath):
    if not (os.path.exists(filePath)):
        os.makedirs(filePath)


# 保存未下载文件连接
def save_undownload_url(curDir, line, newTitle, num):
    os.chdir(curDir)
    with open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.text', 'a+', encoding='utf - 8') as f:
        f.write('第' + str(num) + '行：' + line + ',' + newTitle + '\n')


# 保存下载连接到txt文档
def save_url_down(done_down_path, file_url, short_href, num):
    with open(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '_' + str(num // 500) + '.txt', 'a+') as f:
        f.write(file_url + '\n')
    # 保存已下载的连接，防止重复下载
    with open(done_down_path, 'a+') as f:
        f.write(short_href + '\n')


# 保存图片
def down_img(file_url, image_name):
    if not os.path.exists(image_name):
        get_request = requests.get(file_url, headers=header)
        # f = open(image_name, 'wb')
        with open(image_name, 'wb') as f:
            f.write(get_request.content)
        # f.close()
    else:
        print(image_name + "已存在")


# 判断文件是否存在
def is_file(fileName):
    return os.path.isfile(fileName)


def get_beauty_soup(url):
    proxy_ip = get_ip()
    html = requests.get(url, headers=header, proxies=proxy_ip)
    html.encoding = 'utf-8'
    return BeautifulSoup(html.text, 'lxml')


def getJHImgUrlList(line):
    # 获取代理服务器
    # print(line)
    soup = get_beauty_soup(line)
    # proxy_ip = get_ip()
    # html = requests.get(line, headers=header, proxies=proxy_ip)
    # html.encoding = 'utf-8'
    # itemSoup = BeautifulSoup(html.text, 'lxml')
    new_title = replaceAndSub(soup.title.string)
    img_url_list = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    img_url_list_2 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    img_url_list_3 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    img_url_list_1 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    img_url_list.extend(img_url_list_2)
    img_url_list.extend(img_url_list_3)
    img_url_list.extend(img_url_list_1)
    print('图片数量：' + str(len(img_url_list)))
    print(new_title)
    return [img_url_list, new_title]


# 获取图片连接
def getAllexcludeJH(line):
    soup = get_beauty_soup(line)
    # # 获取代理服务器
    # proxy_ip = get_ip()
    # html = requests.get(line, headers=header, proxies=proxy_ip)
    # html.encoding = 'utf-8'
    # itemSoup = BeautifulSoup(html.text, 'lxml')
    newTitle = replaceAndSub(soup.title.string)

    imgUrls = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    imgUrls2 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    imgUrls1 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    imgUrls4 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    imgUrls.extend(imgUrls1)
    imgUrls.extend(imgUrls2)
    imgUrls.extend(imgUrls4)
    print(str(newTitle.strip()))
    print('图片数量：' + str(len(imgUrls)))
    return [imgUrls, newTitle]
