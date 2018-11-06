#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""用 XPath 中的 text() 方法可以获取节点中的文本，我们接下来
尝试获取一下上文 li 节点中的文本"""

from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 逐层选取,先选取了 li 节点，又利用 / 选取了其直接子节点 a，然后再选取其文本
# result = html.xpath('//li[@class="item-0"]/a/text()')

# 用另一种方式 // 选取的结果
# result = html.xpath('//li[@class="item-0"]//text()')

# 获取属性 href
result = html.xpath('//li/a/@href')



print(result)