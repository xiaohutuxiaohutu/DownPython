# from furl import furl
# from pypinyin import pinyin, lazy_pinyin, Style
import logging
import os
import time
from concurrent import futures

import common
import porn
from common import DownTool
from common import FileTool
from common import ProxyIp
from common import BeautySoupTool

# 重新下载未完成
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
cur_dir = os.getcwd() + os.sep


def save_fail_url(urls):
    try:
        with open(file_dir + 'un_down_' + common.get_datetime('%Y-%m-%d') + '.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            logger.info('写入前文本数量：%i, 写入数量：%i；写入后总量%i' % (len(lines), len(urls), len(lines) + len(urls)))
    except IOError:
        logger.error('error: 没有找到文件或读取文件失败,待写入数量：%i' % len(urls))

    with open(file_dir + 'un_down_' + common.get_datetime('%Y-%m-%d') + '.log', 'a+', encoding='utf-8') as f:
        for value in urls:
            f.write('%s:[%s,%s]\n' % (common.get_datetime('%Y/%m/%d %H:%M'), value['url'].strip('\n'), value['title']))


def down_file(url_list):
    un_done = []
    for index, url in enumerate(url_list, 1):
        if url.strip() == '':
            continue
        # 获取所有图片连接
        logger.info('获取当前链接下的所有图片链接。。。。。。。')
        url_list = porn.get_img_url_list(url)
        img_urls = url_list[0]
        new_title = url_list[1]
        logger.info('第 %i 行： -%s- ; 图片数量： %i ;%s' % (index, url, len(img_urls), new_title))
        if len(img_urls) < 2:
            if '删' not in str(new_title):
                temp_un_down = {'url': url, 'title': str(new_title)}
                un_done.append(temp_un_down)
                continue
            elif '删' in str(new_title):
                continue
        else:
            path = porn.create_down_root_path(classify_name, str(new_title.strip()))  # path_ + str(new_title.strip()) + os.sep
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
                    logger.info('第 %i 行： -%s- ;url:%s;文件 %s已存在 ' % (index, url, file_url, image_name))
            if len(need_down) > 0:
                with futures.ThreadPoolExecutor(max_workers=5 if len(need_down) > 5 else len(need_down), thread_name_prefix="down-thread") as executor:
                    for index1, value1 in enumerate(need_down, 1):
                        submit = executor.submit(DownTool.future_dowm_img, value1['file_url'], ProxyIp.ProxyIp().get_random_proxy_ip(), index, len(need_down), index1, value1['path'])
                        # submit完成之后的回调函数
                        submit.add_done_callback(common.executor_callback)
                        fs.append(submit)
                futures.wait(fs, timeout=15)
            logger.info('第 %i 行： %s 下载完毕；用时：%i ' % (index, url, time.time() - start))
        # 保存所有的下载链接
        os.chdir(cur_dir)
        porn.write_to_done_log(url, new_title, file_dir)
        # time.sleep(1)
    return un_done


def distinct_url():
    # 先打开文件，去重
    down_urls = []
    with open(file_path, encoding='utf-8') as file_obj:
        for num, value in enumerate(file_obj, 1):
            line = value.strip('\n')
            if line == '':
                continue
            start = line.find('https')
            end = line.find(',')
            down_url = line[start:end]
            down_urls.append(down_url)
    logger.info('去重前数据：' + str(len(down_urls)))
    list_distinct = common.list_distinct(down_urls)
    logger.info('去重后数据：' + str(len(list_distinct)))
    return list_distinct


# 删除***.log中包含 删 字段的连接
def filter_delete():
    down_urls = []
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        logger.info('过滤前文本行数：%i' % len(lines))
    with open(file_path, encoding='utf-8') as file_obj:
        for num, value in enumerate(file_obj, 1):
            line = value.strip('\n')
            if line == '':
                continue
            end = line.find(',')
            title = line[end:]
            if '删' not in title:
                down_urls.append(value)
    logger.info('过滤后文本行数：%i；开始写入文件' % len(down_urls))
    # 重新写入文件
    with open(file_path, 'w+', encoding='utf-8') as file_obj:
        for line in down_urls:
            file_obj.write(line)


def write_distinct():
    with open(file_path, 'r+', encoding='utf-8') as f:
        for value in all_urls:
            f.write('%s:[%s,%s]\n' % (common.get_datetime('%Y/%m/%d %H:%M'), value['url'].strip('\n'), value['title']))


# 重新下载 下载失败的的log文件
if __name__ == '__main__':
    # classify_name = '自拍达人原创申请'
    # file_dir = common.get_project_dir() + 'porn' + os.sep + 'all' + os.sep + 'zpdr_ycsq_all' + os.sep
    # file_path = file_dir + 'un_done.log'

    # classify_name = '兴趣分享'
    # file_dir = common.get_project_dir() + 'porn' + os.sep + 'all' + os.sep + 'xqfx' + os.sep
    # file_path = file_dir + 'un_down.log'

    classify_name = '我爱我妻'
    file_dir = common.get_project_dir() + 'porn' + os.sep + 'all' + os.sep + 'wawq_all' + os.sep
    file_path = file_dir + 'un_down.log'

    # classify_name = '原创自拍区'
    # file_dir = common.get_project_dir() + 'porn' + os.sep + 'all' + os.sep + 'yczp_all' + os.sep
    # file_path = file_dir + 'un_down.log'

    # classify_name = '自拍达人原创申请_JH'
    # file_dir = common.get_project_dir() + 'porn' + os.sep + 'jh' + os.sep + 'zpdr_ycsq_jh' + os.sep
    # file_path = file_dir + 'un_done.log'

    # classify_name = '我爱我妻_JH'
    # file_dir = common.get_project_dir() + 'porn' + os.sep + 'jh' + os.sep + 'wawq_jh' + os.sep
    # file_path = file_dir + 'un_down.log'

    filter_delete()

    # 去重后的数据
    all_urls = distinct_url()

    # 将去重后的数据写入原来的文件
    write_distinct()

    # 未下载的数据
    fail_urls = down_file(all_urls)

    # 保存未下载的数据
    save_fail_url(fail_urls)
