# 爬取知乎回答下面照片的爬虫
# 难点：异步加载，同时翻页信息不在html中

import requests
import json
from bs4 import BeautifulSoup
import re
import os
import random
from time import sleep

jsError = 0  # 统计json报错次数,使用了一个全局变量
# 在网上找了多个user-agent，然后每次访问时利用随机库在其中随机选择一个
headerstr = '''Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1
Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1
Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11
Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'''


def headerChange():
    headerList = headerstr.split('\n')
    length = len(headerList)
    return headerList[random.randint(0, length - 1)]


def get_ip_list():
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    }
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


ipList = get_ip_list()


def getHTMLTxt(url):
    querystring = {"status": "P"}
    headers = {
        'accept': "application/json, text/plain, */*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'authorization': "2|1:0|10:1559479354|14:capsion_ticket|44:Y2ZhN2NlNjkwOGUzNGVmMWJkZjcxNmVhNjQzMTQzYWI=|f80f1cb78039404962a082a8980216ec060b2177d2b5ead9682884d7b9af7e65",
        'connection': "keep-alive",
        'cookie': "_zap=7b165478-5fa0-4406-a0f8-973c8633ee9a; _xsrf=YZaFzOyKRmispb82B1Mg2jmNp3M9YJ8Q; d_c0=\"APBpZEkhhg-PTr87NxhsFezfWaNHEqBlA-s=|1559479351\"; capsion_ticket=\"2|1:0|10:1559479354|14:capsion_ticket|44:Y2ZhN2NlNjkwOGUzNGVmMWJkZjcxNmVhNjQzMTQzYWI=|f80f1cb78039404962a082a8980216ec060b2177d2b5ead9682884d7b9af7e65\"; z_c0=\"2|1:0|10:1559479371|4:z_c0|92:Mi4xbnRCS0F3QUFBQUFBOEdsa1NTR0dEeVlBQUFCZ0FsVk5TeExoWFFCLUtKbENrRzMya3NqNkpwNnlwQ2ktdkVHY2lB|a2eb5b43e08c638936978b4ee8d14eacbec4593c50f32cc7cc4119bb85bc8c2c\"; tst=r; q_c1=89cf5548154f44f49d34be6503f45a46|1559479373000|1559479373000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251",
        'host': "www.zhihu.com",
        'referer': "https://www.zhihu.com/question/26037846",
        'user-agent': headerChange(),
        'cache-control': "no-cache",
        'postman-token': "7e2c0f78-046a-09cd-2c11-f648d713b009"
    }
    html = ""
    while html == "":  # 因为请求可能被知乎拒绝，采用循环+sleep的方式重复发送，但保持频率不太高
        try:
            proxies = get_random_ip(ipList)
            print("\r这次试用ip：{}".format(proxies))
            r = requests.request("GET", url, headers=headers, params=querystring, proxies=proxies, timeout=5)
            html = r.text
            return html
        except:
            print("Let me sleep for 3 seconds")
            sleep(3)
            print("Was a nice sleep, now let me continue...")
            continue


def getPicURL(url, urlList):  # 这个函数拿到该页下的所有图片的url
    global jsError
    count = 0
    flag = 1
    while flag == 1:
        try:
            print("2333")
            html = getHTMLTxt(url)
            js = json.loads(html)
            flag = 0
        except:
            jsError += 1
            print("\rjson第{}次报错".format(jsError))
            continue
    # 用type()可以确定在data下的content的内容是字符串类型的，也就是html可以用BeautifSoup进行解析
    for ans in js['data']:
        soup = BeautifulSoup(ans['content'], 'html.parser')
        for img in soup.find_all('img'):
            match = re.match(r'https://.*?\.jpg', img.get('src'))
            if match:
                urlList.append(match.group(0))
        count += 1
    return count


def findNextURL(urlPre):
    global jsError
    flag = 1
    while flag == 1:
        try:
            print("3222")
            html = getHTMLTxt(urlPre)
            js = json.loads(html)
            flag = 0
        except:
            jsError += 1
            print("json第{}次报错".format(jsError))
            continue
    return js['paging']['next'], js['paging']['is_end']


def picDownload(url):
    # 对图片进行存储
    root = "D:/PY/CrawZhihuPic/pics/"  # 这里注意一下转义符
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
    except:
        print("文件保存出现错误")


def main():
    urlPre = "https://www.zhihu.com/api/v4/questions/26037846/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=3&limit=20&sort_by=default"
    isEnd = False
    text = getHTMLTxt(urlPre)
    js = json.loads(text)
    print(js)
    countOfAnswers = js['paging']['totals']  # 记录总的回答数
    print("本问题下共有{}个回答".format(countOfAnswers))
    urlList = []
    count = 0  # 用于记录页数,打印进度
    countOfPics = 0  # 记录图片下载进度
    while (isEnd != True and count < countOfAnswers):
        count += getPicURL(urlPre, urlList)
        print('\r当前进度：已完成爬取{}个回答，共{}个回答'.format(count, countOfAnswers), end="")
        (urlNext, isEnd) = findNextURL(urlPre)
        urlPre = urlNext
    print("图片url列表已经生成，共{}张图片，正在下载图片。。。".format(len(urlList)))
    for urlPic in urlList:
        picDownload(urlPic)
        print("\r当前进度，已下载{}张图片，共{}张".format(countOfPics, len(urlList)), end="")
        countOfPics += 1
    print("下载完成！")


main()
