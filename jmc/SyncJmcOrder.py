# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/9 9:57
# @File:     SyncJmcOrder.py
# @Software: PyCharm

"""
    重试京满仓订单同步服务

"""
import json

import requests

headers = {
    # 'Content-Type': 'application/json;charset=UTF-8',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

params = {
    "projectFlowId": "759156594503196672",
    "accessToken": "ba2ad053-318c-460f-bede-e34591512c3f"

}
url = 'http://gateway.vipmro.org/dxpAdmin/api/v1.0.0/executeRepeat'

print(json.dumps(params))

resp = requests.post(url=url, json=json.dumps(params), headers=headers)

print(resp.status_code)
print(resp.text)
