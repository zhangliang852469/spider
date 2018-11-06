#!/usr/bin/env python3
# -*- coding:utf-8 -*-
""" 爬取猫眼电影前100的电影信息 http://maoyan.com/board/4

之单页爬取"""

"""分析： url的变化 URL 变成了：http://maoyan.com/board/4?offset=10，
相比之前的URL多了一个参数，那就是 offset=10，而目前显示的结果是排行 11-20 名的电影，
初步推断这是一个偏移量的参数，我们再点击下一页，发现页面的 URL 
变成了：http://maoyan.com/board/4?offset=20，参数 offset 变成了 20，
而显示的结果是排行 21-30 的电影
"""


import requests

import re

import json


# 获取网页链接响应
def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# 提取下载的页面信息
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
                         re.S

    )
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }

# 写入文件
def write_to_json(content):
    path = 'E:\virtualenv\spider\content.txt'
    with open(path, 'a') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False).encode('utf8'))



# 调用方法
def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_json(item)