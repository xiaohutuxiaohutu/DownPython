import requests
from bs4 import BeautifulSoup
import os
import sys
import imghdr
import time
import datetime
import random
from urllib.request import Request
from urllib.request import urlopen
if(os.name=='nt'):
    print(u'windows 系统')
else:
    print(u'linux')
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
path='C:/Users/love/OneDrive/photo/'
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
proxyipurl='http://www.xicidaili.com/'
ip_list=get_ip_list(proxyipurl)
#用get方法打开url并发送headers
temp=0
for i in range(397,400):
    print('第'+str(i)+'页')
    url=''
    if(i==1):
        url='http://www.m1f3.com/AAtupian/AAAtb/zipai/'
    else:
        url="http://www.m1f3.com/AAtupian/AAAtb/zipai/index-"+str(i)+".html"
    print(url)
    proxyip=get_random_ip(ip_list)
    html = requests.get(url,headers = header, proxies=proxyip)

    html.encoding='utf-8'

    soup=BeautifulSoup(html.text,'lxml')
    itemUrl=soup.select("body div[class='main'] li a")
    
    for j in range(0,len(itemUrl)):
        fileUrl=itemUrl[j].get('href')
        
        fileU='http://www.m1f3.com'+fileUrl
        temp+=1
        #print(temp)
        print("fileUrl:"+fileUrl)
        os.chdir(path)
        f=open('zipai_'+datetime.datetime.now().strftime('%Y-%m-%d')+'_'+str(temp//500)+'.txt','a+')
        f.write(fileU+'\n')
        f.close()
print("打印完成")
    
