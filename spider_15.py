#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

代理设置
对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，
对于大规模且频繁的请求，网站可能会直接登录验证，验证码，甚至直接把IP给封禁掉。+

那么为了防止这种情况的发生，我们就需要设置代理来解决这个问题，在 Requests
中需要用到 proxies 这个参数。
"""

import requests

# proxies = {
#     'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# }
#
# requests.get('https://www.taobao.com', proxies=proxies)


proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get('https://www.taobao.com', proxies=proxies)
