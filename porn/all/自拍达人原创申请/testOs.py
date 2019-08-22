import os
import sys
import common

curDir = os.getcwd()
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)
print(os.path.expanduser('~'))
# print(os.path.expandvars('$HOME'))
# print(os.environ['HOME'])
# print(common.get_ip())
with open(curDir + "/down-done.txt") as file_obj:
    read_lines = file_obj.readlines()
new_down = curDir + "/done-down.txt"
# common.create_file(new_down)

for item in read_lines:
    strip = item.strip('\n')
    print(strip)
    with open(new_down) as new_file:
        new_lines = new_file.readlines()
    if item not in new_lines:
        os.chdir(curDir)
        with open(new_down, 'a+') as new_down_file:
            new_down_file.write(item)
# curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# rootPath = curPath[:curPath.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# print(rootPath)

print(rootDir)  # 获取当前工作目录路径
# print(os.path.abspath('.'))  # 获取当前工作目录路径
# print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
# print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
