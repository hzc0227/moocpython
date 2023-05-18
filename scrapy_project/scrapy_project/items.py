# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 本次实践要抓取的订单信息声明
    id = scrapy.Field()  # id
    order_id = scrapy.Field()  # 订单号
    order_num = scrapy.Field()  # 单品数量
    order_price = scrapy.Field()  # 总价格
    order_status = scrapy.Field()  # 状态

