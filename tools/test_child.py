import os
import sys
import common
import re

curDir = os.path.abspath(os.curdir)
rootDir = curDir[:curDir.find("DownPython\\") + len("DownPython\\")]  # 获取myProject，也就是项目的根路径
sys.path.append(rootDir)

url = 'https://f.wonderfulday30.live/viewthread.php?tid=346269&extra=page%3D7%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3D2592000'
soup = common.get_beauty_soup(url)
title = soup.title.string
new_title = common.replace_sub(title)
print(new_title)
# resultTags = soup.find_all(id=re.compile('normalthread'))
select = soup.select("body div[id='wrap']  div[class='forumcontrol s_clear'] table tr td div[class='pages'] a[href]")
print(len(select))
preUrl = 'https://f.wonderfulday30.live/'
for item in select:
    print(item.get('href'))
