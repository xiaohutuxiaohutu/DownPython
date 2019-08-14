import os
import sys

curDir = os.getcwd()
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)
import common

print(common.get_ip())

# curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# rootPath = curPath[:curPath.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
# print(rootPath)

print(rootDir)  # 获取当前工作目录路径
# print(os.path.abspath('.'))  # 获取当前工作目录路径
# print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
# print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
