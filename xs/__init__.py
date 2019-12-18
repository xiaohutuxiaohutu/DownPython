import os

import requests

import common

cur_dir = os.getcwd()


def get_img_urls(url, encoding, split_char):
    itemSoup = common.get_beauty_soup_encoding(url, encoding)
    # proxy_ip = common.get_ip()
    # html = requests.get(url, headers=common.header, proxies=proxy_ip)
    # html.encoding = encoding
    # itemSoup = BeautifulSoup(html.text, "lxml")
    title = itemSoup.title.string
    posi = title.index(split_char)
    title = title[0:posi]
    new_title = common.replace_special_char(title)
    imgUrls = itemSoup.select(
        "body div[id='wrap'] div[id='ks'] div[id='ks_xp'] div[class='main'] div[class='content'] div div[class='n_bd'] img")
    img_urls = common.list_distinct(imgUrls)
    return [img_urls, new_title]


# 667xs下载图片
def xs_down_pic(down_path, split_char):
    down_path = down_path + os.sep + common.get_datetime('%Y-%m') + os.sep
    name_list = common.get_file_name_list(os.getcwd(), 'text')
    for index, file_name in enumerate(name_list, 1):
        # print('下载第' + str(index) + '个文件：' + file_name)
        print('下载第%i 个文件：%s' % (index, file_name))
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                print('第 %i 行：%s' % (num, line))
                urls = get_img_urls(line, 'gb2312', split_char)
                img_urls = urls[0]
                new_title = urls[1]
                print('图片数量：%i' % len(img_urls))
                path = down_path + str(new_title) + os.sep
                if not (os.path.exists(path)):
                    os.makedirs(path)
                os.chdir(path)
                if len(img_urls) <= 1:
                    os.chdir(cur_dir)
                    with open(common.get_datetime('%Y-%m-%d') + '_未下载.txt', 'a+', encoding='utf-8') as f:
                        f.write('第 %i 行：%s ;%s \n' % (num, line, new_title))
                else:

                    for i in range(0, len(img_urls)):
                        try:
                            img_url = img_urls[i].get('src')
                            # if img_url.startswith('http://tu.2015img.com'):
                            os.chdir(path)
                            image_name = img_url.split("/")[-1]
                            if not os.path.exists(image_name):
                                print('下载第 %i 行；第% i / %s个: %s ' % (num, i + 1, s, img_url))
                                common.down_img(img_url)
                            else:
                                print('第 %i 行；第% i / %s个 已存在: %s ' % (num, i + 1, s, img_url))
                        except requests.exceptions.RequestException:
                            print('第 %i 行：第%i / %s 个---连接错误：-- %s----' % (num, i + 1, s, img_url))
        os.remove(file_name)
    print('down over -----start delete old----------')
    common.del_old_Undown_Text(cur_dir)
