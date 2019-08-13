# coding=utf-8

from urllib import request as rr
from bs4 import BeautifulSoup
import os
import re

url = "https://www.zhihu.com/question/58604214"  # 指定的URL

#下载图片并保存到本地
def download(_url, file_name):
    if (_url == None):  #地址若为None则pass
        pass
    result = rr.urlopen(_url)  #打开链接

    if (result.getcode() != 200):  #如果链接不正常则pass
        pass
    else:
        data = result.read()  #链接正常的话则进行下载
        with open(file_name, "wb") as f:
            f.write(data)
            f.close()

if __name__ == '__main__':
    res = rr.urlopen(url)   #打开目标地址
    content = res.read()    #获取网页内容

    print(content)
    cnt = 0 #计数器
    soup = BeautifulSoup(content)   #实例化一个BeautifulSoup对象
    link_list = []  #创建一个list来存放链接

    for link in soup.find_all('img'):   #获取img标签中的内容
        addr = link.get('data-original')    #属性data-original对应的值即为图片的地址
        link_list.append(addr)  #添加到list中

    link_set = set(link_list)   #去重
    for addr in link_set:
        print(addr)
        if (addr != None):
            name=len(addr)
            ind=addr.index('com/')+4
            newTitle=addr[ind:name]
            print(newTitle)
            pathName = 'C:\\Users\\23948\\Pictures\\zhihu\\' + newTitle  #设置文件路径
            cnt = cnt + 1
            print("Doenloading the " + str(cnt) + "th picture")
            download(addr, pathName)    #调用下载函数
