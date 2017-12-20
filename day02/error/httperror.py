# -*- coding:utf-8 -*-

import urllib2


def send_request():
    request = urllib2.Request("http://www.itcast.cn/helloworld.html")

    try:
        response = urllib2.urlopen(request)
    except Exception, err:
        print err

        # 显示HTTPError 异常的状态码
        print err.code
    print "aaa"


if __name__ == '__main__':
    send_request()