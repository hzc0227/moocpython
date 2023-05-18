# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/15 17:07
# @File:     selenium_project.py
# @Software: PyCharm

"""
    登录部分，直接打开页面，点击登录就可以了
    打开订单列表页面 http://sleeve.talelin.com/#/statics/order/list
    抓取页面的数据,需要点击下一页,把数据存储到 mongodb

"""
import time

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree


class OrderInfoSpider(object):

    def __init__(self, ):
        # 获取webdriver
        self.driver = webdriver.Chrome()
        # 设置最大窗口
        self.driver.maximize_window()
        # mongo信息
        my_client = MongoClient(host='127.0.0.1', port=27017)
        my_db = my_client['python_study']
        self.mongo = my_db['selenium_order']

    # 登录网站，并返回登录标识
    def login(self, url):

        # 请求目标地址
        self.driver.get(url)

        # 等待登录页面加载完成,presence_of_element_located((By.CLASS_NAME, 'login-form'))方法的参数是元组类型！！！
        if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'login-form'))):
            # 寻找登录按钮并点击
            self.driver.find_element(By.XPATH, '//button[@class="submit-btn"]').click()
            # 判断是否登录成功(找到欢迎页面)
            if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="welcome"]'))):
                # 登录成功
                print("登录成功")
                # self.fetch_order_info('http://sleeve.talelin.com/#/statics/order/list')
                return True
            else:
                print("登录失败")
                return False
        print('登录失败')
        return False

    # 请求订单信息并解析存储
    def fetch_order_info(self, order_url, lock):
        print('开始抓取订单列表的订单信息')
        # 请求订单列表
        self.driver.get(order_url)
        # 有可能刚进入页面，并没有加载到数据，所以需要循环加载
        i = 1
        while True:
            # 出现页面模块判断订单数据加载成功
            if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'el-pager'))):
                # 解析页面数据
                # print(self.driver.page_source)
                # 解析订单页面(page_source就是网页源代码)
                self.parse_page_content(self=self, page_content=self.driver.page_source)
                # 如果到最后一页则结束(TODO 页面最后一页未爬取到)
                if self.driver.find_element(By.XPATH, '//button[@class="btn-next"]').get_attribute('disabled'):
                    break
                # if i == 281:
                    # break
                # 点击翻页
                self.driver.find_element(By.XPATH, '//button[@class="btn-next"]').click()
                i += 281

        self.driver.quit()

    @staticmethod
    def parse_page_content(self, page_content):
        print("开始解析数据")
        try:
            html = etree.HTML(page_content)
            # print(html)

            # 使用或标签
            # orders = html.xpath('//tbody/tr[@class="el-table__row el-table__row--striped" or @class="el-table__row"]')
            orders = html.xpath('//tbody/tr')
            order_infos = []
            for order in orders:
                main_info = order.xpath('./td/div/text()')
                status = ''.join(order.xpath('./td//div[@class="tags"]/span/text()'))
                order_info = {'id': int(main_info[0]),
                              'order_id': main_info[1],
                              'order_num': int(main_info[2]),
                              'order_price': float(main_info[3]),
                              'order_status': status
                              }
                order_infos.append(order_info)
                # print(order_info)
            print(order_infos)
            self.mongo.insert_many(order_infos)
            print("当前页数据解析完毕")
        except Exception as e:
            print('解析数据出错')
            print(e)


if __name__ == '__main__':
    order_spider = OrderInfoSpider()
    login_url = 'http://sleeve.talelin.com/#/login'
    login_flag = order_spider.login(url=login_url)
    fetch_order_url = 'http://sleeve.talelin.com/#/statics/order/list'
    # 如果登录成功才进行后续操作
    if login_flag:
        order_spider.fetch_order_info(order_url=fetch_order_url)
