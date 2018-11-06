#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 练习1：爬取简书网站首页文章的标题和文章的链接"""


from urllib import request
from bs4 import BeautifulSoup # 可以从HTML或XML文件中提取结构化数据的python库


# 构造头部文件，模拟浏览器访问
url = "http://www.jianshu.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf8') # 打开Url,获取HttpResponse返回对象并读取其ResposneBody


# 将获取到的内容转换成BeautifulSoup格式，滨江html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')
# 以格式化的形式打印html
# print(soup.prettify)

titles = soup.find_all('a', 'title')# 查找所有‘a’标签中class=‘title’的语句
"""
# 打印查找到的每一个a标签的string和文章链接
    for title in titles:
        print(title.string)
        print("http://www.jianshu.com" + title.get('href'))  
"""

# open() 函数是读写文件的，with语句会自动关闭打开的文件

with open(r'F:\spider\test\articles_spider_01.txt', 'x') as file: # 新建并打开
    for title in titles:
        file.write(title.string+'\n')
        file.write('http://www.jianshu.com' + title.get('href') + '\n\n')
