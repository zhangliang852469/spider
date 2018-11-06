#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" SSL 证书验证
Requests 提供了证书验证的功能，当发送 HTTP 请求的时候，它会检查 SSL 证书，
我们可以使用 verify 这个参数来控制是否检查此证书，其实如果不加的话默认是 True，
会自动验证。
"""

import requests

# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


# import logging
#
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))

print(response.status_code)



