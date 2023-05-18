# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/14 13:49
# @File:     webdriver_test.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By


import time

test_webdriver = webdriver.Chrome()
test_webdriver.maximize_window
# 访问百度
test_webdriver.get('https://www.baidu.com/')
# 输入python
test_webdriver.find_element(By.ID, 'kw').send_keys('python')
# 点击百度一下
test_webdriver.find_element(By.ID, 'su').click()
print("首次打开搜索结果页面")
time.sleep(3)
print("刷新当前页面")
test_webdriver.refresh()
time.sleep(3)
print("页面回退")
test_webdriver.back()
time.sleep(3)
print("页面前进")
test_webdriver.forward()
time.sleep(2)
# 退出
test_webdriver.quit()
