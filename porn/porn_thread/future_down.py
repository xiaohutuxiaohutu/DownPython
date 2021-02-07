#!/usr/bin/env python3
# from furl import furl
# from pypinyin import pinyin, lazy_pinyin, Style
import logging
import os

# import threading
import porn
from common import FileTool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    file_map = FileTool.get_file_map(os.getcwd() + os.sep, 'txt', 2, '-', 0)
    # 循环分组后的文件列表
    for category_name, file_list in file_map.items():
        # 获取路径
        # dir_path = FileTool.get_classify_dir_path(key)
        print(category_name)
        # 虚幻文件列表
        for index, file_name in enumerate(file_list, 1):
            porn.dow_img_from_file(file_name, category_name)
            print()
            logger.info('第 %i 个文件： %s 下载完毕，开始删除...' % (index, file_name))
            print()
            os.remove(file_name)
            if index == len(file_list):
                logger.info("------------删除成功，所有文件下载完毕------------------")
            else:
                logger.info('第 %i 个文件： %s 删除成功，开始读取下一个文件' % (index, file_name))

    '''
#future.result()会阻塞线程，相当于单线程了
for future in futures.as_completed(fs):
   try:
       print(future.running())
       # print(fs[future])
       data = future.result()
       # logger.info(file_url)
       # logger.info(data)
   except Exception as exc:
       print('%r generated an exception: %s' % (file_url, exc))
   else:
       logger.info(data)
'''
