# -*- coding:utf-8 -*-

from selenium import webdriver


def douban_login(username, password):
    driver = webdriver.PhantomJS(executable_path="/Users/user/phantomjs-2.1.1-macosx/bin/phantomjs")
    driver.get("http://www.douban.com/")

    # 输入用户名跟密码
    driver.find_element_by_name('form_email').send_keys(username)
    driver.find_element_by_name('form_password').send_keys(password)

    # 获取验证码图片
    driver.save_screenshot('douban.png')
    captcha = raw_input("输入验证码:")

    # 添加验证码
    driver.find_element_by_id("captcha_field").send_keys(captcha.decode("utf-8"))
    # 点击提交
    driver.find_element_by_class_name("bn-submit").click()
    # 获取登录后的界面
    driver.save_screenshot("douban.png")

    with open('douban.html','w') as f:
        f.write(driver.page_source.encode('utf-8'))

if __name__ == '__main__':
    username = u'mr.mao.tony@gmail.com'
    password = u'ALARMCHIME'
    douban_login(username, password)
