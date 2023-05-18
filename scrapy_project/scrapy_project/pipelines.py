# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


# 注意在settings中开启
class ScrapyProjectPipeline:

    def __int__(self):
        my_client = MongoClient('mongodb://127.0.0.1:27017')
        my_db = my_client['study_python']
        self.mongo = my_db['scrapy_order']

    def process_item(self, item, spider):
        datas = dict(item)
        print('当前位于 pipelines.py 模块')
        print(datas)
        # self.mongo.insert_many(datas)
        return item
