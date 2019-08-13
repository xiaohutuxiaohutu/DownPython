#coding:utf-8
import os
filePath="E:\\图片\\1535801292420\\"
fielNames=os.listdir(filePath)
errList=[]
print(len(fielNames ))
for fileName in fielNames:
    print(fileName)
    #npos=fileName.index('-')
    new_name = fileName+'.ts'
    try:
        print('修改前：'+fileName)
        print('修改后：'+new_name)
        os.rename(filePath+fileName,filePath+new_name)
        
        print('-----  修改完成 ---------')
    except FileExistsError:
        print(fileName)
        errList.append(fileName)
        pass
print('----All over --------')
'''
for name in errList:
    print(name)
'''
