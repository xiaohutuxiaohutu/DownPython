# coding:utf-8
import os
from urllib import parse
import datetime
import time

# filePath = "C:\\Users\\23948\\Pictures\\111\\黑发、金发美腿丝袜MM相映成趣60P\\"
root_path = 'D:/图片/PPP91/美腿/todo/'
filePath = "D:/图片/PPP91/美腿/todo/%s/"
fielNames = os.listdir(root_path)
errList = []
print(len(fielNames))
for fileName in fielNames:
    new_path = filePath % fileName
    print('fileName: ' + fileName)
    listdir = os.listdir(new_path)
    for name in listdir:
        print('name: ' + name)
        unquote = parse.unquote(name)
        print(unquote)
        split = unquote.split('/')
        print(split)
        if len(split) == 3:
            try:
                os.rename(new_path + name, new_path + split[2])
            except FileExistsError:
                # print(fileName)
                t = time.time()
                i = int(round(t * 1000000))
                os.rename(new_path + name, new_path + str(i) + '-' + split[2])
                pass
print('修改完成')
for name in errList:
    print('----以下修改不成功----')
    print(name)
