#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""BeautifulSoup 的使用"""


# 基本使用
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

from bs4 import BeautifulSoup
# 初始化html字符串以lxml， 然后赋值给soup
soup = BeautifulSoup(html, 'lxml')
# 调用soup的方法解析soup， 使用prettify来进行标准格式输出
print(soup.prettify())
# 调用soup.title.string来输出html中title中的文本内容
print(soup.title.string)

