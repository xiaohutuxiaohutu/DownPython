import datetime

import threading
import time

url = 'https://www.790nd.com/piclist3/333869.html'
url_1 = url.split('piclist3')[1].split('.')[0].split('/')[1]
print(url_1)

# down_path = 'D:/图片/PPP91/网友自拍/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'
'''
down_path = 'D:/图片/PPP91/网友自拍/%s/' % (datetime.datetime.now().strftime('%Y-%m-%d'))
print(down_path)
file_path = 'C:/workspace/GitHub/DownPython/PPP91/wyzp/2019-10-07_0.txt'
with open(file_path) as fileObj:
    read = fileObj.read()
    print(read)
'''
url = "https://www.790nd.com/piclist5/index_1.html"

split = url.split('_')[0]
print(split)

url='/AAtupian/AAAwz/136676.html'
split_ = url.split('/')[3].split('.')[0]
print(split_)


def listen_music(name):
    while True:
        time.sleep(1)
        print(name, "正在播放音乐")


def download_music(name):
    while True:
        time.sleep(2)
        print(name, "正在下载音乐")


if __name__ == '__main__':
    p1 = threading.Thread(target=listen_music, args=("网易云音乐",))
    p2 = threading.Thread(target=download_music, args=("网易云音乐",))
    p1.start()
    p2.start()
