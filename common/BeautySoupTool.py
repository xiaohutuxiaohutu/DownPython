import logging

import requests
from bs4 import BeautifulSoup

import common
from common import ProxyIp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# url 一样只初始化一次
class BeautySoupTool:
    def __init__(self, url, proxy_ip=ProxyIp.ProxyIp().get_random_proxy_ip(), encoding='utf-8', timeout=10):
        try:
            html = requests.get(url, headers=common.header, proxies=proxy_ip, timeout=timeout)
            self.status_code = html.status_code
            html.encoding = encoding
            self.beautySoup = BeautifulSoup(html.text, 'lxml')
            self.title = common.replace_sub(self.beautySoup.title.string).strip()
            # if html.status_code == 200:
            #     self.title = common.replace_sub(self.beautySoup.title.string).strip()
            # else:
            #     self.title = None
            #     logger.info('状态码错误：%i' % html.status_code)
        except Exception as e:
            self.title = self.status_code
            logger.info("BeautySoupTool 请求失败，{},{}".format(common.get_datetime('%Y/%m/%d %H:%M'), e))

# if __name__ == '__main__':
# proxy = ProxyIp.ProxyIp()
# random_ip = proxy.get_random_proxy_ip()
# soup_tool = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=373943&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest')
# print(soup_tool.get_title())
# soup_tool2 = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=374392&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest', random_ip)
# print(soup_tool2.beautySoup.title.string)
# soup_tool1 = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=373943&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest', random_ip)
# print(soup_tool1.beautySoup.title.string)
