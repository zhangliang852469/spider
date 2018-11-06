#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())

# # 匹配所有节点
# # result = html.xpath('//*')

# 匹配li 节点
#result = html.xpath('//li')

# 选取li节点下的直接节点a
# result = html.xpath('//li/a')

# 获取 ul 节点下的所有子孙 a 节点

result = html.xpath('//ul//a')

print(result)

# print(result[0])

