import os
import re

import requests

import common
import threading

cur_dir = os.getcwd()
parent_dir = os.path.dirname(os.getcwd())
# print('parent_dir:' + parent_dir)

done_down_file_path = parent_dir + os.sep + 'done' + os.sep + '%i_doneDown.text'
question_id_path = parent_dir + os.sep + 'question_id.text'

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
        if len(answers) == 0:
            return image_urls
        size += 10
        print("答案数 : %d " % (len(answers)))
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
                    image_urls.append(item)
        print('size: %d, num : %d' % (size, len(image_urls)))


def save_question_id(question_id_path, question_id):
    with open(question_id_path, 'a+') as f:
        f.seek(0, 0)
        read_lines = f.read().splitlines()  # 去除换行符
        if str(question_id) not in read_lines:
            f.write(str(question_id) + '\n')


gLock = threading.Lock()


def write_txt(params):
    gLock.acquire()
    os.chdir(cur_dir)
    question_id = params['question_id']
    save_question_id(question_id_path, question_id)
    # url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)

    img_list = get_image_url(question_id)  # 获取图片的地址列表
    if len(img_list) == 0:
        return
        # print(len(img_list))
    temp = 0
    done_down_path = done_down_file_path % question_id
    with open(done_down_path, 'w+') as file_obj:
        readLines = file_obj.read().splitlines()

    with open(parent_dir + '/doneDown.text') as obj:
        readLinesCopy = obj.read().splitlines()
        readLines.extend(readLinesCopy)
    print('done-length:', end=" ")
    print(len(readLines))
    for i in range(0, len(img_list)):
        img_url = img_list[i]
        # img_name = img_url.split("/")[-1]
        img_name = os.path.basename(img_url)
        temp += 1
        os.chdir(cur_dir)
        if img_name not in readLines:
            file_name = '%i_%s_%i.txt' % (question_id, common.get_datetime('%Y-%m-%d_%H-%M'), temp // 500)
            with open(file_name, 'a+') as f:
                f.write(img_url + '\n')
            # 保存已下载的连接，防止重复下载
            with open(done_down_path, 'a+') as f:
                f.write(img_name + '\n')
        else:
            print('第' + str(i + 1) + '个已存在:' + img_url)
        if img_name in readLinesCopy:
            # 保存旧的连接，防止文件太大
            with open(done_down_path, 'a+') as f:
                f.write(img_name + '\n')

    gLock.release()


def get_file_txt(question_id, file_type, cur_dir):
    for root, dirs, files in os.walk(cur_dir):
        file_name_list = []
        for file in files:
            # print(file)
            if file.startswith(str(question_id)) and os.path.splitext(file)[1] == ('.' + file_type):
                file_name_list.append(os.path.join(root, file))
    return file_name_list


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
    file_name_list = get_file_txt(question_id, 'txt', cur_dir)
    # file_name_list = common.get_file_name_list(cur_dir, 'txt')
    # print(name_list)
    for num, file_name in enumerate(file_name_list, 1):
        print('下载第' + str(num) + '个文件：' + file_name)
        with open(file_name, 'r') as fileObject:
            for num, value in enumerate(fileObject, 1):
                print('第%i行' % (num), end=' ; ')
                img_url = value.strip('\n')
                if img_url == '':
                    print('当前行为空：%i line' % num)
                    continue
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


def compare_down():
    old_file = parent_dir + os.sep + 'doneDown.text'
    print(old_file)
    new_file = parent_dir + os.sep + 'new_done_down.text'
    # 读取done文件下内容
    file_list = common.get_file_name_list(cur_dir, 'text')
    print(file_list)
    list = []
    for num, file_name in enumerate(file_list, 1):
        print('读取第%i个文件：%s' % (num, file_name))
        with open(file_name, 'r') as fileObject:
            readLines = fileObject.read().splitlines()
            list.extend(readLines)
    print(len(list))
    new_num = 0
    old_num = 0
    with open(old_file) as obj:
        for num, value in enumerate(obj, 1):
            old_num = old_num + 1
            img_name = value.strip('\n')
            if img_name == '':
                print('当前行为空：%i line' % num)
                continue
            elif img_name not in list:
                print('第%i行:%s 不存在，写入新文件' % (num, img_name))
                new_num = new_num + 1
                with open(new_file, 'a+') as f:
                    f.write(img_name + '\n')
    print('读取旧文件行数：%i; 写入新文件行数：%i' % (old_num, new_num))
    # 比对，如果不在done文件下，写入新文件
