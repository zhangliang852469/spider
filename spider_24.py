#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree
"""属性多值匹配: 有时候某些节点的某个属性可能有多个值  """

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, "li")]/a/text()')

print(result)