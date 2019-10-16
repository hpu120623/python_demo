# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/22 17:56

import re
import time
import json
import requests

from functools import reduce
from pprint import pprint
from urllib.parse import quote
from retrying import retry
from pyquery import PyQuery as pq
from scrapy.selector import Selector

from spiders.user_agent import FakeChromeUA


@retry(stop_max_attempt_number=3)
def test_request(request_url):
    # 配置请求头
    headers = {
        'User-Agent': FakeChromeUA.get_ua()
        # 'Cookie': 'acw_sc__v2=5da01528173d706c807e5b7816cebf30ee71ee3a'
    }

    response = requests.get(request_url, headers=headers, timeout=3)
    return response


def handle_json(response):
    result = json.loads(response.text)
    if result:
        pass


def handle_html(response):
    # 限定格式
    response.encoding = 'utf-8'
    # 利用scrapy.selector进行解析（css、xpath）
    selector = Selector(response)
    title = selector.css('title::text').extract_first()
    print(f'title: {title}')


if __name__ == '__main__':
    test_url = 'https://www.baidu.com'
    html = test_request(test_url)
    handle_html(html)
