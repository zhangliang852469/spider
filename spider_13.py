#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 维持同一个会话， get post """

import requests

s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")

r = s.get('http://httpbin.org/cookies')

print(r.text)
