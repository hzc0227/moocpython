# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/10 13:42
# @File:     Movie.py
# @Software: PyCharm

"""
    mooc爬虫15章实战
    url：http://movie.54php.cn/movie/?&p=2
    详情url：http://movie.54php.cn/movie/info?id=13996
    1. 获取数据
    2. 解析数据
    3. 多线程爬取
    4. 队列缓存
    5. 存入mongoDB
"""
import threading
import requests
from pymongo import MongoClient
from queue import Queue
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}


# 抓取页面信息类
class PageSpider(threading.Thread):

    def __init__(self, thread_name, page_queue, detail_queue):
        super(PageSpider, self).__init__()
        self.thread_name = thread_name
        self.detail_queue = detail_queue
        self.page_queue = page_queue

    # 重写run方法
    def run(self):
        print('======线程 {} 启动======'.format(self.thread_name))
        try:
            while not self.page_queue.empty():
                page_url = self.page_queue.get(block=False)
                resp = requests.get(url=page_url, headers=headers)
                if resp and 200 == resp.status_code:
                    self.parse_detail_url(resp.text)

        except Exception as e:
            print('======第 %s 线程出错%s======' % (self.thread_name, e))
        print('======线程 {} 结束======'.format(self.thread_name))

    def parse_detail_url(self, content):
        html = etree.HTML(content)
        detail_urls = html.xpath('//a[@class="thumbnail"]/@href')
        for detail_url in detail_urls:
            self.detail_queue.put(detail_url)


# 抓取详情页信息
class DetailSpider(threading.Thread):

    def __init__(self, thread_name, detail_queue, data_queue):
        super(DetailSpider, self).__init__()
        self.thread_name = thread_name
        self.detail_queue = detail_queue
        self.data_queue = data_queue

    def run(self):
        print('======线程 {} 启动======'.format(self.thread_name))
        try:
            while not self.detail_queue.empty():
                detail_url = self.detail_queue.get(block=False)
                resp = requests.get(url=detail_url, headers=headers)
                if resp and 200 == resp.status_code:
                    self.data_queue.put(resp.text)
        except Exception as e:
            print('======第 %s 线程出错%s======' % (self.thread_name, e))
        print('======线程 {} 结束======'.format(self.thread_name))


# 解析详情页数据并保存
class DataSpider(threading.Thread):
    def __init__(self, thread_name, data_queue, mongo_info, lock):
        super(DataSpider, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.mongo = mongo_info
        self.lock = lock

    def run(self):
        print('======线程 {} 启动======'.format(self.thread_name))
        try:
            while not self.data_queue.empty():
                data_info = self.data_queue.get(block=False)
                self.parse(data_info)
        except Exception as e:
            print('======第 %s 线程出错%s======' % (self.thread_name, e))
        print('======线程 {} 结束======'.format(self.thread_name))

    def parse(self, data):
        html = etree.HTML(data)
        movie_info = {
            'title': self._join_list(html.xpath('//div[@class="page-header"]/h1/text()')),
            'update_time': self._join_list(html.xpath('//div[@class="panel-body"]/p[1]/text()')),
            'type': self._join_list(html.xpath('//div[@class="panel-body"]/p[2]/text()')),
            'starring': self._join_list(html.xpath('//div[@class="panel-body"]/p[3]/text()')),
            'description': self._join_list(html.xpath('//div[@class="panel-body"]/p[4]/text()')),
            'img_url': self._join_list(html.xpath('//img[@class="img-thumbnail"]/@src')),
            'download_url': self._join_list(html.xpath('//div[@class="panel-body"]/p[5]/text()')),
            'source_url': self._join_list(html.xpath('//div[@class="panel-body"]/p[6]/a/text()'))
        }
        print(movie_info)
        # 写入数据库需要加锁
        # self.lock.acquire()
        # self.mongo.insert_one(movie_info)
        # self.lock.release()
        with self.lock:
            self.mongo.insert_one(movie_info)

    def _join_list(self, item):
        return ''.join(item)


def main():
    page_queue = Queue()  # 页面url队列
    detail_queue = Queue()  # 详情页url队列
    data_queue = Queue()  # 数据队列
    for page in range(1, 21):
        page_url = 'http://movie.54php.cn/movie/?&p={}'.format(page)
        page_queue.put(page_url)
    print(page_queue.qsize())

    # 列表页
    page_spider_threadname_list = ["列表页采集线程1号", "列表页采集线程2号", "列表页采集线程3号"]
    page_spider_list = []
    for thread_name in page_spider_threadname_list:
        thread = PageSpider(thread_name, page_queue, detail_queue)
        # 启动线程
        thread.start()
        page_spider_list.append(thread)

    print(detail_queue.qsize())

    # 查看当前page_queue里面数据状态
    while not page_queue.empty():
        # 有数据的时候什么都不干
        pass
    # 释放资源
    for thread in page_spider_list:
        if thread.is_alive():
            thread.join()

    # 详情页
    detail_spider_threadname_list = ["电影数据采集线程1号", "电影数据采集线程2号", "电影数据采集线程3号", "电影数据采集线程4号", "电影数据采集线程5号"]
    detail_spider_list = []
    for thread_name in detail_spider_threadname_list:
        thread = DetailSpider(thread_name, detail_queue, data_queue)
        # 启动线程
        thread.start()
        detail_spider_list.append(thread)

    # 查看当前detail_queue里面数据状态
    while not detail_queue.empty():
        # 有数据的时候什么都不干
        pass

    # 释放资源
    for thread in detail_spider_list:
        if thread.is_alive():
            thread.join()

    # 数据
    data_spider_threadname_list = ["电影数据采集线程1号", "电影数据采集线程2号", "电影数据采集线程3号"]
    data_spider_list = []
    mongo_clint = MongoClient('127.0.0.1', 27017)
    mongo_db = mongo_clint['python_study']
    mongo_collection = mongo_db['mooc_movie']
    lock = threading.Lock()

    for thread_name in data_spider_threadname_list:
        thread = DataSpider(thread_name, data_queue, mongo_collection, lock)
        # 启动线程
        thread.start()
        data_spider_list.append(thread)

    # 查看当前data_queue里面数据状态
    while not data_queue.empty():
        # 有数据的时候什么都不干
        pass

    # 释放资源
    for thread in data_spider_list:
        if thread.is_alive():
            thread.join()


if __name__ == '__main__':
    main()
