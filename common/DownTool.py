import io
import logging
import os
import threading
import time
import urllib.parse
import urllib.request
# from urlparse import urlsplit
from os.path import basename

import requests

import common
from common import ProxyIp

# 下载工具类
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def down_img(file_url):
    image_name = file_url.split("/")[-1]
    if not os.path.exists(image_name):
        proxy_ip = ProxyIp.ProxyIp().get_random_proxy_ip()
        # print(file_url)
        get_request = requests.get(file_url, headers=common.header, proxies=proxy_ip, timeout=10)
        image = get_request.content
        image_b = io.BytesIO(image).read()
        # print(' size : %i kb' % (len(image_b) / 1000))
        logger.info(' 图片大小 : %i kb' % (len(image_b) / 1000))
        if len(image_b) > 0:
            with open(image_name, 'wb') as f:
                f.write(image)
    # else:
    #     print(image_name + "已存在")


def future_dowm_img(img_url, proxy_ip, line_num, img_nums, img_num, down_path):
    os.chdir(down_path)
    image_name = img_url.split("/")[-1]
    if not os.path.exists(image_name):
        # logger.debug('start get request.get')
        try:
            get_request = requests.get(img_url, headers=common.header, proxies=proxy_ip, timeout=10)
        except Exception as e:
            logger.info("请求失败，请求时间是：{}".format(common.get_datetime('%Y/%m/%d %H:%M')))
            logger.info('失败原因：%s' % e)
            time.sleep(5)
            get_request = requests.get(img_url, headers=common.header, proxies=proxy_ip, timeout=10)
        # logger.debug('end request.get')
        image = get_request.content
        image_b = io.BytesIO(image).read()
        # logger.info('%s 图片大小 : %i kb' % (image_name, len(image_b) / 1000))
        logger.info('%s  start down 第 %i 行：第 %i / %i 个 : %s ；size：%s kb' % (threading.current_thread().name, line_num, img_num + 1, img_nums, img_url, len(image_b) / 1000))
        if len(image_b) > 0:
            os.chdir(down_path)
            with open(image_name, 'wb') as f:
                f.write(image)
            # logger.info('%s 图片下载完成' % image_name)
    # else:
    #     logger.info(image_name + "已存在")
    # return '%s done 第 %i 行：第 %i / %i 个 : %s 下载完成！' % (threading.current_thread().name, line_num, img_num + 1, img_nums, img_url)


# 下载知乎图片
def down_zhihu_img(file_url, proxy_ip):
    image_name = os.path.basename(file_url).split('?')[0]
    if not os.path.exists(image_name):
        get_request = requests.get(file_url, headers=common.header, proxies=proxy_ip)
        image = get_request.content
        image_b = io.BytesIO(image).read()
        logger.info(' 图片大小 : %i kb' % (len(image_b) / 1000))
        if len(image_b) > 0:
            with open(image_name, 'wb') as f:
                f.write(image)
    else:
        logger.error("%s 已存在" % image_name)


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
            logger.info("下载 {} 完成!".format(picture))
        except IOError:
            logger.error("IO Error\n")
            # continue
        finally:
            picture.close
    else:
        logger.error(response.status_code)
        # continue
