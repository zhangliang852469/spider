#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
第三方库：requests
"""
import requests

r = requests.get('http://www.baidu.com/')

print(type(r))
print(r.status_code)
print(type(r.text))
print(r.cookies)
print(r.text)



m = requests.get('http://httpbin.org/get')
print(r.text)


