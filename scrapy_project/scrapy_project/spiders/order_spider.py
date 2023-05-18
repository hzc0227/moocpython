import scrapy
from lxml import etree


class OrderSpiderSpider(scrapy.Spider):
    name = 'order_spider'  # spider的名称，注：name在spiders目录中，不能重复
    allowed_domains = ['http://digital.talelin.com/']  # 允许爬取url的域名(需要登录后才能访问)
    start_urls = ['http://digital.talelin.com/v1/order/page?page=1&count=10']  # 起始url，项目启动首先访问的地址，如果是分页，则可以根据情况自定义修改

    # allowed_domains = ['http://sleeve.talelin.com/']  # 允许爬取url的域名(需要登录后才能访问)
    # start_urls = ['http://sleeve.talelin.com/#/statics/order/list']  # 起始url，项目启动首先访问的地址，如果是分页，则可以根据情况自定义修改



    def parse(self, response):
        print(response.headers)
        # 此处的response已经是解析过的资源了
        response = etree.HTML(response)
        orders = response.xpath('//tbody/tr')
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
            print('当前位于 order_spider.py 模块')
            print(order_infos)
            # 判断是否到最后一页，不到则继续翻页
            if response.xpath('//button[@class="btn-next" and not contain(@disabled,"disabled")]'):
                now_page = int(response.xpath['//ui[@class="el-pager"]/li[@class="number active"]'].extract_first())
                next_url = 'http://digital.talelin.com/v1/order/page?page=%d&count=10' % (now_page + 1)
                # 请求下一页
                # 注意 callback属性只需要方法名即可，不需要带参数
                yield scrapy.Request(url=next_url, callback=self.parse)

