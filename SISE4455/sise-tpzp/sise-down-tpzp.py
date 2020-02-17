#!/usr/bin/env python3
import datetime
import os

import requests.packages.urllib3.util.ssl_

import SISE4455

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
SISE4455.down_pic(SISE4455.DOWN_PATH_D_TP)
print("all over")
