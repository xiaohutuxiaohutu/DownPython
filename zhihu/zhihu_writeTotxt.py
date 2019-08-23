import common
import re
import requests
import os
import sys

curDir = os.path.abspath(os.curdir)  # 当前文件路径
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取DownPython，也就是项目的根路径
sys.path.append(rootDir)
doneDownPath = curDir + '/doneDown.text'
common.create_file(doneDownPath)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate'}


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
        img_reg = re.compile('data-original="(.*?)"', re.S)
        for answer in answers:
            tmp_list = []
            url_items = re.findall(img_reg, answer)
            for item in url_items:  # 这里去掉得到的图片URL中的转义字符'\\'
                image_url = item.replace("\\", "")
                tmp_list.append(image_url)
            # 清理掉头像和去重 获取data-original的内容
            tmp_list = list(set(tmp_list))  # 去重
            # print(tmp_list)
            # print('tmp_list:' + str(len(tmp_list)))
            for item in tmp_list:
                pattern = re.compile(r'^https://.*.(jpg|png|gif|jpeg)$')
                if pattern.match(item):
                    # if item.endswith('r.jpg'):
                    # print(item)
                    image_urls.append(item)
        print('size: %d, num : %d' % (size, len(image_urls)))


if __name__ == '__main__':
    os.chdir(curDir)
    question_id = 310786985
    with open('question_id.text', 'a+') as qid_file:
        qid_file.write(str(question_id) + '\n')
    # url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)
    img_list = get_image_url(question_id, headers)  # 获取图片的地址列表
    print(len(img_list))
    temp = 0
    for i in range(0, len(img_list)):
        img_url = img_list[i]
        # img_name = img_url.split("/")[-1]
        img_name = os.path.basename(img_url)
        temp += 1
        with open(doneDownPath) as f:
            readLines = f.readlines()
        os.chdir(curDir)
        if (img_name + '\n') not in readLines:
            common.save_url_down(doneDownPath, img_url, img_name, temp)
        else:
            print('第' + str(i + 1) + '个已存在:' + img_url)
