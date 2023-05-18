# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/16 20:36
# @File:     main.py
# @Software: PyCharm

from scrapy import cmdline

# 在scrapy项目里面，为了运行scrapy的项目
# cmdline.execute
# scrapy crawl 项目的名称(spider名称)
cmdline.execute("scrapy crawl order_spider".split())

