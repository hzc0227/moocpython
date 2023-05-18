# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/8 9:40
# @File:     fetch_ip_pool.py
# @Software: PyCharm

"""
    爬取快代理免费代理ip地址，构建自己的ip池
    链接：https://www.kuaidaili.com/free/inha/1/
"""

import requests

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


class BuildIpPool:

    # 获取ip池
    @staticmethod
    def fetch_ips():
        # 暂时只取10页的ip地址
        ip_data = []
        for page in range(1, 11):
            url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            resp = requests.get(url=url, headers=headers)
            if resp and 200 == resp.status_code and resp.text:
                # print(resp.text)
                soup = BeautifulSoup(resp.text, "html.parser")
                # print(soup)
                tags = soup.select("#list > table > tbody > tr")
                for tag in tags:
                    ip_info = tag.find_all("td", limit=2)
                    ip = ip_info[0].text
                    port = ip_info[1].text
                    ip_data.append({
                        'HTTP': str(ip) + ':' + str(port)
                    })
            # print(ip_data)
            # break
        return ip_data

    # 筛选出大概率可用的ip
    @staticmethod
    def filter_ip(data):
        print('共获取的ip数量', len(data))
        # 过滤掉不可用ip
        available_ip = []

        for ip in data:
            try:
                resp = requests.get('https://www.baidu.com/', headers=headers, proxies=ip, timeout=0.1)
                if resp and 200 == resp.status_code:
                    available_ip.append(ip)
            except Exception as e:
                print(e)
        print("共获取到的可用ip数量", len(available_ip))
        return available_ip

    # 保存可用ip到文件
    @staticmethod
    def save(data):
        with open('ips.txt', 'w') as file:
            for ip in data:
                file.write(str(ip) + '\n')
        # file.close()


if __name__ == '__main__':
    ip_datas = BuildIpPool.fetch_ips()
    available_ips = BuildIpPool.filter_ip(ip_datas)
    BuildIpPool.save(available_ips)

