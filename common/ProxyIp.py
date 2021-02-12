import os
import sys
# from urlparse import urlsplit
from urllib.request import Request
from urllib.request import urlopen
import logging
from bs4 import BeautifulSoup

from common import DoConfig
import random
import common

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
project_dir = common.get_project_dir()


class ProxyIp:
    __instance = None
    __init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # logger.info(' proxyip not int ,start init')
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # logger.info(' proxyip has init')
            return cls.__instance

    def __init__(self, config_path=project_dir + 'common' + os.sep + 'config.ini'):
        if not ProxyIp.__init_flag:
            # logger.info('init proxyip;config_path: ' + config_path)
            config = DoConfig.DoConfig(config_path)
            common_dict = config.get_dict('common')
            self.proxy_url = common_dict.get('proxy_url')
            self.ip_list = []
            self.get_ip_list()
            ProxyIp.__init_flag = True

    def get_ip_list(self):
        # logger.info(self.proxy_url)
        request = Request(self.proxy_url, headers=common.header)
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
                    request = Request(proxy_temp, headers=common.header)
                    response = urlopen(request).read()
                except Exception as e:
                    self.ip_list.remove(ip)
                    continue
        return self.ip_list

    def get_random_proxy_ip(self):
        if len(self.ip_list) == 0:
            self.get_ip_list()
        random_ip = 'http://' + random.choice(self.ip_list)
        return {'http:': random_ip}


if __name__ == '__main__':
    proxy_ip = ProxyIp()
    print(proxy_ip.ip_list)

    ip = ProxyIp()
    print(ip.ip_list)
