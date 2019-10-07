import os
import sys
curDir = os.getcwd()
print(curDir)
with open('C:/workspace/GitHub/DownPython/porn/all/xqfx/down-done.text') as file_obj:
    read_lines = file_obj.readlines()

    for item in read_lines:
        strip = item.strip('\n')
        # print(strip)
        if strip:
            split = strip.split("=")
            split_ = split[1]
            print(split_)
            with open(curDir+'/DoneDown.text', 'a+') as new_file:
                new_file.write(split_ + '\n')
