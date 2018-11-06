#!/usr/bin/env python3
# -*- coding:utf-8 -*-
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
print(soup.title.name)

# 获取属性  每个节点可能有多个属性，比如 id，class 等等，我们选择到这个节点元素之后，可以调用 attrs 获取所有属性。
print(soup.p.attrs)
print(soup.p.attrs['name'])

print(soup.p['name'])
print(soup.p['class'])







