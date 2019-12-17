import os
import common

temp = 0
for i in range(1, 47):
    print('第' + str(i) + '页')
    url = "https://www.4455sk.com/xiaoshuo/list-武侠古典-%i.html" % i
    soup = common.get_beauty_soup(url)
    itemUrl = soup.select(
        "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a")

    for j in range(0, len(itemUrl)):
        fileUrl = itemUrl[j].get('href')
        # print('fileUrl:'+fileUrl)
        if fileUrl is not None and fileUrl.find('.html') >= 0:
            fileUrl = "https://www.4455sk.com" + fileUrl
            temp += 1
            print("fileUrl:" + fileUrl)
            os.chdir(os.getcwd())
            with open('wuxia_%s_%i.txt' % (common.get_datetime('%Y-%m-%d'), temp // 500), 'a+') as f:
                f.write(fileUrl + '\n')
print("打印完成")
