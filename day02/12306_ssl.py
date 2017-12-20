# -*- coding:utf-8 -*-

import urllib2

# Python 处理SSL的模块
import ssl

# 可以忽略网站的未经认证的 SSl 证书
context = ssl._create_unverified_context()


def main():
    url = "https://www.12306.cn/mormhweb/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, context=context)
    print response.read()


if __name__ == '__main__':
    main()
