import datetime
import io
import logging
import os
import re
# from urlparse import urlsplit
from urllib.request import Request
from urllib.request import urlopen

import requests

import common

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# header = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

    'cookie': '__utmz=195573755.1598620045.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __cfduid=d24b36dcbef40c33632ea75ba4ce7a3e71598620060; CzG_fid19=1598788937; __utmc=195573755; cf_clearance=0ef2867122cd2e6d2be89b3f7747e5bc53b86281-1598791835-0-1z79fa549dz49af16edz49fae42c-150; CzG_sid=e9C94M; CzG_oldtopics=D387559D387527D; CzG_fid33=1598781265; CzG_visitedfid=33D19; __utma=195573755.98189959.1598620045.1598789118.1598791835.4; __utmt=1; __utmb=195573755.1.10.1598791835'

}
default_time_format = '%Y-%m-%d %X'


# 获取用户目录
def get_user_dir():
    return os.path.expanduser('~') + os.sep


# 替换特殊字符
def replace_special_char(old_str):
    if old_str is not None:
        new_str = re.sub(r'<+|>+|/+|‘+|’+|\?+|\|+|"+|：+|:+|【+|】+|\.+|~+|\*+|\.\.\.+|\�+|�+|\？+', '', old_str)
        return new_str.strip()
    else:
        return old_str.strip()


# 替换并截取名字-porn使用
def replace_sub(old_str):
    title = replace_special_char(old_str)
    logger.info('common-title:' + title)
    ind = title.index('-')
    return title[0:ind]


def get_cur_dir():
    # 当前文件路径
    # curDir = os.path.abspath(os.curdir) + os.sep
    curDir = os.getcwd() + os.sep
    return curDir


def get_datetime(template):
    return datetime.datetime.now().strftime(template)


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
    logger.info(size)
    return size


# 获取线程异常
def executor_callback(worker):
    # logger.info("called worker callback function")
    # logger.info(worker.result())
    # logger.info('')
    worker_exception = worker.exception()
    if worker_exception:
        logger.exception("Worker return exception: {}".format(worker_exception))
        # raise worker_exception


# 排序
def list_distinct(old_list):
    new_list = list(set(old_list))
    # 按照原来顺序去重
    new_list.sort(key=old_list.index)
    return new_list


def del_old_Undown_Text(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('未下载.text'):
                file_list.append(os.path.join(root, file))
        # if len(file_list) >= 2:

        # 删除所有未下载记录文件
        for f in file_list:
            print('删除***未下载.text:' + f)
            os.remove(f)

        # 删除当前日期之前的未下载记录文件
        '''
        file_name = get_datetime('%Y-%m-%d') + '_未下载.text'
            
            
        for f in file_list:
            split = f.split('\\')
            L = len(split) - 1
            if split[L] != file_name:
                print('删除***未下载.text:' + f)
                os.remove(f)
        '''


# 获取项目路径
def get_project_dir():
    cur_dir = os.getcwd() + os.sep
    # 获取myProject，也就是项目的根路径
    rootDir = cur_dir[:cur_dir.find("DownPython\\") + len("DownPython\\")]
    return rootDir
