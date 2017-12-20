# -*- coding:utf-8 -*-

import urllib2


def send_request():
    # 请求报头是一个字典,添加到 Requset 对象的 headers 参数里
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }

    # 构建请求对象, 并包含自定义的请求报文信息
    requset = urllib2.Request("http://www.baidu.com/",headers=headers)

    # add_header 添加/修改一个请求报头
    requset.add_header("User-Agent", "hello world")
    requset.add_header("Connection", "keep-alive")

    # get_header 获取一个请求报头的值
    # 参数只能是第一个字母大写,后面必须是小写
    print requset.get_header("User-agent")
    print requset.get_header("Connection")

    # 发送请求,获取服务器的响应
    response = urllib2.urlopen(requset)

    # 获取响应的实际 url 地址,可以用获取重定向后的页面 url
    print response.geturl()

    # 获取响应状态码
    if response.getcode() == 200:
        print('发送成功')


if __name__ == '__main__':
    send_request()