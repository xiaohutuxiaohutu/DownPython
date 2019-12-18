#!/usr/bin/env python3
import os

import common

temp = 0
for i in range(8, 75):
    print('第 %i 页' % i)
    url = "http://www.ve2s.com/AAbook/AAAtb/changpian/index-%i.html" % i
    if i == 1:
        url = "http://www.ki7r.com/AAbook/AAAtb/changpian/index.html"

    soup = common.get_beauty_soup(url)
    itemUrl = soup.select("body div[class='main'] div[class='classList'] ul li a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        print('fileUrl:' + fileUrl)
        if fileUrl is not None and fileUrl.find('.html') >= 0:
            fileUrl = "https://www.4455sk.com" + fileUrl
            temp += 1
            print("fileUrl:" + fileUrl)
            os.chdir(os.getcwd())
            with open('changpian_%s_%i.txt' % (common.get_datetime('%Y-%m-%d'), temp // 500), 'a+') as f:
                f.write(fileUrl + '\n')
print("打印完成")
