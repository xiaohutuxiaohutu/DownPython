#!/usr/bin/env python3
# coding=UTF-8
# encoding: utf-8
import os
import re
from furl import furl
import common
from common import BeautySoupTool
from configparser import ConfigParser
import logging
from common import FileTool
import time
from concurrent import futures
from common import DownTool
from common import FileTool
from common import ProxyIp

logger = logging.getLogger(__name__)
# 用户目录
user_dir = os.path.expanduser('~') + os.sep

DOWN_PATH = user_dir + 'Pictures/Camera Roll/PORN/'
# 我爱我妻
DOWN_PATH_WAWQ_OS = user_dir + 'Pictures/Camera Roll/PORN/我爱我妻/'
DOWN_PATH_WAWQ_F = 'F:/PORN/我爱我妻'
DOWN_PATH_WAWQ_D = 'D:/PORN/我爱我妻'
DOWN_PATH_WAWQ_Linux = '/usr/local/src/PORN/我爱我妻'
# JH
DOWN_PATH_JH_WAWQ_OS = user_dir + 'Pictures/Camera Roll/PORN/我爱我妻_JH/'
DOWN_PATH_JH_WAWQ_F = 'F:/PORN/我爱我妻_JH'
DOWN_PATH_JH_WAWQ_D = 'D:/PORN/我爱我妻_JH'
DOWN_PATH_JH_WAWQ_Linux = '/usr/local/src/PORN/我爱我妻_JH'
# 兴趣分享
DOWN_PATH_XQFX_OS = user_dir + 'Pictures/Camera Roll/PORN/兴趣分享/'
DOWN_PATH_XQFX_F = 'F:/PORN/兴趣分享'
DOWN_PATH_XQFX_D = 'D:/PORN/兴趣分享'
DOWN_PATH_XQFX_Linux = '/usr/local/src/PORN/兴趣分享'
# 自拍达人原创申请
DOWN_PATH_ZPDR_OS = user_dir + '/Pictures/Camera Roll/PORN/自拍达人原创申请'
DOWN_PATH_ZPDR_F = 'F:/PORN/自拍达人原创申请'
DOWN_PATH_ZPDR_D = 'D:/PORN/自拍达人原创申请'
DOWN_PATH_ZPDR_Linux = '/usr/local/src/PORN/自拍达人原创申请'
# 91自拍达人原创申请-精华
DOWN_PATH_JH_ZPDR_OS = user_dir + 'Pictures/Camera Roll/PORN/自拍达人原创申请_JH'
DOWN_PATH_JH_ZPDR_F = 'F:/PORN/精华/自拍达人原创申请_JH'
DOWN_PATH_JH_ZPDR_D = 'D:/PORN/自拍达人原创申请_JH'
DOWN_PATH_JH_ZPDR_Linux = '/usr/local/src/PORN/自拍达人原创申请_JH'
# 原创自拍
DOWN_PATH_YCZP_OS = user_dir + '/Pictures/Camera Roll/all/原创自拍区'
DOWN_PATH_YCZP_F = 'F:/图片/porn/ALL/原创自拍区'
DOWN_PATH_YCZP_D = 'D:/porn/ALL/原创自拍区'
DOWN_PATH_YCZP_Linux = '/usr/local/src/porn/ALL/原创自拍区'
# from urlparse import urlsplit
# 获取当前文件路径
# cur_dir = os.path.abspath(os.curdir) + os.sep
cur_dir = os.getcwd() + os.sep

# 获取当前月份
cur_month = os.sep + common.get_datetime('%Y-%m') + os.sep

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

pre_url = 'https://f.w24.rocks/'
# pre_url = 'http://f.wonderfulday25.live/'
# 自拍达人下载链接
# http://f.wonderfulday25.live/forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=2
down_url_zpdr = 'forumdisplay.php?fid=19&orderby=dateline&filter=2592000&page=%i'

down_url_zpdr_jh = 'forumdisplay.php?fid=19&orderby=dateline&filter=digest&page=%i'
# 兴趣分享下载链接
down_url_xqfx = 'forumdisplay.php?fid=33&orderby=dateline&filter=2592000&page=%i'
# 我爱我妻下载链接
down_url_wawq = 'forumdisplay.php?fid=21&orderby=dateline&filter=2592000&page=%i'
down_url_wawq_jh = 'forumdisplay.php?fid=21&orderby=dateline&filter=digest&page=%i'
# 原创自拍
down_url_yczp_jh = 'forumdisplay.php?fid=4&orderby=dateline&filter=digest&page=%i'

down_url_yczp = 'forumdisplay.php?fid=4&orderby=dateline&filter=2592000&page=%i'


def save_not_down_url(dir_path, line, new_title, num):
    name_list = FileTool.get_file_name_list(dir_path, 'un_done-' + common.get_datetime('%Y-%m') + '.log')
    # print(dir_path)
    if len(name_list) == 0:
        file_name = dir_path + 'un_done-' + common.get_datetime('%Y-%m') + '.log'
    else:
        file_name = name_list[0]
        logger.info('un_down_file:' + file_name)
    # os.chdir(dir_path)
    with open(file_name, 'a+', encoding='utf-8') as f:
        # f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n')
        f.write('%s:[%s,%s]\n' % (common.get_datetime('%Y/%m/%d %H:%M'), line, new_title))


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num):
    file_name = '%s_%i.txt' % (common.get_datetime('%Y-%m-%d_%H%M'), num // 500)
    with open(file_name, 'a+') as f:
        f.write(file_down_url + '\n')
    # 保存已下载的连接，防止重复下载
    with open(done_down_text, 'a+') as f:
        f.write(pic_href + '\n')


listTagName = ['img']


# 非精华连接
def write_to_text_exclude_jh(down_param):
    down_url = pre_url + down_param['down_url']
    start_page = down_param['start_page']
    end_page = down_param['end_page']
    # done_down_text = cur_dir + down_param['done_down_text']
    file_name_list = common.get_file_name_list(cur_dir, 'text')
    done_down_text = file_name_list[0]
    # print(done_down_text)
    temp = 0
    with open(done_down_text) as fileObj:
        readLines = fileObj.read().splitlines()
    for i in range(start_page, end_page):
        print('Page %i :' % i)
        url = down_url % i
        print(url)
        soup = common.get_beauty_soup(url)
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
                                print('down the %i ge: %s' % (temp, pic_href))
                                save_url_down(done_down_text, file_down_url, split_, temp)
                            # else:
                            #     print('the %i   is exist : %s ' % (temp, file_down_url))
    print("print over")


# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_to_text_include_jh(down_param):
    down_url = pre_url + down_param['down_url']
    start_page = down_param['start_page']
    end_page = down_param['end_page']
    # done_down_text = cur_dir + down_param['done_down_text']
    file_name_list = common.get_file_name_list(cur_dir, 'text')
    done_down_text = file_name_list[0]
    # print(done_down_text)
    temp = 0
    with open(done_down_text) as fileObj:
        # readLines = fileObj.readlines()
        readLines = fileObj.read().splitlines()
    for i in range(start_page, end_page):
        print('Page' + str(i) + ':')
        url = down_url % i
        print(url)
        soup = common.get_beauty_soup(url)
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
                print('down the %i : %s ' % ((j + 1), file_url))
                save_url_down(done_down_text, file_url, split_, temp)
            else:
                print('the ' + str(j + 1) + ' is exist:' + file_url)
    print("print over ")


# # 获取除了JH图片外链接集合
def get_exclude_jh_image_url_list(line):
    soup = common.get_beauty_soup(line)
    new_title = common.replace_sub(soup.title.string)
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
    new_list = common.list_distinct(img_url_list)
    print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


# 获取JH图片链接集合
def get_jh_img_url_list(line):
    soup = common.get_beauty_soup(line)
    new_title = common.replace_sub(soup.title.string)
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
    new_list = common.list_distinct(img_url_list)
    print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


def get_img_child_url(url, pre_url):
    soup = BeautySoupTool.BeautySoupTool(url)
    # 获取当前页面的分页连接
    child_page_url = soup.select(
        "body div[id='wrap']  div[class='forumcontrol s_clear'] table tr td div[class='pages'] a[href]")
    new_list = []
    for item in child_page_url:
        get = pre_url + item.get('href')
        print('child_page:%s' % get)
        new_list.extend(get_img_url_list(get))
    print('child_page_img:%i' % len(new_list))
    return new_list


def get_img_url_list(url):
    try:
        soup = BeautySoupTool.BeautySoupTool(url)
        title = soup.get_title()
        logger.info('porn-title= ' + title)
    except:
        return [[], 'none']

    # new_title = common.replace_sub(title)
    img_url_list = soup.beautySoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
    img_url_list_2 = soup.beautySoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tr td img[file]")
    img_url_list_3 = soup.beautySoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div div[class='postattachlist'] dl dd p img[file]")
    img_url_list_1 = soup.beautySoup.select(
        "body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] div div table tbody tr td a[href]")
    img_url_list.extend(img_url_list_2)
    img_url_list.extend(img_url_list_3)
    img_url_list.extend(img_url_list_1)
    # print('----------- 去重 ------------------')
    new_list = common.list_distinct(img_url_list)
    # print('去重后图片数量：' + str(len(new_list)))
    return [new_list, title]


def get_child_img_url(url):
    soup = common.get_beauty_soup(url)
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
    new_list = common.list_distinct(img_url_list)
    return new_list


def write_to_done_log(line, new_title, dir_path=os.getcwd()):
    done_file_list = FileTool.get_cur_file_list('log', 'done-' + common.get_datetime('%Y-%m') + '.log', dir_path)
    # print(dir_path)
    if len(done_file_list) == 0:
        done_log = dir_path + 'done-' + common.get_datetime('%Y-%m') + '.log'
    else:
        done_log = done_file_list[0]
        logger.info("保存已下载图片链接--->>>done.log:   " + done_log)
    # os.chdir(os.getcwd())
    with open(done_log, 'a+', encoding='utf-8') as f:
        f.write('%s:[%s,%s]\n' % (common.get_datetime('%Y/%m/%d %H:%M'), line, new_title))
    # print()


def down_all_pic(down_param):
    path_ = down_param + cur_month
    if not (os.path.exists(path_)):
        os.makedirs(path_)
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(file_name_list, 1):
        # print('down the %i file： %s' % (index, file_name))
        print('读取第 %i 个文件： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                if line == '':
                    print('当前行为空：%i line' % num)
                    continue
                # print('the %i line： -%s- ' % (num, line), end=' ;')
                print('第 %i 行： -%s- ' % (num, line), end=' ;')
                # 获取所有图片连接
                url_list = get_img_url_list(line)
                img_urls = url_list[0]
                # print(' image num： %i ' % l)
                print(' 图片数量： %i ' % len(img_urls))
                new_title = url_list[1]

                if len(img_urls) < 2:
                    os.chdir(cur_dir)
                    save_not_down_url(line, new_title, num)
                else:
                    path = path_ + str(new_title.strip()) + os.sep
                    common.create_file(path)
                    os.chdir(path)
                    for i in range(0, len(img_urls)):
                        file_url = img_urls[i].get('file')
                        # if not ('http://' in file_url or 'https://' in file_url):
                        if not file_url.startswith('http'):
                            print('in:' + file_url)
                            file_url = pre_url + file_url
                        # fileUrl = file_url.replace('http://pic.w26.rocks/', pre_url)
                        image_name = file_url.split("/")[-1]
                        if not os.path.exists(image_name):
                            # print('the %i line：the %i  / %i ge : %s' % (num, i + 1, l, file_url), end=' ;')
                            print('第 %i 行：第 %i / %i 个 : %s' % (num, i + 1, len(img_urls), file_url), end=' ;')
                            common.down_img(file_url)
                # print("-----down over----------------")
                print('第 %i 行： %s 下载完毕 ' % (num, line))
                # 保存所有的下载链接
                os.chdir(cur_dir)
                write_to_done_log(line, new_title)
        print('第 %i 个文件： %s 下载完毕，开始删除...' % (index, file_name))
        os.remove(file_name)
        print('第 %i 个文件： %s 删除成功，开始读取下一个文件' % (index, file_name), end=";")
    # print("down all over----------------start delete old undown text-------------------")
    print("---------------- 所有文件下载完毕 -------------------")
    # common.del_old_Undown_Text(cur_dir)


def down_pic_include_child(down_path):
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    # down_path = down_param['down_file_path']
    for index, file_name in enumerate(file_name_list, 1):
        # print('down the %i file ： %s' % (index, file_name))
        print('读取第 %i 个文件 ： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                if line == '':
                    print('当前行为空：%i line' % num)
                    continue
                # print('the %i line： -%s-  ' % (num, line), end=';')
                print('第 %i 行： -%s-  ' % (num, line), end=';')
                # 获取子页面连接
                # child_img_url = get_img_child_url(line, pre_url)
                url_list = get_img_url_list(line)
                img_urls = url_list[0]
                # img_urls.extend(child_img_url)
                total = len(img_urls)
                # print('duplicate removal image num： %i ' % total)
                print('去重后图片数量： %i ' % total)
                new_title = url_list[1]
                # 保存所有的下载记录
                os.chdir(cur_dir)
                write_to_done_log(line, new_title)
                if len(img_urls) < 2:
                    os.chdir(cur_dir)
                    save_not_down_url(line, new_title, num)
                else:
                    path = down_path + cur_month + str(new_title.strip()) + '/'
                    common.create_file(path)
                    os.chdir(path)
                    for i in range(0, len(img_urls)):
                        file_url = img_urls[i].get('file')
                        # print(file_url)
                        # fileUrl = file_url.replace('http://pic.w26.rocks/', pre_url)
                        if not file_url.startswith('http'):
                            # if not ('http://' in file_url or 'https://' in file_url):
                            print('in:' + file_url)
                            file_url = pre_url + file_url
                        image_name = file_url.split("/")[-1]
                        # print(file_url)
                        if not os.path.exists(image_name):
                            # print('the %i line：the %i  / %i ge: %s' % (num, i + 1, total, file_url), end=';')
                            print('第 %i 行：第 %i  / %i 个: %s' % (num, i + 1, total, file_url), end=';')
                            common.down_img(file_url)
                        # else:
                        # print('the %i line：the %i  / %i is exist: %s' % (num, i + 1, total, file_url))
                        # print('第 %i 行：第 %i  / % i个已存在: %s' % (num, i + 1, total, file_url))
                # print("-----down over----------------")
                print('第 %i 行： %s 下载完毕，开始下载下一行文件  ' % (num, line))
        print('第 %i 个文件： %s 下载完毕，开始删除...' % (index, file_name))
        os.remove(file_name)
        print('第 %i 个文件： %s 删除成功，开始读取下一个文件' % (index, file_name))
    print("----------------所有文件下载完毕-------------------")
    # common.del_old_Undown_Text(cur_dir)


class FurlTool:
    def __init__(self, down_url, encoding='utf-8'):
        self.cf = furl(down_url)

    def get_furl(self):
        return self.cf

    def get_args(self, arg):
        return self.cf.args[arg]

    def get_fid(self):
        return self.cf.args['fid']  # 分类

    def get_filter(self):
        return self.cf.args['filter']  # 分类

    def is_digital(self, arg):
        return str(self.cf.args[arg]).isdigit()

    def get_down_file(self, arg='filter'):
        file_dir = self.get_file_dir(arg)
        return common.get_file_name_list(file_dir, 'text')

    def get_file_dir(self, arg='filter'):
        isdigit = self.is_digital(arg)
        fid_ = self.get_fid()
        file_dir = ''
        if fid_ == '19' and not isdigit:
            file_dir = '..\jh\zpdr_ycsq_jh'
        elif fid_ == '19' and isdigit:
            file_dir = '../all/zpdr_ycsq_all'
        elif fid_ == '21' and not isdigit:
            file_dir = '..\jh\wawq_jh'
        elif fid_ == '21' and isdigit:
            file_dir = '../all/wawq_all'
        elif fid_ == '33':
            file_dir = '../all/xqfx'
        elif fid_ == '4' and not isdigit:
            file_dir = '..\jh\yczp_jh'
        elif fid_ == '4' and isdigit:
            file_dir = '../all/yczp_all'
        return file_dir

    def get_down_map(self, arg='filter', file_type='text'):
        file_dir = self.get_file_dir(arg)
        return FileTool.get_file_map(file_dir, file_type)


# 获取当前月份
down_path_c = user_dir + 'Pictures/Camera Roll/PORN/'


# 创建下载目录
def create_down_root_path(category_name, title):
    # root_path = down_path_c + category_name + os.sep + common.get_datetime('%Y-%m') + os.sep + str(title.strip()) + os.sep
    root_path = '%s%s%s%s%s' % (user_dir, 'Pictures' + os.sep + 'Camera Roll' + os.sep + 'PORN', os.sep + category_name + os.sep, common.get_datetime('%Y-%m'), os.sep + str(title.strip()) + os.sep)
    if not (os.path.exists(root_path)):
        os.makedirs(root_path)
    return root_path


# 读取单个文本文件下载-futures
def dow_img_from_file(file_name, category_name):
    # 获取路径
    dir_path = FileTool.get_classify_dir_path(category_name)
    un_down = []
    with open(file_name) as file_obj:
        # logger.info('open file........')
        for num, value in enumerate(file_obj, 1):
            # logger.info('read file........')
            line = value.strip('\n')
            if line == '':
                logger.info('当前行为空：%i line' % num)
                continue
            logger.info(line)
            # 获取所有图片连接
            url_list = get_img_url_list(line)
            img_urls = url_list[0]
            logger.info('第 %i 行： -%s- ; 图片数量： %i ' % (num, line, len(img_urls)))
            new_title = url_list[1]
            logger.info(new_title)

            if len(img_urls) < 2:
                save_not_down_url(dir_path, line, new_title, num)
                continue
            else:
                path = create_down_root_path(category_name, str(new_title.strip()))  # path_ + str(new_title.strip()) + os.sep
                os.chdir(path)
                fs = []
                start = time.time()
                need_down = []
                for i in range(0, len(img_urls)):
                    file_url = img_urls[i].get('file')
                    if not file_url.startswith('http'):
                        logger.info('in:' + file_url)
                        file_url = pre_url + file_url
                    image_name = file_url.split("/")[-1]
                    if not os.path.exists(image_name):
                        temp_map = {'file_url': file_url, 'path': path}
                        need_down.append(temp_map)
                    else:
                        logger.info('第 %i 行： -%s- ;url:%s;文件 %s已存在 ' % (num, line, file_url, image_name))
                if len(need_down) > 0:
                    with futures.ThreadPoolExecutor(max_workers=5 if len(need_down) > 5 else len(need_down), thread_name_prefix="down-thread") as executor:
                        for index1, value1 in enumerate(need_down, 1):
                            submit = executor.submit(DownTool.future_dowm_img, value1['file_url'], ProxyIp.ProxyIp().get_random_proxy_ip(), num, len(need_down), index1, value1['path'])
                            # submit完成之后的回调函数
                            submit.add_done_callback(common.executor_callback)
                            fs.append(submit)
                    futures.wait(fs, timeout=15)
            logger.info('第 %i 行： %s 下载完毕；用时：%i ' % (num, line, time.time() - start))
            # 保存所有的下载链接
            os.chdir(cur_dir)
            write_to_done_log(line, new_title, dir_path)
            time.sleep(1)

# if __name__ == '__main__':
#     root_path = '%s%s%s%s%s' % (user_dir, 'Pictures' + os.sep + 'Camera Roll' + os.sep + 'PORN', os.sep + 'category_name' + os.sep, common.get_datetime('%Y-%m'), os.sep + 'str(title.strip())' + os.sep)
#     print(root_path)
