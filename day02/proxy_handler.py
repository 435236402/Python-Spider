# -*- coding:utf-8 -*-

import urllib2


def send_request():
    # 1.免费代理(不需要账号密码就能直接使用)
    # proxy = {"http":"127.27.218.32:16816"}

    # 2.验证代理(需要账户密码才能使用)
    proxy = {"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"}

    # 3.空代理 (不使用代理,使用本机的 ip发送请求)
    # proxy = {}

    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    response = opener.open("http://www.httpbin.org/ip")

    # install_opener 将指定的 opener 对象修改成全局 opener
    # 好处是不管在程序的任何地方,使用 urllib2.urlopen()发送的请求,都附带opener 功能
    # 可选,根据请求使用
    urllib2.install_opener(opener)
    print response.read()


def send_request2():
    # 因为 install_opener 的作用,在程序的任何地方发送请求,都会附带代理
    response = urllib2.urlopen("http://www.httpbin.org/ip")
    print response.read()

if __name__ == '__main__':
    send_request()
    # 第一函数没有调用,就不install_opener 就不会生效
    send_request2()