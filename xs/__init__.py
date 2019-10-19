import datetime
import os
import common
import requests
from bs4 import BeautifulSoup

# from urlparse import urlsplit

if os.name == 'nt':
    print(u'windows 系统')
else:
    print(u'linux')

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}


def get_img_urls(url, encoding, split_char):
    proxy_ip = common.get_ip()
    html = requests.get(url, headers=header, proxies=proxy_ip)
    html.encoding = encoding
    itemSoup = BeautifulSoup(html.text, "lxml")
    title = itemSoup.title.string
    posi = title.index(split_char)
    title = title[0:posi]
    new_title = common.replace_special_char(title).strip()
    imgUrls = itemSoup.select(
        "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='content'] div div[class='n_bd'] img")
    img_urls = common.list_distinct(imgUrls)
    return [img_urls, new_title]


# 667xs下载图片
def xs_down_pic(down_path, cur_dir, split_char):
    name_list = common.get_file_name_list(cur_dir, 'text')
    for index, file_name in enumerate(name_list, 1):
        # print('下载第' + str(index) + '个文件：' + file_name)
        print('下载第%i 个文件：%s' % (index, file_name))
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('第' + str(num) + '行：' + line)
                urls = get_img_urls(line, 'gb2312', split_char)
                img_urls = urls[0]
                new_title = urls[1]
                s = str(len(img_urls))
                print('图片数量：' + s)
                path = down_path + str(new_title) + '/'
                if not (os.path.exists(path)):
                    os.makedirs(path)
                os.chdir(path)
                if len(img_urls) <= 1:
                    os.chdir(cur_dir)
                    f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.txt', 'a+', encoding='utf-8')
                    f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n', )
                    f.close()
                else:

                    for i in range(0, len(img_urls)):
                        try:
                            img_url = img_urls[i].get('src')
                            # if img_url.startswith('http://tu.2015img.com'):
                            os.chdir(path)
                            image_name = img_url.split("/")[-1]
                            if not os.path.exists(image_name):
                                print('下载第' + str(num) + '行；第' + str(i + 1) + ' / ' + s + ' 个: ' + img_url)
                                common.down_img(img_url)
                            else:
                                print('第' + str(num) + '行；第' + str(i + 1) + ' / ' + s + ' 个:已存在 ' + img_url)
                        except requests.exceptions.RequestException:
                            print('第 %i 行：第%i / %i 个---连接错误：-- %s----' % (num, i + 1, s, img_url))
    os.remove(file_name)
