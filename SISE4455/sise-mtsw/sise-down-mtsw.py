#!/usr/bin/env python3

import requests.packages.urllib3.util.ssl_

import SISE4455

down_path = 'D:/图片/四色AV/美腿丝袜'
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
params = {
    'down_path': down_path
}
SISE4455.down_pic(params)
