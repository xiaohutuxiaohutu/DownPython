#!/usr/bin/env python3
import os
# import threading
import common
import porn
from furl import furl
import re
from concurrent import futures
import logging
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
cur_dir = os.getcwd() + os.sep
# gLock = threading.Lock()

executor = futures.ThreadPoolExecutor(max_workers=5)


# 保存下载连接到txt文档
def save_url_down(done_down_text, file_down_url, pic_href, num, title):
    file_name = '%s-%s_%i.txt' % (title, common.get_datetime('%Y-%m-%d_%H%M'), num // 500)
    with open(file_name, 'a+') as f:
        f.write(file_down_url + '\n')
    # 保存已下载的连接，防止重复下载
    with open(done_down_text, 'a+') as f:
        f.write(pic_href + '\n')


# current_dir 当前路径，done_down_path 保存已下载连接的text文档路径；pre_url url;down_url 下载页面连接
def write_jh_thread(start_page, end_page, read_lines, done_file_name):
    temp = 0
    fs = []
    for page_num in range(start_page, end_page):
        # 当前页数不重复的连接：》0读取下一页
        url = porn.pre_url + down_url % page_num
        logger.info('第 %i 页 ：%s' % (page_num, url))
        proxy_ip = common.get_random_ip(ip_list)
        soup = common.get_beauty_soup2(url, proxy_ip)
        title = common.replace_sub(soup.title.string).strip()
        if title.startswith('91'):
            title = title[2:]
        new_title = title + '_JH'
        logger.info(new_title)
        item_url = soup.select(
            "body div[id='wrap'] div[class='main'] div[class='content'] div[id='threadlist'] form table tbody[id] th span[id] a")
        logger.info('当前页获取到的连接数：%i' % len(item_url))
        # 当前页不重复的数字
        cur_page_num = 0
        for j in range(0, len(item_url)):
            sort_href = item_url[j].get('href')
            # print(sort_href)
            file_url = porn.pre_url + sort_href
            split = sort_href.split("&")
            item_name = split[0]
            name_split = item_name.split("=")
            split_ = name_split[1]
            temp += 1
            os.chdir(cur_dir)
            if split_ not in read_lines:
                logger.info('获取第 %i 个连接: %s ' % ((j + 1), file_url))
                cur_page_num += 1
                # save_url_down(done_file_name, file_url, split_, temp, new_title)
                f = executor.submit(save_url_down, done_file_name, file_url, split_, temp, new_title)
                f.add_done_callback(common.executor_callback)
                fs.append(f)
        if cur_page_num == 0:
            break
    logger.info("print over ")
    # 等待这些任务全部完成
    futures.wait(fs)


# 非精华连接
def write_exclude_jh(start_page, end_page, read_lines, done_file_name):
    temp = 0
    fs = []
    for page_num in range(start_page, end_page):
        url = porn.pre_url + down_url % page_num
        logger.info('第 %i 页 ：%s' % (page_num, url))
        soup = common.get_beauty_soup2(url, common.get_random_ip(ip_list))
        title = common.replace_sub(soup.title.string).strip()
        if title.startswith('91'):
            title = title[2:]
        # 查找所有 id 包含normalthread 的tags
        # 当前页不重复的数字
        cur_page_num = 0
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
                            if tag_name.name in porn.listTagName:
                                tag_name_src = tag_name['src']
                                rfind = tag_name_src.find('digest_1.gif') >= 0
                                if rfind:
                                    flag = False
                                    break
                        contents3 = contents2[3].contents
                        if len(contents3) > 0 and flag:
                            contents4 = contents3[0]
                            pic_href = contents4['href']
                            file_down_url = porn.pre_url + pic_href
                            split = pic_href.split("&")
                            item_name = split[0]
                            # contents__string = contents4.string
                            name_split = item_name.split("=")
                            split_ = name_split[1]
                            os.chdir(cur_dir)
                            temp += 1
                            if split_ not in read_lines:
                                print('down the %i ge: %s' % (temp, pic_href))
                                cur_page_num += 1
                                # save_url_down(done_file_name, file_down_url, split_, temp, title)
                                f = executor.submit(save_url_down, done_file_name, file_down_url, split_, temp, title)
                                fs.append(f)
        if cur_page_num == 0:
            break
    print("print over")
    # 等待这些任务全部完成
    futures.wait(fs)


def write_common(start_page, end_page):
    furl_tool = porn.FurlTool(down_url)
    # file_name_list = furl_tool.get_down_file()
    file_name_list = furl_tool.get_down_map()
    if file_name_list is None and len(file_name_list) == 0:
        logger.info('找不到已下载文件，无法读取数据。。。。。。')
        return
    isdigit = furl_tool.is_digital('filter')
    read_lines = []
    cur_month_done_file = ''
    pre_month_done_file = ''
    orgin_done_file_path = ''

    # 只读取上个月和这个月的连接
    file_name_list.items()
    for item, values in file_name_list.items():
        if not bool(re.search(r'\d', item)):
            orgin_done_file_path = values[0]
        if item.find(cur_month) > 0:
            cur_month_done_file = values[0]
            with open(cur_month_done_file) as fileObj:
                read_lines.extend(fileObj.read().splitlines())
        if item.find(pre_month) > 0:
            pre_month_done_file = values[0]
            with open(pre_month_done_file) as fileObj:
                read_lines.extend(fileObj.read().splitlines())
    # 判断当前月文件是否存在，如果不存在，用上个月文件生成
    if not cur_month_done_file.strip() and not pre_month_done_file.strip():
        logger.info('cur_month_done_file and pre_month_done_file 不能同时为空 ')
    # 如果上个月文件为空，则是首次下载，读取原始文件
    if not pre_month_done_file.strip():
        logger.info('pre_month_done_file  is null')
        with open(orgin_done_file_path) as fileObj:
            read_lines.extend(fileObj.read().splitlines())
    if not cur_month_done_file.strip():
        logger.info('cur_month_done_file  is null')
        cur_month_done_file = orgin_done_file_path.split('.text')[0] + '-' + cur_month + '.text'
        # with open(cur_month_done_file, 'a+') as fileObj:
        #     logger.info('create file')
        #     fileObj.close()
        # read_lines.append(fileObj.read().splitlines())
    if isdigit:
        logger.info('保存非jh 链接')
        write_exclude_jh(start_page, end_page, read_lines, cur_month_done_file)
    else:
        logger.info('保存 jh 链接')
        write_jh_thread(start_page, end_page, read_lines, cur_month_done_file)
    # gLock.release()


if __name__ == '__main__':
    cur_month = common.get_datetime('%Y-%m')

    today = datetime.date.today()
    first = today.replace(day=1)

    last_month = first - datetime.timedelta(days=1)
    pre_month = last_month.strftime("%Y-%m")

    ip_list = common.get_ip_list(common.ipUrl)
    # down_url = [porn.down_url_zpdr, porn.down_url_zpdr_jh, porn.down_url_wawq, porn.down_url_xqfx, porn.down_url_wawq_jh]
    down_urls = [porn.down_url_zpdr, porn.down_url_zpdr_jh, porn.down_url_wawq_jh, porn.down_url_yczp_jh, porn.down_url_yczp]
    # down_url = [porn.down_url_zpdr, porn.down_url_zpdr_jh, porn.down_url_wawq_jh]
    # down_url = [porn.down_url_yczp_jh, porn.down_url_yczp]
    # down_url = [porn.down_url_yczp_jh]
    # down_url = [porn.down_url_yczp]
    # threads = []
    # down_urls = [porn.down_url_zpdr_jh, porn.down_url_wawq_jh, porn.down_url_yczp_jh]
    for index in range(0, len(down_urls)):
        down_url = down_urls[index]
        write_common(1, 15)
