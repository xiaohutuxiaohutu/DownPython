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
import requests.packages.urllib3.util.ssl_
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
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
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
    random_ip = 'http://' + random.choice(ip_list)
    proxy_ip = {'http:':random_ip}
    return proxy_ip

file=open("G:/down/TP/toupai_2019-01-27_1.txt")
#ip_list=get_ip_list(proxyipurl)
#获取总行数
for num,value in enumerate(file,1):
    print('第'+str(num)+'行：')
    line=value.strip('\n')
    print(line)
    #获取代理服务器
    #proxyip=get_random_ip(ip_list)
    #print('proxyip:'+str(proxyip))

    #html=requests.get(line,headers = header, proxies=proxyip)
    html=requests.get(line,headers = header)
    html.encoding='utf-8'
    itemSoup=BeautifulSoup(html.text,'lxml')
    title=itemSoup.title.string
    title=re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+','',title)
    newTitle=title.split('www')[-1]
    print(str(newTitle.strip()))
    
    imgUrls=itemSoup.select("body div[class='maomi-content'] main[id='main-container'] div[class='content'] img")
    print('图片数量：'+str(len(imgUrls)))
    #print(imgUrls)
    if len(imgUrls)==0:
        f=open('toupai'+datetime.datetime.now().strftime('%Y-%m-%d')+'_未下载.txt','a+')
        f.write('第'+str(num)+'行：'+line+','+newTitle+'\n')
        f.close()
    else:
        path='G:/down/TP/toupai'+datetime.datetime.now().strftime('%Y-%m-%d')+'/'+str(newTitle.strip())+'/'
        if not(os.path.exists(path)):
            os.makedirs(path)
        for i in range(0,len(imgUrls)):
            fileUrl=imgUrls[i].get('data-original')
            #print(fileUrl)
            image_name=fileUrl.split("/")[-1]
            print('下载第'+str(i+1)+'个:'+fileUrl)
            imageUrl=requests.get(fileUrl,headers=header,verify=True)
            #if not(os.path.exists(path)):
                #os.makedirs(path)
            os.chdir(path)
            f=open(image_name,'wb')
            f.write(imageUrl.content)
            f.close()
    print("-----down over----------------")
file.close
print("all over")
