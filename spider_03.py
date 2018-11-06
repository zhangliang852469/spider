#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 需要登录的页面页面抓取
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener

from urllib.error import URLError

username = 'username'
password = 'password'

url = 'http://www.zhihu.com'

# 1 实例化一个管理账户密码的表
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)

# 2 如果网站需要认证，在登录之前完成认证
auth_handler = HTTPBasicAuthHandler(p)

# 3 构造一个发送请求类
opener = build_opener(auth_handler)


try:
    # 4 打开连接
    result = open(url)
    # 5 获取内容
    html = result.read().decode('utf8')
    print(html)
except URLError as e:
    print(e.reason)





