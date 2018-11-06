#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
处理Cookies

Cookies 的处理就需要 Cookies 相关的 Handler 了

"""

import http.cookiejar, urllib.request

# 1 声明cookie对象（也就是实例化一个cookie）
cookie = http.cookiejar.CookieJar()
# 2 构建hander
handler = urllib.request.HTTPCookieProcessor(cookie)
# 3 构建处理函数
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)

