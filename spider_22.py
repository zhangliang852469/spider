#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree

""" 通过子点来查找父节点"""
html = etree.parse('./test.html', etree.HTMLParser())

# 例如： href 是 link4.html 的 a 节点，然后再获取其父节点，
# 然后再获取其 class 属性

# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link3.html"]/../@class')

# 通过 parent:: 来获取父节点
# result = html.xpath('//a[@href="link3.html"]/parent::*/@class')

# 用 @ 符号进行属性过滤
result = html.xpath('//li[@class="item-0"]')
print(result)