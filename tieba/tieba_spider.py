# -*- coding:utf-8 -*-

import urllib
import urllib2


def send_request(s):
    # 接收参数
    keyword = {"kw": s}
    kw_str = urllib.urlencode(keyword)

    # 拼接 Url
    base_url = 'http://tieba.baidu.com/f?'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(base_url + kw_str, headers=headers)
    print request
    response = urllib2.urlopen(request)

    return response.read()


if __name__ == '__main__':
    s = raw_input("请输入你要搜索的贴吧")
    html = send_request(s)
    with open(s + '.html', 'w') as f:
        f.write(html)