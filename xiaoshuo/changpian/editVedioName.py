#coding:utf-8
import os
filePath="G:\\down\\长篇小说\\2019-02-12\\"
fielNames=os.listdir(filePath)
errList=[]
print(len(fielNames ))
for fileName in fielNames:
    npos=fileName.index('-淫色淫色-黄色小说频道')
    print(npos)
    new_name = fileName[0:npos]+'.txt'
    try:
        print('修改前：'+fileName)
        print('修改后：'+new_name)
        os.rename(filePath+fileName,filePath+new_name)
        
        print('-----  修改完成 ---------')
    except FileExistsError:
        #print(fileName)
        errList.append(fileName)
        pass
print('----All over --------')
for name in errList:
    print(name)
