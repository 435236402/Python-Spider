# -*- coding:utf-8 -*-

# urllib不能构建请求对象,也就是不能添加请求报头,但是有 urlencode()
import urllib
# urllib2 是可以构建请求对象,但是没有 urlencode()
import urllib2


def send_request(s):
    # 处理查询的字符串 转为 url 编码
    keyword = {"wd": s}
    kw_str = urllib.urlencode(keyword)

    # 固定 url 地址
    base_url = 'http://www.baidu.com/s?'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 将查询的字符串固定 url 地址拼接,发送请求
    request = urllib2.Request(base_url + kw_str, headers=headers)
    response = urllib2.urlopen(request)

    # response.read() 取决网页的 charset
    return response.read()


if __name__ == '__main__':
    s = raw_input("请输入需要查询的关键字")
    html = send_request(s)

    with open("baidu.html", "w") as f:
        f.write(html)
