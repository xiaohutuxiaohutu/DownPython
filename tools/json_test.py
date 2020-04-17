import json
import os

list = [1, 2, 3, 4]
dumps = json.dumps(list)
# print(dumps)
cur_dir = os.getcwd()
with open(cur_dir + os.sep + 'list.json', 'a+') as f:
    json.dump(list, f)

with open(cur_dir + os.sep + 'list.json', 'a+') as f1:
    f1.readline()
    # load = json.load(f)
    print(f1.readline())
