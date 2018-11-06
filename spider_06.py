#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" c处理cookie 生成文件"""


import urllib.request, http.cookiejar

filename = 'cookie.txt' #生成的文件名

cookie = http.cookiejar.MozillaCookieJar(filename) # 实例化一个cookie

handler = urllib.request.HTTPCookieProcessor(cookie) # 生成处理handler

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)
