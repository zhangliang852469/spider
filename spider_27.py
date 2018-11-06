#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 节点轴选择
XPath 提供了很多节点轴选择方法，英文叫做 XPath Axes，包括获取子元素、兄弟元素、
父元素、祖先元素等等，在一定情况下使用它可以方便地完成节点的选择"""

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)

result = html.xpath('//li[1]/ancestor::*')
print(result)

result = html.xpath('//li[1]/ancestor::div')
print(result)

result = html.xpath('//li[1]/attribute::*')
print(result)

result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)

result = html.xpath('//li[1]/descendant::span')
print(result)

result = html.xpath('//li[1]/following::*[2]')
print(result)

result = html.xpath('//li[1]/following-sibling::*')
print(result)



















