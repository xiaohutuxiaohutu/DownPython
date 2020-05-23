#!/usr/bin/env python3
import zhihu
from multiprocessing import Process
import threading

question_id = [386250141, 384408291
               ]

if __name__ == '__main__':
  threads = []
  for index in range(0, len(question_id)):
    print('开始获取第%i个 ID：' % index)
    t = threading.Thread(target=zhihu.write_txt, args=({'question_id': question_id[index]},))
    t.setDaemon(True)
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  print("所有线程任务完成")
