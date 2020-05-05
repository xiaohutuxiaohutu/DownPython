# import common
# import porn
# from testclass import DownPic
# import testclass
# down = DownPic('https://www.kuaidaili.com/free/intr/', 1, 5, 'Pictures/Camera Roll/PORN/自拍达人原创申请-JH')
from testclass import DownPic
from common import ProxyIp
# down = DownPic.DownPic( 1, 5, 'Pictures/Camera Roll/PORN/自拍达人原创申请-JH')

ip = ProxyIp.ProxyIp()
print(ip.get_ip_list())
print(ip.get_random_proxy_ip())
#