#!/usr/bin/env python3
import common
import os
from common import ProxyIp

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'cookie': 'fvlid=1597625585953zQdtJ1EJ4L; sessionip=61.144.97.195; sessionid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; autoid=ac8e7bc62f1d44610e0ccf927310f83b; area=440113; ahpau=1; __ah_uuid_ng=c_E554438A-793F-4510-A2D6-7E3FC7DEA18E; sessionuid=E554438A-793F-4510-A2D6-7E3FC7DEA18E%7C%7C2020-08-17+08%3A53%3A06.504%7C%7Cwww.baidu.com; papopclub=7EF4B085C9B313B48E3E27DB78354755; sessionvid=D0BF9713-8187-4530-85A9-F14F8034817D; pepopclub=C4F7FB8E90D00844FE5A7C4CA0D060E3; v_no=2; visit_info_ad=E554438A-793F-4510-A2D6-7E3FC7DEA18E||D0BF9713-8187-4530-85A9-F14F8034817D||-1||-1||2; ahpvno=14; ref=www.baidu.com%7C0%7C0%7C0%7C2020-08-17+12%3A27%3A57.446%7C2020-08-17+08%3A53%3A06.504; pvidchain=102410,3274715'

}
proxy_ip = ProxyIp.ProxyIp().get_random_proxy_ip()
