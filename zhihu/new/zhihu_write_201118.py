#!/usr/bin/env python3
import json
import os
import time
import requests
from pyquery import PyQuery as pq

import common

cur_dir = os.getcwd()
parent_dir = os.path.dirname(os.getcwd())
print('parent_dir:' + parent_dir)

done_down_file_path = parent_dir + os.sep + 'done' + os.sep + '%i_doneDown.text'
question_id_path = parent_dir + os.sep + 'question_id.text'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate',

    'cookie': '_xsrf=qOXZsVd6NGOKZh6tUmOG4xsjxK4tfX9a; _zap=265dd66d-39ec-481d-8bb1-983e5776e8cf; q_c1=567acd3ddf5a46009972f7972478fdc5|1605495526000|1605495526000; d_c0="AJAQ9Hf3MxKPTmw5YoJwZebNDhuo8CxtP3c=|1605505069"; capsion_ticket="2|1:0|10:1605505069|14:capsion_ticket|44:Y2JhZjQ1MDE3NjE5NGY1YWE1ZDEzMGUxY2RkNTBlNDE=|18d06bd2fb972a9025cc1e2b149b2cfaefca03cadec97043d77d6a4dee90bdad"; z_c0="2|1:0|10:1605505087|4:z_c0|92:Mi4xbnRCS0F3QUFBQUFBa0JEMGRfY3pFaVlBQUFCZ0FsVk5QMTZmWUFBTFFmN216UTZPd3ZvdWhQRFhJLWtoQlQ2ajNB|4bdf4e8a938f447f5dc2b56d2b302be51c3bde61b47461c607640085bdf4bed1"; tst=r; SESSIONID=5Mkr6Fr7hRX9sDoCYqvXXGQVfHHfQ51Pux1nquDGjfd; JOID=VlATAkxHaSdjHevuYUJWOqxkGdJxfipLFyihklEsN3FdaKyNLPoXkjkS6edgk8YFMmObAiWZ8yxsvlZi-BKT8Aw=; osd=VlodAk9HYyljHuvkb0JVOqZqGdFxdCRLFCirnFEvN3tTaK-NJvQXkTkY5-djk8wLMmCbCCuZ8CxmsFZh-Bid8A8=; anc_cap_id=c8199b4a7ab64ce39fcdc85eed716fc0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1605505069,1605574087,1605662652,1605668419; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1605668472; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1605670685|1605662650'
}


def get_image_url(qid, next_page):
    # next_page = 'https://www.zhihu.com/api/v4/questions/420285724/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bsettings.table_of_content.enabled%3B&limit=20&offset=0&platform=desktop&sort_by=default'
    done_down_path = done_down_file_path % qid
    if not os.path.exists(done_down_path):
        with open(done_down_path, 'w+') as cf:
            readLines = cf.read().splitlines()
            print('file not exist ;create file :%s' % done_down_path)
    else:
        with open(done_down_path, 'r') as file_obj:
            readLines = file_obj.read().splitlines()

    with open(parent_dir + '/doneDown.text') as obj:
        readLinesCopy = obj.read().splitlines()
        readLines.extend(readLinesCopy)

    while True:
        post = requests.get(next_page, headers=headers)
        # print(post)
        loads = json.loads(post.text)
        if loads.get('error'):
            print(loads.get('error'))
            return
        data = loads.get('data')
        if len(data) == 0:
            return
        else:
            print('总回答数量：%s' % loads.get('paging').get('totals'))
            # 获取图片链接
            print('当前页回答数量：%i' % len(data))
            temp = 0
            for i, item in enumerate(data):
                content = pq(item['content'])
                imgUrls = content.find('noscript img').items()

                for imgTag in imgUrls:
                    src = imgTag.attr("src")
                    img_name = os.path.basename(src).split('?')[0]
                    temp += 1
                    os.chdir(cur_dir)
                    if img_name not in readLines:
                        # 保存图片下载链接到 txt
                        file_name = '%i_%s_%i.txt' % (qid, common.get_datetime('%Y-%m-%d_%H-%M'), temp // 500)
                        with open(file_name, 'a+') as f:
                            f.write(src + '\n')
                        # 保存已下载的连接，防止重复下载
                        with open(done_down_path, 'a+') as f:
                            f.write(img_name + '\n')
                    else:
                        print('第' + str(temp + 1) + '个已存在:' + src)
                    if img_name in readLinesCopy:
                        # 保存旧的图片名字到 done\qid_doneDown.text，防止doneDown.text文件太大
                        with open(done_down_path, 'a+') as f:
                            f.write(img_name + '\n')
            # 获取下一页
        next_page = loads.get('paging').get('next')
        time.sleep(3)

        # print(next_page)


if __name__ == '__main__':
    # 385322368
    qid = 385322368
    next_page = 'https://www.zhihu.com/api/v4/questions/%i/answers?' % qid
    include = 'include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bsettings.table_of_content.enabled%3B&limit=20&offset=0&platform=desktop&sort_by=default'

    # print(next_page + include)
    get_image_url(qid, next_page + include)
