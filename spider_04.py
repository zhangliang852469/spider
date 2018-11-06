#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 代理

在做爬虫的时候免不了要使用代理
"""

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 构建一个代理
proxy_handler = ProxyHandler(
    {
        'http': 'http://127.0.0.1:8000',
        'https': 'https://127.0.0.1:9743'
    },

)

opener = build_opener(proxy_handler)

try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf8'))
except URLError as e:
    print(e.reason)
