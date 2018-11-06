#!/usr/bin/env python3
# -*- coding:utf-8 -*-
""" 多属性匹配 另外我们可能还遇到一种情况，我们可能需要根据多个属性才能确定一个节点，
这是就需要同时匹配多个属性才可以，那么这里可以使用运算符 and 来连接"""
from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')

print(result)