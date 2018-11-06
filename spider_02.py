#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 爬取知乎网站的美女图片链接，并保存到本地"""

from urllib import request
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.zhihu.com/question/22918070'  # 需要爬取的页面
# 模拟浏览器头部
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# 访问页面
page = request.Request(url, headers=headers)

html_info = request.urlopen(page).read().decode('utf8')  # 获取爬取的页面并将以utf8的格式保存

soup = BeautifulSoup(html_info, 'html.parser')  # 利用bs4提取结构化数据，保存在soup

# 利用Beatiful Soup结合正则提取包含所有图片的链接（img标签中, class=**, 以.jpg结尾的链接）的语句
links = soup.find_all('img', 'origin_image zh-lightbox-thumb', src=re.compile(r'.jpg$'))
print(links)


# 设置保存的路径
path = r'F:\spider\test\images'
for link in links:
    print(link.attrs['src'])
    # 保存链接并命名，time.time()返回当前时间搓防止命名冲突
    request.urlretrieve(link.attrs['src'], path+'\%s.jpg' % time.time())
    # 使用request.urlretrieve直接将所有远程链接数据下载到本地

