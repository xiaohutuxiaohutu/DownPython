import sys
import imghdr
import time
import os
import io
import re

def fileSize():
    i = Image.open(StringIO(imageUrl.content))
    print(i.size)
    return i.size


# 判断文件或文件夹是否存在
def fileExist(fileName):
    return os.path.exists(fileName)


# 判断文件是否存在
def isFile(fileName):
    return os.path.isfile(fileName)
