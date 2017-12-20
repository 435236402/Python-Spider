# -*- coding:utf-8 -*-

import urllib2


def main():

    # 1.使用特定功能的处理器类,创建处理器对象
    # HTTPHandler(debuglevel = 1)表示在发送请求后,同时打印收发包信息
    http_handler = urllib2.HTTPHandler(debuglevel=1)

    # 2.使用这些处理器,并创建自定义的 opener 对象
    opener =urllib2.build_opener(http_handler)

    # 3.使用 opener 对象发送请求即可
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib2.Request("http://www.baidu.com/", headers=headers)
    response = opener.open(request)

if __name__ == '__main__':
    main()