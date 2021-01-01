# coding:utf-8
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 获取指定目录下 指定类型的文件
def get_file_name_list(file_dir, file_type):
    file_name_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ('.' + file_type):
                file_name_list.append(os.path.join(root, file))
    return file_name_list


def modify_name(file_list):
    # print(name_list)
    # errList = []
    for old_name in file_list:
        # print(old_name)
        npos = old_name.find('Chinese')
        if npos > 0:
            new_file = old_name[0:npos].strip()
            new_name = old_name[0:npos].strip() + '.ts'
            # try:
            print('修改前：' + old_name)
            print('修改后：' + new_name)
            # 判断文件是否存在
            i = 1
            while os.path.exists(new_name):
                print(new_name)
                new_name = new_file + '_' + str(i) + '.ts'
                i += 1
            else:
                os.rename(old_name, new_name)

            print('-----  修改完成 ---------')
        '''
        except FileExistsError:
            logger.info(old_name + "已存在！")
            errList.append(old_name)
            pass
        '''

    print('----All over --------')


if __name__ == '__main__':
    # 用户路径
    user_dir = os.path.expanduser('~') + os.sep
    # print(user_dir)
    filePath = user_dir + "Videos"
    name_list = get_file_name_list(filePath, 'ts')
    # print(name_list)
    modify_name(name_list)
