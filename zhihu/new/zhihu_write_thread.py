#!/usr/bin/env python3
import zhihu
from multiprocessing import Process
import threading

question_id = [1231860133

               ]
# , , 1075898334, 1238282965, 1136933318, 1199481548, 1232722574
#   , 1167574309, 1176881962, 1095439525, 1183590856, 1223828804, 1115323230
#   , 1134234070, 1102764170, 1156848781, 1015734135, 45719428, 1091394880
#   , 1213568727, 1040792640, 1090137756, 1161712947, 1093678867, 91665588
#   , 1168599753, 804513132,1198759633, 1102250485
if __name__ == '__main__':
  threads = []
  for index in range(0, len(question_id)):
    print('开始获取第%i个 ID：%i' % (index, question_id[index]))
    t = threading.Thread(target=zhihu.write_txt, args=({'question_id': question_id[index]},))
    t.setDaemon(True)
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  print("所有线程任务完成")
