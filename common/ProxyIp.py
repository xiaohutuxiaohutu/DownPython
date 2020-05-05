import os
import sys
# from urlparse import urlsplit
from urllib.request import Request
from urllib.request import urlopen

from bs4 import BeautifulSoup

from common import DoConfig
import random
import json


class ProxyIp():
  def __init__(self, ip_list=[], random_ip=''):

    self.ip_list = ip_list
    self.random_ip = random_ip
    # self.header = {}
    config = DoConfig.DoConfig(sys.path[1] + os.sep + 'common' + os.sep + 'config.ini')
    common_dict = config.get_dict('common')
    self.proxy_url = common_dict.get('proxy_url')
    self.header = json.loads(common_dict.get('header'))

  def get_ip_list(self):
    print(sys.path[1])
    request = Request(self.proxy_url, headers=self.header)
    response = urlopen(request)
    obj = BeautifulSoup(response, 'lxml')
    # ip_text = obj.findAll('tr', {'class': 'odd'})
    ip_text = obj.findAll('tr')
    if len(ip_text) > 0:
      for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        if len(ip_tag) > 0:
          ip_port = ip_tag[0].get_text() + ':' + ip_tag[1].get_text()
          self.ip_list.append(ip_port)
    # 检测IP是否可用
    # print(ip_list)
    if len(self.ip_list) > 0:
      for ip in self.ip_list:
        try:
          proxy_host = 'https://' + ip
          proxy_temp = {"https:": proxy_host}
          # res = urllib.urlopen(proxy_host, proxies=proxy_temp).read()
          request = Request(proxy_temp, headers=self.header)
          response = urlopen(request).read()
        except Exception as e:
          self.ip_list.remove(ip)
          continue
    return self.ip_list

  def get_random_proxy_ip(self):
    if len(self.ip_list) == 0:
      self.get_ip_list()
    random_ip = 'http://' + random.choice(self.ip_list)
    proxy_ip = {'http:': random_ip}
    return proxy_ip


if __name__ == '__main__':
  proxy_ip = ProxyIp()

  print(proxy_ip.get_ip_list())
  header = proxy_ip.header
  print(header)
  print(type(header))
