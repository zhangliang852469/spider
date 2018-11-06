#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" requests 的高级用法"""

import requests

files = {'file': open('favicon', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)