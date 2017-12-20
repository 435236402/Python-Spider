# -*- coding:utf-8 -*-

import urllib2
import urllib
import json


def send_request(text):
    """
    爬取百度翻译的翻译功能
    :param text:
    :return:
    """
    url = "http://fanyi.baidu.com/v2transapi"
    # form 表单数据
    form = {
        "from": "auto",
        "to": "auto",
        "query": text,
        "simple_means_flag": "3"
    }
    data = urllib.urlencode(form)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, data, headers)

    response = urllib2.urlopen(request)

    # 响应是 json字符串
    json_str = response.read()
    # 将 json字符串转为 python数据类型
    json_obj = json.loads(json_str)

    print json_obj["trans_result"]["data"][0]["dst"]


if __name__ == '__main__':
    text = raw_input("请输入你要翻译的内容")
    send_request(text)