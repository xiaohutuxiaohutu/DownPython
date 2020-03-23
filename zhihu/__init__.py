import os
import re

import requests

import common

cur_dir = os.getcwd()
parent_dir = os.path.dirname(os.getcwd())
print('parent_dir:' + parent_dir)

done_down_file_path = parent_dir + '/doneDown.text'
question_id_path = parent_dir + '/question_id.text'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate'}


def get_image_url(qid):
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
        img_reg = re.compile('data-original="(.*?)"', re.S)
        for answer in answers:
            tmp_list = []
            url_items = re.findall(img_reg, answer)
            for item in url_items:  # 这里去掉得到的图片URL中的转义字符'\\'
                image_url = item.replace("\\", "")
                tmp_list.append(image_url)
            # 清理掉头像和去重 获取data-original的内容
            tmp_list = list(set(tmp_list))  # 去重
            for item in tmp_list:
                pattern = re.compile(r'^https://.*.(jpg|png|gif|jpeg)$')
                if pattern.match(item):
                    # if item.endswith('r.jpg'):
                    # print(item)
                    image_urls.append(item)
        print('size: %d, num : %d' % (size, len(image_urls)))


def save_question_id(question_id_path, question_id):
    with open(question_id_path, 'a+') as f:
        f.seek(0, 0)
        read_lines = f.read().splitlines()  # 去除换行符
        if str(question_id) not in read_lines:
            f.write(str(question_id) + '\n')


def write_txt(params):
    os.chdir(cur_dir)
    question_id = params['question_id']
    save_question_id(question_id_path, question_id)
    # url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)

    img_list = get_image_url(question_id)  # 获取图片的地址列表
    print(len(img_list))
    temp = 0
    with open(done_down_file_path) as file_obj:
        readLines = file_obj.read().splitlines()
    for i in range(0, len(img_list)):
        img_url = img_list[i]
        # img_name = img_url.split("/")[-1]
        img_name = os.path.basename(img_url)
        temp += 1
        os.chdir(cur_dir)
        if img_name not in readLines:
            file_name = '%s_%i.txt' % (common.get_datetime('%Y-%m-%d_%H-%M'), temp // 500)
            with open(file_name, 'a+') as f:
                f.write(img_url + '\n')
            # 保存已下载的连接，防止重复下载
            with open(done_down_file_path, 'a+') as f:
                f.write(img_name + '\n')
        else:
            print('第' + str(i + 1) + '个已存在:' + img_url)


def down_zhihu_pic(param):
    down_path = param['down_path']
    question_id = param['question_id']
    url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
    soup = common.get_beauty_soup(url)
    title = common.replace_sub(soup.title.string)
    print(title)
    down_path = down_path + os.sep + title
    if not (os.path.exists(down_path)):
        os.makedirs(down_path)
    # 获取当前目录下所有的待下载txt
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    # print(name_list)
    for num, file_name in enumerate(file_name_list, 1):
        print('下载第' + str(num) + '个文件：' + file_name)
        with open(file_name, 'r') as fileObject:
            for num, value in enumerate(fileObject, 1):
                print('第%i行' % (num), end=' ; ')
                img_url = value.strip('\n')
                image_name = img_url.split("/")[-1]
                os.chdir(down_path)
                if not os.path.exists(image_name):
                    print('下载第%i个：%s' % (num, img_url), end=" ; ")
                    common.down_img(img_url)
                else:
                    print('第' + str(num + 1) + '个已存在:' + img_url)
            print(file_name + "-----down over----------------")
        print('删除文件：' + file_name)
        os.remove(file_name)
    print("-----***************down all over********************----------------")
