#!/usr/bin/env python3
import os
# import threading
import common
from concurrent import futures
import porn
import time
# from furl import furl
# from pypinyin import pinyin, lazy_pinyin, Style
import pypinyin
from pypinyin import Style
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
user_dir = os.path.expanduser('~') + os.sep

down_path_c = user_dir + 'Pictures/Camera Roll/PORN/'
if not os.name == 'nt':
    down_file_path = '/usr/local/src/PORN/'

# 获取当前月份
cur_month = os.sep + common.get_datetime('%Y-%m') + os.sep
cur_dir = os.getcwd() + os.sep
rootDir = cur_dir[:cur_dir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径


def write_to_done_log(dir_path, line, new_title):
    done_file_list = common.get_cur_file_list2('log', 'done-' + common.get_datetime('%Y-%m') + '.log', dir_path)
    # print(dir_path)
    if len(done_file_list) == 0:
        done_log = dir_path + 'done-' + common.get_datetime('%Y-%m') + '.log'
    else:
        done_log = done_file_list[0]
        logger.info("保存已下载图片链接--->>>done.log:   " + done_log)
    # os.chdir(os.getcwd())
    with open(done_log, 'a+', encoding='utf-8') as f:
        f.write('%s:[%s,%s]\n' % (common.get_datetime('%Y/%m/%d %H:%M'), line, new_title))
    print()


def get_file_name_list(file_dir, file_type):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # print(file)
            # print(os.path.splitext(file))
            # if os.path.splitext(file)[1] == ('.' + file_type):
            if file == file_type:
                file_name_list.append(os.path.join(root, file))
    return file_name_list


def save_not_down_url(dir_path, line, new_title, num):
    name_list = get_file_name_list(dir_path, 'un_done-' + common.get_datetime('%Y-%m') + '.log')
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


def get_img_url_list(url, proxy_ip):
    try:

        soup = common.get_beauty_soup2(url, proxy_ip=proxy_ip)
        title = soup.title.string
    except:
        return [[], 'none']

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


# 获取指定目录下 指定类型的文件
def get_file_map(file_dir, file_type):
    file_map = {}
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ('.' + file_type):
                key = file.split('-')[0]
                value = file_map.get(key)
                if value is None or value == 'None':
                    file_map[key] = [os.path.join(root, file)]
                else:
                    value.append(os.path.join(root, file))
                    file_map[key] = value
    return file_map


def get_dir_path(category_name):
    pypinyin_slug = pypinyin.slug(category_name, separator='', style=Style.FIRST_LETTER)
    # print(pypinyin_slug)
    dir_path = rootDir + 'porn' + os.sep
    if pypinyin_slug.endswith('JH') and 'zpdrycsq' in pypinyin_slug:
        # dir_path = '../jh/zpdr_ycsq_jh/'
        dir_path = dir_path + 'jh/zpdr_ycsq_jh/'
    elif (not pypinyin_slug.endswith('JH')) and 'zpdrycsq' in pypinyin_slug:
        # dir_path = '../all/zpdr_ycsq_all/'
        dir_path = dir_path + 'all/zpdr_ycsq_all/'
    elif pypinyin_slug.endswith('JH') and 'wawq' in pypinyin_slug:
        # dir_path = '../jh/wawq_jh/'
        dir_path = dir_path + 'jh/wawq_jh/'
    elif 'wawq' in pypinyin_slug:
        # dir_path = '../all/wawq_all/'
        dir_path = dir_path + 'all/wawq_all/'
    elif 'xqxt' in pypinyin_slug:
        # dir_path = '../all/xqfx/'
        dir_path = dir_path + 'all/xqfx/'
    elif pypinyin_slug.endswith('JH') and 'yczp' in pypinyin_slug:
        # dir_path = '../jh/yczp_jh/'
        dir_path = dir_path + 'jh/yczp_jh/'
    elif (not pypinyin_slug.endswith('JH')) and 'yczp' in pypinyin_slug:
        # dir_path = '../all/yczp_all/'
        dir_path = dir_path + 'all/yczp_all/'
    return dir_path


# 创建下载目录
def create_down_root_path(category_name, title):
    root_path = down_path_c + category_name + os.sep + cur_month + os.sep + str(title.strip()) + os.sep
    if not (os.path.exists(root_path)):
        os.makedirs(root_path)
    return root_path


# executor = futures.ThreadPoolExecutor(max_workers=10, thread_name_prefix='down-pic-'


def down_all_pic(category_name, file_list):
    # 获取路径
    dir_path = get_dir_path(category_name)
    for index, file_name in enumerate(file_list, 1):
        logger.info('读取第 %i 个文件： %s' % (index, file_name))
        # 打开文件
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
                url_list = get_img_url_list(line, common.get_random_ip(ip_list))
                img_urls = url_list[0]
                logger.info('第 %i 行： -%s- ; 图片数量： %i ' % (num, line, len(img_urls)))
                new_title = url_list[1]
                logger.info(new_title)
                if len(img_urls) < 2:
                    # os.chdir(cur_dir)
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
                            file_url = porn.pre_url + file_url
                        image_name = file_url.split("/")[-1]
                        if not os.path.exists(image_name):
                            temp_map = {'file_url': file_url, 'path': path}
                            need_down.append(temp_map)
                        else:
                            logger.info('第 %i 行： -%s- ;url:%s;文件 %s已存在 ' % (num, line, file_url, image_name))
                    if len(need_down) > 0:
                        with futures.ThreadPoolExecutor(max_workers=5 if len(need_down) > 5 else len(need_down), thread_name_prefix="down-thread") as executor:
                            for index1, value1 in enumerate(need_down, 1):
                                submit = executor.submit(common.future_dowm_img, value1['file_url'], common.get_random_ip(ip_list), num, len(need_down), index1, value1['path'])
                                # submit完成之后的回调函数
                                submit.add_done_callback(common.executor_callback)
                                fs.append(submit)
                        futures.wait(fs, timeout=15)
                logger.info('第 %i 行： %s 下载完毕；用时：%i ' % (num, line, time.time() - start))
                # 保存所有的下载链接
                os.chdir(cur_dir)
                write_to_done_log(dir_path, line, new_title)
                time.sleep(1)
        print()
        logger.info('第 %i 个文件： %s 下载完毕，开始删除...' % (index, file_name))
        print()
        os.remove(file_name)
        if index == len(file_list):
            logger.info("------------删除成功，所有文件下载完毕------------------")
        else:
            logger.info('第 %i 个文件： %s 删除成功，开始读取下一个文件' % (index, file_name))


if __name__ == '__main__':
    file_map = get_file_map(cur_dir, 'txt')
    ip_list = common.get_ip_list(common.ipUrl)
    # 循环分组后的文件列表
    for key, item in file_map.items():
        print(key)
        down_all_pic(key, item)
'''
#future.result()会阻塞线程，相当于单线程了
for future in futures.as_completed(fs):
   try:
       print(future.running())
       # print(fs[future])
       data = future.result()
       # logger.info(file_url)
       # logger.info(data)
   except Exception as exc:
       print('%r generated an exception: %s' % (file_url, exc))
   else:
       logger.info(data)
'''
