#!/usr/bin/env python3
import zhihu
from multiprocessing import Process
import threading
question_id = [285072479, 278164241, 368176418
  , 363020928, 282840187, 316954079, 28483870, 266626906, 980882475, 49513201, 302912986
  , 340057767, 376376914, 1187898738, 383189925, 90210016, 46936305, 68285001, 852276684
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


