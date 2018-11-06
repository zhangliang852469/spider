#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" XPath"""

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''


# 利用etree.HTML 方法将text的内容转化成为html代码
html = etree.HTML(text)
# 利用etree.tostring 将html代码补全，成为一个完整的html代码，代码为bytes类型
result = etree.tostring(html)
# 将byte类型的html 转化成为utf8格式
print(result.decode('utf8'))
