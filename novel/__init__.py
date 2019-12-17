import os
import common

cur_dir = os.getcwd() + os.sep
pre_url = 'https://www.4455sk.com'
cur_month = os.sep + common.get_datetime('%Y-%m') + os.sep


# 获取下载连接
def write_to_text(params):
    temp = 0
    start_page = params['start_page']
    end_page = params['end_page']
    select_str = params['select_str']
    down_url = params['down_url']
    done_down_text = cur_dir + params['done_down_text']
    with open(done_down_text, 'a+') as fileObj:
        readLines = fileObj.read().splitlines()
    for i in range(start_page, end_page):
        soup = common.get_beauty_soup(down_url % i)
        itemUrl = soup.select(select_str)

        for j in range(0, len(itemUrl)):
            fileUrl = itemUrl[j].get('href')
            print('fileUrl:' + fileUrl)
            if fileUrl is not None and fileUrl.find('.html') >= 0 and fileUrl not in readLines:
                os.chdir(cur_dir)
                # 保存已下载连接
                with open(done_down_text, 'a+') as ff:
                    ff.write(fileUrl + '\n')
                fileUrl = pre_url + fileUrl
                temp += 1
                print("fileUrl:" + fileUrl)
                # 保存下载连接
                with open(common.get_datetime('%Y-%m-%d') + '_' + str(temp // 500) + '.txt', 'a+') as f:
                    f.write(fileUrl + '\n')


# 下载文本
def down_noval(params):
    # 文件下载路径
    down_path = params['down_file_path'] + cur_month
    select_str = params['select_str']
    require_pre_url = params['require_pre_url']
    if require_pre_url:
        pre_url_ = params['pre_url']
    if not (os.path.exists(down_path)):
        os.makedirs(down_path)
    file_name_list = common.get_file_name_list(cur_dir, 'txt')
    for index, file_name in enumerate(file_name_list, 1):
        print('下载第 %i 个文件： %s' % (index, file_name))
        # 打开文件
        with open(file_name) as file_obj:
            for num, value in enumerate(file_obj, 1):
                line = value.strip('\n')
                if require_pre_url:
                    line = pre_url_ + line
                print('第 %i 行： %s' % (num, line))
                soup = common.get_beauty_soup(line)
                title = common.replace_special_char(soup.title.string)
                newTitle = title.split('www')[-1]

                print(str(newTitle.strip()))
                textContent = soup.select(select_str)
                print('text数量：' + str(len(textContent)))
                if len(textContent) == 0:
                    os.chdir(os.getcwd())
                    with open(common.get_datetime('%Y-%m-%d') + '_未下载.txt', 'a+') as f:
                        f.write('第' + str(num) + '行：' + line + ',' + newTitle + '\n')
                else:
                    os.chdir(down_path)
                    with open(newTitle.strip() + '.txt', 'a+', encoding='utf8') as f:
                        for i in range(0, len(textContent)):
                            text = textContent[i].text
                            os.chdir(down_path)
                            f.write(text + '\n')
                print("-----down over----------------")
