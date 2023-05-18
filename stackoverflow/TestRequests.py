# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/4/19 20:12
# @File:     TestRequests.py
# @Software: PyCharm


import requests_mock
import requests as req



def my_test():
    auth_headers = {"Authorization": "Bearer ..."}
    query_params = "?since=0&until=1"
    expected_url = f"mock://some.url/media{query_params}"  # no mock address
    with requests_mock.Mocker() as mocker:
        mocker.get(
            expected_url,
            headers=auth_headers,
            text="media_found",
        )
        response = make_request()
        assert response.text == "media_found"
#         # assert mocker.last_request.params == query_params


def make_request():
    url = "mock://some.url/media"
    headers = {"Authorization": "Bearer ..."}
    params = {"since": 0, "until": 1}
    req.get(url, params=params, headers=headers, timeout=30)

