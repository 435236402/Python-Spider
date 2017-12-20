# -*- coding:utf-8 -*-

import urllib2


def send_request():

    url = "http://www.renren.com/410043129/profile"

    headers = {
        "Cookie": "anonymid=j7wsz80ibwp8x3; _r01_=1; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; depovince=BJ; jebecookies=f2692c97-c0d9-477b-a648-6fccd157e1a3|||||; JSESSIONID=abc3Hww5VNL-qecuUDIbw; ick_login=1a433c78-7419-40a7-90f4-d89c28d92353; p=289f8b08af600106b2d9fbe09c3e203a9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20171214/1615/main_CqLX_b0920000a566195a.jpg; t=23d9fc926d60fbce88d07abd4e4bb5879; societyguester=23d9fc926d60fbce88d07abd4e4bb5879; id=327550029; xnsid=9d88e636; loginfrom=syshome; ch_id=10016",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    with open("renren.html", "w") as f:
        f.write(response.read())

if __name__ == '__main__':
    send_request()