# -*- coding:utf-8 -*-
import re
import requests
import os
import sys
import common
from os.path import basename

import urllib.parse
curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# sys.path.append(r"C:\workspace\GitHub\DownPython")
sys.path.append(rootDir)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate'}

userPath = os.path.expanduser('~')  # 获取用户目录


def get_image_url(qid, headers):
    # 利用正则表达式把源代码中的图片地址过滤出来
    # reg = r'data-actualsrc="(.*?)">'
    tmp_url = "https://www.zhihu.com/node/QuestionAnswerListV2"
    size = 0
    image_urls = []
    session = requests.Session()
    while True:
        postdata = {'method': 'next', 'params': '{"url_token":' +
                                                str(qid) + ',"pagesize": "0",' + '"offset":' + str(size) + "}"}
        page = session.post(tmp_url, headers=headers, data=postdata)
        ret = eval(page.text)
        answers = ret['msg']
        print("答案数 : %d " % (len(answers)))
        size += 10
        if not answers:
            print("图片URL获取完毕, 页数: ", (size - 10) / 10)
            return image_urls
        # reg = r'https://pic\d.zhimg.com/[a-fA-F0-9]{5,32}_\w+.jpg'
        imgreg = re.compile('data-original="(.*?)"', re.S)
        for answer in answers:
            tmp_list = []
            url_items = re.findall(imgreg, answer)
            for item in url_items:  # 这里去掉得到的图片URL中的转义字符'\\'
                image_url = item.replace("\\", "")
                tmp_list.append(image_url)
            # 清理掉头像和去重 获取data-original的内容
            tmp_list = list(set(tmp_list))  # 去重
            for item in tmp_list:
                if item.endswith('r.jpg'):
                    # print(item)
                    image_urls.append(item)
        print('size: %d, num : %d' % (size, len(image_urls)))


def download_pic(img_lists, dir_name):
    print("一共有 {} 张照片".format(len(img_lists)))
    if not os.path.exists(dir_name):  # 新建文件夹
        os.mkdir(dir_name)
    os.chdir(dir_name)
    for i, image_url in enumerate(img_lists):
        # print(image_url)
        # file_name = basename(urllib.parse.urlsplit(image_url)[2])
        # print('file_name:'+file_name)
        print(image_url.split("/")[-1])
        if not os.path.exists(image_url.split("/")[-1]):
            print('下载第' + str(i + 1) + '个:' + image_url)
            common.down_img(image_url)
        else:
            print('第' + str(i + 1) + '个已存在:' + image_url)


if __name__ == '__main__':
    # question_id = 30061914 32762402
    question_id = 336969810
    zhihu_url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
    # 文件下载保存路径
    downFilePath = userPath + '/Pictures/zhihu/'
    common.mkdir(downFilePath)  # 创建本地文件夹
    img_list = get_image_url(question_id, headers)  # 获取图片的地址列表
    print(img_list)
    print(len(img_list))
    download_pic(img_list, downFilePath)  # 保存图片
