import os
import logging
import pypinyin
from pypinyin import Style

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
cur_dir = os.getcwd() + os.sep
rootDir = cur_dir[:cur_dir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径


# 获取指定目录下 指定类型的文件
def get_file_name_list(file_dir, file_type):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:

            if os.path.splitext(file)[1] == ('.' + file_type):
                logger.info(file)
                file_name_list.append(os.path.join(root, file))
    return file_name_list


# 获取目录下指定的文件
def get_appoint_file(file_dir, file_type):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file == file_type:
                file_name_list.append(os.path.join(root, file))
    return file_name_list


# 获取指定目录下 指定类型的文件,key为文件名;key_type=1 标识按照文件名分组,==2是按照pattern分割后获取的列表中index
def get_file_map(file_dir, file_type='txt', key_type=1, pattern=None, index=0):
    file_map = {}
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            splitext = os.path.splitext(file)
            if splitext[1] == ('.' + file_type):
                if key_type == 1:
                    key = splitext[0]
                elif key_type == 2:
                    key = file.split(pattern)[index]
                value = file_map.get(key)
                if value is None or value == 'None':
                    file_map[key] = [os.path.join(root, file)]
                else:
                    value.append(os.path.join(root, file))
                    file_map[key] = value
    return file_map


# 获取当前目录下指定类型的文件
def get_cur_file_list(file_type, pattern, file_dir=os.getcwd()):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # print(file)
            if os.path.splitext(file)[1] == ('.' + file_type) and pattern in file:
                file_name_list.append(os.path.join(root, file))
    return file_name_list


def get_classify_dir_path(category_name):
    pypinyin_slug = pypinyin.slug(category_name, separator='', style=Style.FIRST_LETTER)
    # print(pypinyin_slug)
    dir_path = rootDir + 'porn' + os.sep
    if pypinyin_slug.endswith('JH') and 'zpdrycsq' in pypinyin_slug:
        # dir_path = '../jh/zpdr_ycsq_jh/'
        dir_path = dir_path + 'jh/zpdr_ycsq_jh/'
    elif (not pypinyin_slug.endswith('JH')) and 'zpdrycsq' in pypinyin_slug:
        # dir_path = '../all/zpdr_ycsq_all/'
        dir_path = dir_path + 'all/zpdr_ycsq_all/'
    elif pypinyin_slug.endswith('JH') and 'wawq' in pypinyin_slug:
        # dir_path = '../jh/wawq_jh/'
        dir_path = dir_path + 'jh/wawq_jh/'
    elif 'wawq' in pypinyin_slug:
        # dir_path = '../all/wawq_all/'
        dir_path = dir_path + 'all/wawq_all/'
    elif 'xqxt' in pypinyin_slug:
        # dir_path = '../all/xqfx/'
        dir_path = dir_path + 'all/xqfx/'
    elif pypinyin_slug.endswith('JH') and 'yczp' in pypinyin_slug:
        # dir_path = '../jh/yczp_jh/'
        dir_path = dir_path + 'jh/yczp_jh/'
    elif (not pypinyin_slug.endswith('JH')) and 'yczp' in pypinyin_slug:
        # dir_path = '../all/yczp_all/'
        dir_path = dir_path + 'all/yczp_all/'
    return dir_path


def mkdir(path):
    if not os.path.exists(path):
        logger.info('新建文件夹:', path)
        os.makedirs(path)
        return True
    else:
        # print("图片存放于:", os.getcwd() + os.sep + path)
        print("图片存放于:", path)
        return False


# 判断文件或文件夹是否存在
def file_exist(file_path):
    return os.path.exists(file_path)


# 判断文件夹是否存在，不存在则创建
def create_file(file_path):
    if not (os.path.exists(file_path)):
        os.makedirs(file_path)


# 判断文件是否存在
def is_file(file_name):
    return os.path.isfile(file_name)
