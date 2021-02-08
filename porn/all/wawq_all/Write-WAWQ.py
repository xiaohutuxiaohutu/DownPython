# !/usr/bin/env python3
# coding=UTF-8
import os
import sys
from porn import FurlTool
import logging
import porn
import common
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
down_param = {
    'down_url': porn.down_url_wawq,
    'start_page': 1,
    'end_page': 5
}

if __name__ == '__main__':
    down_url = porn.down_url_wawq
    cur_month = common.get_datetime('%Y-%m')

    today = datetime.date.today()
    first = today.replace(day=1)

    last_month = first - datetime.timedelta(days=1)
    pre_month = last_month.strftime("%Y-%m")
    furl_tool = porn.FurlTool(down_url)
    file_name_list = furl_tool.get_down_map()
    if file_name_list is None and len(file_name_list) == 0:
        logger.info('找不到已下载文件，无法读取数据。。。。。。')

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
    porn.write_exclude_jh(porn.down_url_wawq, 1, 15)
