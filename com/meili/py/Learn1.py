#!/usr/bin/evn python3
# -*- coding:utf-8 -*-

import requests

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
print('code =', r.status_code)
print('encode =', r.encoding)
print(r.text)
