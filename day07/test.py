# -*- coding:utf-8 -*-

# 导入 webdricer
from selenium import webdriver
# 调用指定位置的phantomJ的浏览器创建浏览器对象
driver = webdriver.PhantomJS(executable_path="/Users/user/phantomjs-2.1.1-macosx/bin/phantomjs")

# get方法会一直等到页面被完全加载，然后才会继续程序
driver.get("http://www.baidu.com/")

# 获取当前页面的网页源码（Unicode字符串）
html = driver.page_source.encode("uft-8")

# 打印数据内容
print html

# 打印页面标题 '百度一下，你就知道'
print driver.title

# 生成当前页面快照并保存
driver.save_screenshot('baidu.png')

# 点击指定name属性的a标签
driver.find_element_by_name('tj_trnews').click()

# 获取当前标签页的截图
driver.save_screenshot("baidu.png")



