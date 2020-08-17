import common
import os

header = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

  'cookie': 'fvlid=1597625585953zQdtJ1EJ4L; sessionip=61.144.97.195; sessionid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; autoid=ac8e7bc62f1d44610e0ccf927310f83b; sessionvid=EF01FBFB-A52F-4D65-A006-FF0739E0F586; area=440113; ahpau=1; __ah_uuid_ng=c_E554438A-793F-4510-A2D6-7E3FC7DEA18E; sessionuid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; pvidchain=6842494,3311253; ahpvno=5; v_no=5; visit_info_ad=E554438A-793F-4510-A2D6-7E3FC7DEA18E||EF01FBFB-A52F-4D65-A006-FF0739E0F586||-1||-1||5; ahrlid=1597625641002gTVBP9NgZm-1597625642889; ref=www.baidu.com%7C0%7C0%7C0%7C2020-08-17+08%3A54%3A03.773%7C2020-08-17+08%3A53%3A06.504'
}
proxy_ip = common.get_ip()


# 获取指定目录下 指定类型的文件
def get_file_map(file_dir, file_type):
  file_map = {}
  for root, dirs, files in os.walk(file_dir):
    for file in files:
      if os.path.splitext(file)[1] == ('.' + file_type):
        key = file.split('-')[0]
        value = file_map.get(key)
        if value is None or value == 'None':
          file_map[key] = [os.path.join(root, file)]
        else:
          value.append(os.path.join(root, file))
          file_map[key] = value
  return file_map


# 获取文件列表
def get_file_list(file_dir, file_type):
  # file_map = {}
  file_list = []
  for root, dirs, files in os.walk(file_dir):
    for file in files:
      if os.path.splitext(file)[1] == ('.' + file_type):
        file_list.append(os.path.join(root, file))
  return file_list
