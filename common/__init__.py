import datetime
import io
import os
import random
import re
from urllib.request import Request
from urllib.request import urlopen
import urllib.request
import requests
from bs4 import BeautifulSoup

# from urlparse import urlsplit
from os.path import basename

import urllib.parse

if os.name == 'nt':
    print(u'windows 系统')
else:
    print(u'linux')

# ipUrl = 'http://www.xicidaili.com/'
ipUrl = 'https://www.kuaidaili.com/free/intr/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
ISOTIMEFORMAT = '%Y-%m-%d %X'


# 替换特殊字符
def replace_special_char(old_str):
    # newstr = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|\：+|\:+|\【+|\】+|\.+|\~+|\*+', '', old_str)
    new_str = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|：+|:+|【+|】+|\.+/~+|\*+|\.\.\.+|\�+|�+', '', old_str)
    return new_str


# 替换并截取名字-porn使用
def replace_sub(old_str):
    title = replace_special_char(old_str)
    ind = title.index('-')
    return title[0:ind]


# 代理地址集合-全局变量
ipList = []


# 获取代理IP
def get_ip_list(proxy_url):
    ip_list = []
    # print(proxy_url)
    request = Request(proxy_url, headers=header)
    response = urlopen(request)
    obj = BeautifulSoup(response, 'lxml')
    # ip_text = obj.findAll('tr', {'class': 'odd'})
    ip_text = obj.findAll('tr')

    if len(ip_text) > 0:
        for i in range(len(ip_text)):
            ip_tag = ip_text[i].findAll('td')
            if len(ip_tag) > 0:
                ip_port = ip_tag[0].get_text() + ':' + ip_tag[1].get_text()
                ip_list.append(ip_port)
    # 检测IP是否可用
    # print(ip_list)
    if len(ip_list) > 0:
        for ip in ip_list:
            try:
                proxy_host = 'https://' + ip
                proxy_temp = {"https:": proxy_host}
                # res = urllib.urlopen(proxy_host, proxies=proxy_temp).read()
                request = Request(proxy_temp, headers=header)
                response = urlopen(request).read()
            except Exception as e:
                ip_list.remove(ip)
                continue
    # print(ip_list)
    return ip_list


# get_ip_list(ipUrl)


# 从IPlist中获取随机地址
def get_random_ip(ip_list):
    # ip_list = get_ip_list(bsObj)
    random_ip = 'http://' + random.choice(ip_list)
    proxy_ip = {'http:': random_ip}
    return proxy_ip


# 从代理地址列表中获取一个随机IP
def get_ip():
    global ipList
    if len(ipList) == 0:
        print("请求代理地址列表：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        ipList = get_ip_list(ipUrl)
    random_ip = get_random_ip(ipList)
    return random_ip


test_image_url = [
    'http://pic.w26.rocks/attachments//1908131105d9a99e769a3ff3d4.jpg',
    'http://pic.w26.rocks/attachments//1908131059de4602941152bcd6.jpg'
]


def image_size(image_url):
    image = requests.get(image_url).content
    image_b = io.BytesIO(image).read()
    size = len(image_b) / 1000
    print(size)
    return size


def file_size(url):
    request = Request(url, headers=header)
    response = urlopen(request).read()
    size = len(response) / 1000
    print(size)
    return size


# 判断文件或文件夹是否存在
def file_exist(file_path):
    return os.path.exists(file_path)


# 判断文件夹是否存在，不存在则创建
def create_file(file_path):
    if not (os.path.exists(file_path)):
        os.makedirs(file_path)


# 保存未下载文件连接
def save_not_down_url(line, new_title, num):
    # os.chdir(cur_dir)
    with open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.text', 'a+', encoding='utf - 8') as f:
        f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n')


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num):
    file_name = '%s_%i.txt' % (datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'), num)
    # with open(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '_' + str(num // 500) + '.txt', 'a+') as f:
    with open(file_name, 'a+') as f:
        f.write(file_down_url + '\n')
    # 保存已下载的连接，防止重复下载
    # print(split)
    with open(done_down_text, 'a+') as f:
        f.write(pic_href + '\n')


# 保存图片
def down_img(file_url):
    image_name = file_url.split("/")[-1]
    if not os.path.exists(image_name):
        proxy_ip = get_ip()
        # print('随机代理地址：' + str(proxy_ip))
        get_request = requests.get(file_url, headers=header, proxies=proxy_ip)
        image = get_request.content
        image_b = io.BytesIO(image).read()
        print('图片大小：' + str(len(image_b) / 1000) + ' kb')
        with open(image_name, 'wb') as f:
            f.write(image)
    # else:
    #     print(image_name + "已存在")


def down_img_2(img_url, down_path, index):
    response = requests.get(img_url)  # , stream=True
    if response.status_code == 200:
        image = urllib.request.urlopen(img_url).read()
        # response = requests.get(image_url, stream=True) #
        # image = response.content
        try:
            # file_name = dir_name + os.sep + basename(urlsplit(image_url)[2])
            file_name = basename(urllib.parse.urlsplit(img_url)[2])

            with open(down_path + os.sep + '%d.jpg' % index, "wb") as picture:
                picture.write(image)
                print("下载 {} 完成!".format(picture))
        except IOError:
            print("IO Error\n")
            # continue
        finally:
            picture.close
    else:
        print()
        # continue


def mkdir(path):
    if not os.path.exists(path):
        print('新建文件夹:', path)
        os.makedirs(path)
        return True
    else:
        # print("图片存放于:", os.getcwd() + os.sep + path)
        print("图片存放于:", path)
        return False


# down_img('http://pic.w26.rocks/attachments//1908131059de4602941152bcd6.jpg')


# 判断文件是否存在
def is_file(file_name):
    return os.path.isfile(file_name)


def get_beauty_soup(url):
    proxy_ip = get_ip()
    html = requests.get(url, headers=header, proxies=proxy_ip)
    html.encoding = 'utf-8'
    return BeautifulSoup(html.text, 'lxml')


# 排序
def list_distinct(old_list):
    new_list = list(set(old_list))
    # 按照原来顺序去重
    new_list.sort(key=old_list.index)
    # print(len(new_list))
    return new_list


def get_title(url):
    soup = get_beauty_soup(url)
    new_title = replace_sub(soup.title.string)
    return new_title


# 获取JH图片链接集合
def get_jh_img_url_list(line):
    soup = get_beauty_soup(line)
    new_title = replace_sub(soup.title.string)
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
    # print('图片数量：' + str(len(img_url_list)))
    # print('----------- 去重 ------------------')
    new_list = list_distinct(img_url_list)
    print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


# # 获取除了JH图片外链接集合
def get_exclude_jh_image_url_list(line):
    soup = get_beauty_soup(line)
    new_title = replace_sub(soup.title.string)
    img_url_list = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    img_url_list_1 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    img_url_list_2 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    img_url_list_3 = soup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    img_url_list.extend(img_url_list_1)
    img_url_list.extend(img_url_list_2)
    img_url_list.extend(img_url_list_3)
    # print(str(new_title.strip()))
    new_list = list_distinct(img_url_list)
    print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


def get_img_child_url(url):
    soup = get_beauty_soup(url)
    # 获取当前页面的分页连接
    child_page_url = soup.select(
        "body div[id='wrap']  div[class='forumcontrol s_clear'] table tr td div[class='pages'] a[href]")
    return child_page_url


def get_img_url_list(url):
    soup = get_beauty_soup(url)
    # print(soup)
    title = soup.title.string

    new_title = replace_sub(title)
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
    # print('----------- 去重 ------------------')
    new_list = list_distinct(img_url_list)
    # print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


def get_file_name_list(file_dir, file_type):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ('.' + file_type):
                file_name_list.append(os.path.join(root, file))
    return file_name_list


def del_old_Undown_Text(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('未下载.text'):
                file_list.append(os.path.join(root, file))
        # if len(file_list) >= 2:
        file_name = datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.text'

        for f in file_list:
            split = f.split('\\')
            L = len(split) - 1
            if split[L] != file_name:
                print('删除***未下载.text:' + f)
                os.remove(f)


# 91-下载text文档中的连接图片
def down_all_pic(down_param):
    file_name_list = get_file_name_list(down_param['cur_dir'], 'txt')
    for index, file_name in enumerate(file_name_list, 1):
        print('下载第 %i 个文件： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('第 %i 行： %s' % (num, line))
                # 获取所有图片连接
                url_list = get_img_url_list(line)
                img_urls = url_list[0]
                # total = str(len(img_urls))
                l = len(img_urls)
                print('去重后图片数量： %i ' % l)
                new_title = url_list[1]
                if len(img_urls) == 0 or len(img_urls) == 1:
                    os.chdir(down_param['cur_dir'])
                    save_not_down_url(line, new_title, num)
                else:
                    path = down_param['down_file_path'] + str(new_title.strip()) + '/'
                    create_file(path)
                    os.chdir(path)
                    for i in range(0, len(img_urls)):
                        file_url = img_urls[i].get('file')
                        fileUrl = file_url.replace('http://pic.w26.rocks/', down_param['replace_url'])
                        image_name = fileUrl.split("/")[-1]
                        if not os.path.exists(image_name):
                            print('第 %i 行：第 %i  / %i 个: %s' % (num, i, l, file_url))
                            down_img(fileUrl)
                        else:
                            print('第 %i 行：第 %i  / %i 个 已存在: %s' % (num, i, l, file_url))
                print("-----down over----------------")
        os.remove(file_name)
    print("all over")


listTagName = ['img']


# 保存非精华连接   current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_to_text_exclude_jh(down_param):
    down_url = down_param['down_url']
    start_page = down_param['start_page']
    end_page = down_param['end_page']
    done_down_text = down_param['done_down_text']
    pre_url = down_param['pre_url']
    cur_dir = down_param['cur_dir']
    temp = 0
    with open(done_down_text) as fileObj:
        readLines = fileObj.read().splitlines()
    for i in range(start_page, end_page):
        print('第 %i 页' % i)
        url = down_url % i
        print(url)
        soup = get_beauty_soup(url)
        # 查找所有 id 包含normalthread 的tags
        result_tags = soup.find_all(id=re.compile('normalthread'))
        for tag in result_tags:
            for child in tag.children:
                if len(child) > 1:
                    contents1 = child.contents[5]
                    contents2 = contents1.contents
                    if len(contents2) >= 0:
                        flag = True  # 默认不是精华
                        for item in range(0, len(contents2)):
                            tag_name = contents2[item]
                            if tag_name.name in listTagName:
                                tag_name_src = tag_name['src']
                                rfind = tag_name_src.find('digest_1.gif') >= 0
                                if rfind:
                                    flag = False
                                    break
                        contents3 = contents2[3].contents
                        if len(contents3) > 0 and flag:
                            contents4 = contents3[0]
                            pic_href = contents4['href']
                            file_down_url = pre_url + pic_href
                            split = pic_href.split("&")
                            item_name = split[0]
                            # contents__string = contents4.string
                            name_split = item_name.split("=")
                            split_ = name_split[1]
                            os.chdir(cur_dir)
                            temp += 1
                            if split_ not in readLines:
                                print('下载第 %i 个: %s' % (temp, pic_href))
                                save_url_down(done_down_text, file_down_url, split_, temp)
                            else:
                                print('第' + str(temp) + '已存在')
    print("打印完成")


# 保存精华下载链接

# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_to_text_include_jh(down_param):
    down_url = down_param['down_url']
    start_page = down_param['start_page']
    end_page = down_param['end_page']
    done_down_text = down_param['done_down_text']
    pre_url = down_param['pre_url']
    cur_dir = down_param['cur_dir']
    temp = 0
    with open(done_down_text) as fileObj:
        # readLines = fileObj.readlines()
        readLines = fileObj.read().splitlines()
    for i in range(start_page, end_page):
        print('第' + str(i) + '页')
        url = down_url % i
        print(url)
        soup = get_beauty_soup(url)
        item_url = soup.select(
            "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")

        for j in range(0, len(item_url)):
            sort_href = item_url[j].get('href')
            # print(sort_href)
            file_url = pre_url + sort_href
            split = sort_href.split("&")
            item_name = split[0]
            name_split = item_name.split("=")
            split_ = name_split[1]
            # print(split_)
            temp += 1
            os.chdir(cur_dir)
            if split_ not in readLines:
                print('下载第' + str(j + 1) + '个:' + file_url)
                save_url_down(done_down_text, file_url, split_, temp)
            else:
                print('第' + str(j + 1) + '个已存在:' + file_url)
    print("打印完成")


# 667xs下载图片
def xs_down_pic(down_path, cur_dir, split_char):
    name_list = get_file_name_list(cur_dir, 'text')
    for index, file_name in enumerate(name_list, 1):
        # print('下载第' + str(index) + '个文件：' + file_name)
        print('下载第%i 个文件：%s' % (index, file_name))
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('第' + str(num) + '行：' + line)
                proxy_ip = get_ip()
                html = requests.get(line, headers=header, proxies=proxy_ip)
                html.encoding = 'gb2312'
                itemSoup = BeautifulSoup(html.text, "lxml")
                title = itemSoup.title.string
                posi = title.index(split_char)
                title = title[0:posi]
                new_title = replace_special_char(title).strip()
                imgUrls = itemSoup.select(
                    "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='content'] div div[class='n_bd'] img")
                img_urls = list_distinct(imgUrls)
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
                        img_url = img_urls[i].get('src')
                        if img_url.startswith('http://tu.2015img.com'):
                            print('下载第' + str(num) + '行；第' + str(i + 1) + ' / ' + s + ' 个: ' + img_url)
                            os.chdir(path)
                            down_img(img_url)
        os.remove(file_name)
