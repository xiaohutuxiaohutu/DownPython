import logging

import requests
from bs4 import BeautifulSoup

import common
from common import ProxyIp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# url 一样只初始化一次
class BeautySoupTool:

    def __init__(self, url, proxy_ip=ProxyIp.ProxyIp().get_random_proxy_ip(), encoding='utf-8'):
        # logger.info('BeautySoupTool init')
        html = requests.get(url, headers=common.header, proxies=proxy_ip)
        html.encoding = encoding
        self.beautySoup = BeautifulSoup(html.text, 'lxml')
        self.title = self.beautySoup.title.string
        # if self.title is None:
        #     self.title = self.beautySoup.text
        #
        # logger.info('soup init success')

    def get_title(self):
        strip = common.replace_sub(self.title).strip()
        return strip

# if __name__ == '__main__':
# proxy = ProxyIp.ProxyIp()
# random_ip = proxy.get_random_proxy_ip()
# soup_tool = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=373943&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest')
# print(soup_tool.get_title())
# soup_tool2 = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=374392&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest', random_ip)
# print(soup_tool2.beautySoup.title.string)
# soup_tool1 = BeautySoupTool('https://f.w24.rocks/viewthread.php?tid=373943&extra=page%3D1%26amp%3Borderby%3Ddateline%26amp%3Bfilter%3Ddigest', random_ip)
# print(soup_tool1.beautySoup.title.string)
