# -*- coding: utf-8 -*-

import sys

sys.path.append(r"C:\workspace\GitHub\DownPython")

import common
proxyipurl = 'http://www.xicidaili.com/'

ip_list = common.get_ip_list(proxyipurl)
proxy_ip = common.get_random_ip(ip_list)
print(proxy_ip)
