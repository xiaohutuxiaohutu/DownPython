import requests
from bs4 import BeautifulSoup
import os
import sys
import imghdr
import time
import io
import re
import datetime
import random
from urllib.request import Request
from urllib.request import urlopen
if(os.name=='nt'):
    print(u'windows 系统')
else:
    print(u'linux')

proxyipurl='http://www.xicidaili.com/'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT='%Y-%m-%d %X'

#获取代理IP
def get_ip_list(proxyipurl):
    request = Request(proxyipurl, headers=header)
    response = urlopen(request)
    obj = BeautifulSoup(response, 'lxml')
    ip_text = obj.findAll('tr', {'class': 'odd'})
    ip_list = []
    for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text()
        ip_list.append(ip_port)
    # print("共收集到了{}个代理IP".format(len(ip_list)))
    # print(ip_list)
    #检测IP是否可用   
    for ip in ip_list:
        try:
            proxy_host='https://'+ip   
            proxy_temp={"https:":proxy_host}    
            res=urllib.urlopen(url,proxies=proxy_temp).read()
        except Exception as e:         
            ip_list.remove(ip)
            continue
    return ip_list
#从IPlist中获取随机地址
def get_random_ip(ip_list):
    #ip_list = get_ip_list(bsObj)
    random_ip = 'http://' + random.choice(ip_list)
    proxy_ip = {'http:':random_ip}
    return proxy_ip
file=open("D:/TP/downPic-python/jh/91自拍达人原创申请/2019-07-07_0.txt")
ip_list=get_ip_list(proxyipurl)
preUrl='http://f.w24.rocks/'
#获取总行数
for num,value in enumerate(file,1):
    print('第'+str(num)+'行：')
    line=value.strip('\n')
    print(line)
    #获取代理服务器
    proxyip=get_random_ip(ip_list)
    #print('proxyip:'+str(proxyip))

    html=requests.get(line,headers = header, proxies=proxyip)
    html.encoding='utf-8'
    itemSoup=BeautifulSoup(html.text,'lxml')
    title=itemSoup.title.string
    title=re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+','',title)
    ind=title.index('-')
    newTitle=title[0:ind]
    print(str(newTitle.strip()))
    imgUrls=itemSoup.select("body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    imgUrls2 = itemSoup.select("body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    imgUrls1 = itemSoup.select("body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    imgUrls4 = itemSoup.select("body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    print('图片数量：'+str(len(imgUrls)) + '；图片数量1：'+str(len(imgUrls1)) + '；图片数量2：'+str(len(imgUrls2)) + '；图片数量4：'+str(len(imgUrls4)))
    if len(imgUrls)==0 and len(imgUrls1)==0 and len(imgUrls2)==0 and len(imgUrls4)==0:
        os.chdir('D:/TP/downPic-python/jh/91自拍达人原创申请/')
        f=open(datetime.datetime.now().strftime('%Y-%m-%d')+'_未下载.txt','a+')
        f.write('第'+str(num)+'行：'+line+','+newTitle+'\n')
        f.close()
    else:   
        path='D:/TP/'+datetime.datetime.now().strftime('%Y-%m-%d')+'/'+str(newTitle.strip())+'/'
        if not(os.path.exists(path)):
            os.makedirs(path)
            os.chdir(path)
        os.chdir(path)
        for i in range(0,len(imgUrls)):
            fileUrl=imgUrls[i].get('file')
            fileUrl=fileUrl.replace('http://pic.w26.rocks/',preUrl)
            image_name=fileUrl.split("/")[-1]
            #判断文件或文件夹是否存在
            if not os.path.exists(image_name):
                print('下载第'+str(i+1)+'个:'+fileUrl)
                imageUrl=requests.get(fileUrl,headers=header)
                f=open(image_name,'wb')
                f.write(imageUrl.content)
                f.close()
            else:
                print(image_name+"-1已存在")
            #判断文件是否存在
            '''
            if not os.path.isfile(image_name):
                f=open(image_name,'wb')
                f.write(imageUrl.content)
                f.close()
            '''
        for i in range(0,len(imgUrls1)):
            fileUrl1=imgUrls1[i].get('file')
            fileUrl1=fileUrl1.replace('http://pic.w26.rocks/',preUrl)
            #fileUrl1='http://pic.w26.rocks/attachments/1906212318f9e42462ac7298ea.jpg'
            image_name1=fileUrl1.split("/")[-1]
            #判断文件或文件夹是否存在
            if not os.path.exists(image_name1):
                print('下载第'+str(i+1)+'个:'+fileUrl1)
                imageUrl1=requests.get(fileUrl1,headers=header)
                f=open(image_name1,'wb')
                f.write(imageUrl1.content)
                f.close()
            else:
                print(image_name1+"-1已存在")
        for i in range(0,len(imgUrls2)):
            fileUrl2=imgUrls2[i].get('file')
            fileUrl=fileUrl2.replace('http://pic.w26.rocks/',preUrl)
            image_name2=fileUrl2.split("/")[-1]    
            #判断文件或文件夹是否存在
            if not os.path.exists(image_name2):
                print('下载第'+str(i+1)+'个:'+fileUrl2)
                imageUrl2=requests.get(fileUrl2,headers=header)
                f=open(image_name2,'wb')
                f.write(imageUrl2.content)
                f.close()
            else:
                print(image_name2+"-2已存在")
        for i in range(0,len(imgUrls4)):
            print('------------')
            fileUrl2=imgUrls4[i].get('file')
            fileUrl=fileUrl2.replace('http://pic.w26.rocks/',preUrl)
            image_name2=fileUrl2.split("/")[-1]
            #判断文件或文件夹是否存在
            if not os.path.exists(image_name2):
                print('下载第'+str(i+1)+'个:'+fileUrl2)
                imageUrl2=requests.get(fileUrl2,headers=header)
                f=open(image_name2,'wb')
                f.write(imageUrl2.content)
                f.close()
            else:
                print(image_name2+"-4已存在")
                #time.sleep(5)
    print("-----down over----------------")
file.close
print("all over")
