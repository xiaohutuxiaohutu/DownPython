import os

import requests

import common

cur_dir = os.getcwd()

DOWN_PATH_D_TP = 'D:/图片/四色AV/自拍偷拍'


def write_to_txt(params):
    pre_url = params['pre_url']
    down_url = params['down_url']
    start_page = params['start_page']
    end_page = params['end_page']
    # done_down_text = params['done_down_text']
    done_down_text = common.get_file_name_list(cur_dir, 'text')[0]
    temp = 0
    for i in range(start_page, end_page):
        print('第 %i 页' % i)
        url = down_url % i
        soup = common.get_beauty_soup(url)
        itemUrl = soup.select(
            "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a")
        with open(done_down_text) as fileObj:
            readLines = fileObj.read().splitlines()
        for j in range(0, len(itemUrl)):
            fileUrl = itemUrl[j].get('href')
            # print('fileUrl:'+fileUrl)
            if fileUrl is not None and fileUrl.find('.html') >= 0:
                if fileUrl not in readLines:
                    fileUrl = pre_url + fileUrl
                    temp += 1
                    print("fileUrl:" + fileUrl)
                    os.chdir(cur_dir)
                    file_name = '%s_%i.txt' % (common.get_datetime('%Y-%m-%d'), temp // 500)
                    with open(file_name, 'a+') as f:
                        f.write(fileUrl + '\n')
                else:
                    print('第' + str(j + 1) + '个已存在:' + fileUrl)
                    with open(done_down_text) as file_obj:
                        file_obj.write(fileUrl, 'a+')


def down_pic(params):
    down_path = params['down_path'] + common.get_datetime('%Y-%m-%d')
    name_list = common.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(name_list, 1):
        print('下载第 %i 个文件：%s ' % (index, file_name))

        with open(file_name) as file:
            for num, value in enumerate(file, 1):
                line = value.strip('\n')
                print('第 %i 行： %s' % (num, line))
                itemSoup = common.get_beauty_soup(line)
                title = itemSoup.title.string
                title = common.replace_special_char(title).strip()
                new_title = title.split('www')[-1]
                # print(new_title)

                imgUrls = itemSoup.select(
                    "body div[class='maomi-content'] main[id='main-container'] div[class='content'] img")

                img_urls = common.list_distinct(imgUrls)
                print('去重后图片数量： %i' % len(img_urls))
                s = len(img_urls)
                if s > 1:
                    path = down_path + str(new_title) + '/'
                    if not (os.path.exists(path)):
                        os.makedirs(path)
                    os.chdir(path)
                    for i in range(0, len(img_urls)):
                        img_url = img_urls[i].get('data-original')
                        image_name = img_url.split("/")[-1]
                        if not os.path.exists(image_name):
                            print('下载第 %i 行； 第 %i  / %i  个: %s' % (num, i + 1, s, img_url))
                            imageUrl = requests.get(img_url, headers=common.header, verify=True)
                            with open(image_name, 'wb') as f:
                                f.write(imageUrl.content)
                        else:
                            print('第 %i 行； 第 %i  / %i  个 已存在: %s' % (num, i + 1, s, img_url))
                print("-----down over----------------")

        os.remove(file_name)
    print("all over")
