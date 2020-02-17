import os
import sys

curDir = os.getcwd()
print(os.curdir)
print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
print(os.getcwd())


def test_os_method():
    root_dir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
    sys.path.append(root_dir)
    print(os.path.expanduser('~'))
    print(os.path.expandvars('$HOME'))
    print(os.environ['HOME'])
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.abspath('.'))  # 获取当前工作目录路径
    print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
    print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
    print(os.sep)


def read_lines():
    with open(curDir + "/down-done.txt", 'a+') as file_obj:
        read_lines = file_obj.readlines()

    for item in read_lines:
        strip = item.strip('\n')
        print(strip)
        with open(curDir + "/new_down-done.txt", ) as new_file:
            new_lines = new_file.readlines()
        if item not in new_lines:
            os.chdir(curDir)
            with open(curDir + "/new_down-done.txt", 'a+') as new_down_file:
                new_down_file.write(item)


def test_method():
    file_path = 'C:/workspace/GitHub/DownPython/porn/all/自拍达人原创申请/2019-08-23_未下载.text'
    print(os.path.basename(file_path))  # 获取文件名
    print(os.path.dirname(file_path))  # 获取文件路径
    print(os.path.splitext(file_path))  # 获取文件类型

    http_url = 'https://pic1.zhimg.com/50/v2-f4fa476367e6a4620dbdf9e8d817193f_r.jpg?extent=1&sss=2'
    print(os.path.basename(http_url))  # 获取文件名
    print(os.path.dirname(http_url))  # 获取文件路径


# params = {'pre_url': 'https://f.wonderfulday29.live/', 'down_path': ''}
# print(params['pre_url'])
# test_method()
print('***获取当前目录***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

print('***获取上级目录***')
print(os.path.dirname(os.getcwd()))
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
