import datetime
import os
import common
import xs

curDir = os.path.abspath(os.curdir)  # 当前文件路径
userPath = os.path.expanduser('~')  # 获取用户目录
down_path = 'D:/图片/667xs/制服美腿/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
file_name = curDir + '/tpzp-2019-10-07_9.text'
with open(file_name) as file_obj:
    for num, value in enumerate(file_obj, 1):
        line = value.strip('\n')
        print('第' + str(num) + '行：' + line)
        urls = xs.get_img_urls(line, 'gb2312', '_制服美腿')
        img_urls = urls[0]
        new_title = urls[1]
        s = str(len(img_urls))
        path = down_path + str(new_title) + '/'
        if not (os.path.exists(path)):
            os.makedirs(path)
        os.chdir(path)
        if len(img_urls) <= 1:
            os.chdir(curDir)
            f = open(datetime.datetime.now().strftime('%Y-%m-%d') + '_未下载.txt', 'a+', encoding='utf-8')
            f.write('第' + str(num) + '行：' + line + ',' + new_title + '\n', )
            f.close()
        else:
            for i in range(0, len(img_urls)):
                img_url = img_urls[i].get('src')
                # if img_url.startswith('http://tu.2015img.com'):
                os.chdir(path)
                image_name = img_url.split("/")[-1]
                if not os.path.exists(image_name):
                    print('下载第' + str(num) + '行；第' + str(i + 1) + ' / ' + s + ' 个: ' + img_url)
                    common.down_img(img_url)
                else:
                    print('第' + str(num) + '行；第' + str(i + 1) + ' / ' + s + ' 个:已存在 ' + img_url)
os.remove(file_name)
