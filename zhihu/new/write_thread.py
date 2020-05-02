#!/usr/bin/env python3
import zhihu
from multiprocessing import Process
import threading

question_id = [278164241, 1191256779,]

if __name__ == '__main__':
  for index in range(0, len(question_id)):
    t = threading.Thread(target=zhihu.write_txt, args=({'question_id': question_id[index]},))
    t.setDaemon(True)
    t.start()
  t.join()
  # print(question_id[index])
  # p = Process(target=zhihu.write_txt, args=({'question_id': question_id[index]},))
  # p.start()
  # p.join()
  # 执行下载逻辑
