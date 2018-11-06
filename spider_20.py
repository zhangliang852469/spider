#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree

# 直接读取文本文件进行解析
html = etree.parse('./test.html', etree.HTMLParser())

result = etree.tostring(html)

print(result.decode('utf8'))

