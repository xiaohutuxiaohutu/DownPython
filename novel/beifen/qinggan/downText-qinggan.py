import os

import common

# 获取总行数
path = 'D:/down/qinggan/%s/' % common.get_datetime('%Y-%m-%d')
if not (os.path.exists(path)):
    os.makedirs(path)

file_list = common.get_file_name_list(os.getcwd(), 'txt')
for index, file_name in enumerate(file_list, 1):
    print('下载第 %i 个文件： %s' % (index, file_name))
    # 打开文件
    with open(file_name) as file_obj:
        for num, value in enumerate(file_obj, 1):
            line = value.strip('\n')
            print('第 %i 行： %s' % (num, line))
            itemSoup = common.get_beauty_soup(line)
            title = common.replace_special_char(itemSoup.title.string)
            newTitle = title.split('www')[-1]

            print(str(newTitle.strip()))
            textContent = itemSoup.select(
                "body div[class='maomi-content'] main[id='main-container'] div[class='content']")
            if len(textContent) == 0:
                with open('qinggan_%s_未下载.txt' % common.get_datetime('%Y-%m-%d'), 'a+') as f:
                    f.write('第 %i 行：%s ; %s \n' % (num, line, newTitle) + str(num))
            else:
                with open(newTitle.strip() + '.txt', 'a+', encoding='utf8') as f:
                    for i in range(0, len(textContent)):
                        text = textContent[i].text
                        os.chdir(path)
                        f.write(text + '\n')
            print("-----down over----------------")
print("all over")
