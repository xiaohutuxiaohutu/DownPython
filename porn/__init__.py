import os
import re

import common

# from urlparse import urlsplit
# 获取当前文件路径
# cur_dir = os.path.abspath(os.curdir) + os.sep
cur_dir = os.getcwd() + os.sep

# 获取当前月份
cur_month = os.sep + common.get_datetime('%Y-%m') + os.sep

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

pre_url = 'https://f.w24.rocks/'


def save_not_down_url(line, new_title, num):
    with open(common.get_datetime('%Y-%m-%d') + '_未下载.text', 'a+', encoding='utf-8') as f:
        f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n')


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num):
    file_name = '%s_%i.txt' % (common.get_datetime('%Y-%m-%d_%H-%M'), num // 500)
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
    done_down_text = cur_dir + down_param['done_down_text']
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
                            else:
                                print('the %i   is exist : %s ' % (temp, file_down_url))
    print("print over")


# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_to_text_include_jh(down_param):
    down_url = pre_url + down_param['down_url']
    start_page = down_param['start_page']
    end_page = down_param['end_page']
    done_down_text = cur_dir + down_param['done_down_text']
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
    soup = common.get_beauty_soup(url)
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
    soup = common.get_beauty_soup(url)
    # print(soup)
    title = soup.title.string

    new_title = common.replace_sub(title)
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
    new_list = common.list_distinct(img_url_list)
    # print('去重后图片数量：' + str(len(new_list)))
    return [new_list, new_title]


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


def down_all_pic(down_param):
    path_ = down_param['down_file_path'] + cur_month
    if not (os.path.exists(path_)):
        os.makedirs(path_)
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(file_name_list, 1):
        print('down the %i file： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('the %i line： %s' % (num, line))
                # 获取子页面连接
                # 获取所有图片连接
                url_list = get_img_url_list(line)
                img_urls = url_list[0]
                l = len(img_urls)
                print('duplicate removal image num： %i ' % l)
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

                        # fileUrl = file_url.replace('http://pic.w26.rocks/', pre_url)
                        image_name = file_url.split("/")[-1]
                        if not os.path.exists(image_name):
                            print('the %i line：the %i  / %i ge : %s' % (num, i + 1, l, file_url))
                            common.down_img(pre_url + file_url)
                        else:
                            print('the %i line：the %i  / %i is exist: %s' % (num, i + 1, l, file_url))
                print("-----down over----------------")
        os.remove(file_name)
    print("down all over----------------start delete old undown text-------------------")
    common.del_old_Undown_Text(cur_dir)


def down_pic_include_child(down_param):
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    down_path = down_param['down_file_path']
    for index, file_name in enumerate(file_name_list, 1):
        print('down the %i file ： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('the %i line： %s' % (num, line))
                # 获取子页面连接
                # child_img_url = get_img_child_url(line, pre_url)
                url_list = get_img_url_list(line)
                img_urls = url_list[0]
                # img_urls.extend(child_img_url)
                total = len(img_urls)
                print('duplicate removal image num： %i ' % total)
                new_title = url_list[1]
                if len(img_urls) < 2:
                    os.chdir(cur_dir)
                    save_not_down_url(line, new_title, num)
                else:
                    path = down_path + cur_month + str(new_title.strip()) + '/'
                    common.create_file(path)
                    os.chdir(path)
                    for i in range(0, len(img_urls)):
                        file_url = img_urls[i].get('file')
                        # fileUrl = file_url.replace('http://pic.w26.rocks/', pre_url)
                        fileUrl = pre_url + file_url
                        image_name = fileUrl.split("/")[-1]
                        if not os.path.exists(image_name):
                            print('the %i line：the %i  / %i ge: %s' % (num, i + 1, total, file_url))
                            common.down_img(fileUrl)
                        else:
                            print('the %i line：the %i  / %i is exist: %s' % (num, i + 1, total, file_url))
                print("-----down over----------------")
        os.remove(file_name)
    print("all over----------------start delete old undown text-------------------")
    common.del_old_Undown_Text(cur_dir)


def get_cur_dir():
    # 当前文件路径
    curDir = os.path.abspath(os.curdir) + os.sep
    return curDir
