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
from common import BeautySoupTool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
cur_dir = os.getcwd() + os.sep


def write_common(start_page, end_page):
    furl_tool = porn.FurlTool(down_url)
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
        porn.write_exclude_jh(down_url, start_page, end_page, read_lines, cur_month_done_file)
    else:
        logger.info('保存 jh 链接')
        porn.write_jh_thread(down_url, start_page, end_page, read_lines, cur_month_done_file)


if __name__ == '__main__':
    date_tool = porn.DateTool()
    cur_month = date_tool.cur_month
    pre_month = date_tool.pre_month

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
