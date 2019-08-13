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

file=open("zipai_2018-09-01_0.txt")
ip_list=get_ip_list(proxyipurl)
#获取总行数
for num,value in enumerate(file,1):
    #print('第'+str(num)+'行：')
    line=value.strip('\n')
    print('第%i行:%s'%(num,line))
    #获取代理服务器
    proxyip=get_random_ip(ip_list)
    #print('proxyip:'+str(proxyip))
    try:
        html=requests.get(line,headers = header, proxies=proxyip,timeout=10)
        html.encoding='utf-8'
        itemSoup=BeautifulSoup(html.text,'lxml')
        
        title=itemSoup.title.string
        title=re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\*+|\:+|\【+|\】+','',title)
        
        ind=title.index('-')
        newTitle=title[0:ind]
        
        imgUrls=itemSoup.select("body div[class='main'] div[class='contentList'] div[class='content'] p img")
        
        print('name：%s；个数：%s'%(str(newTitle.strip()),str(len(imgUrls))))
        '''
    	if len(imgUrls)==1:
            
            print('name：%s；个数：%s'%(str(newTitle.strip()),str(len(imgUrls))))

            continue
        '''
        path='E:/图片/zipai/'+datetime.datetime.now().strftime('%Y-%m-%d')+'/'+str(newTitle.strip())+'/'
        for i in range(0,len(imgUrls)):
            #restart=0
            fileUrl=imgUrls[i].get('src')
            image_name=fileUrl.split("/")[-1]
            print('开始下载-第'+str(i+1)+'个:'+fileUrl)
            try:
                imageUrl=requests.get(fileUrl,headers=header,proxies=proxyip,timeout=15)
                if imageUrl.status_code==200:
                    if not(os.path.exists(path)):
                        os.makedirs(path)
                    os.chdir(path)
                    f=open(image_name,'wb')
                    f.write(imageUrl.content)
                    f.close()
            except requests.exceptions.RequestException:                
                #restart+=1
                print('--第%i：---%s连接错误----'%(i+1,fileUrl))
                #print('尝试第%i次连接'%restart)
        print("---------------------")
    except requests.exceptions.RequestException:
       print('第%i行:%s---连接超时'%(num,line)) 
file.close
print("all over")
