# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/22 17:56
import json
import re
import hashlib
from functools import reduce
from pprint import pprint
from urllib.parse import quote

import requests
from retrying import retry
from pyquery import PyQuery as pq
from scrapy.selector import Selector


@retry(stop_max_attempt_number=3)
def request_url(request_url):
    # 配置请求头
    # print(get_auth_sign(request_url))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
        # 'Cookie': '_hc.v=1234',
        # 'Referer': 'http://so.eastmoney.com'
        # 'x-sign': get_auth_sign(request_url)
    }
    # 配置代理
    proxies = {
        'https': 'http://103.46.128.41:57345'
    }
    response = requests.get(request_url, headers=headers)
    # print(response.url)
    # print(response.text)

    # 调用Scrapy中选择器进行解析
    selector = Selector(response)
    # 示例如下:
    # address = selector.css('div.more-class p').xpath('string(.)').extract_first()
    # 获取所有分类
    # print(selector.css('.brief-info .address::text').extract()[-1].strip())
    # li_list = selector.css('.table:nth-child(4) tr')[3:]
    li_list = selector.xpath('//table/')
    print(li_list)
    # # li_dict = {}
    for li in li_list:
    #     # li_id = li.css('span.title::text').extract_first()
    #     # li_name = li.css('::text').extract()[-1].strip()
    #     # li_dict[li_id] = li_name
    # # pprint(li_dict)
        print(li.css('td:nth-child(1) a::attr(href)').extract_first())



# md5加密
def md5(code, length=None):
    res = hashlib.md5(code.encode('utf8')).hexdigest()
    if length is None:
        return res
    else:
        return res[:length]



def get_auth_sign(url):
    url = url.split('/fe_api/')[1]
    return 'X' + md5(f'/fe_api/{url}WSUDD')

# test_url = 'http://www.dianping.com/shenzhen/ch70/g20009p2'
test_url = 'http://bbs.jjwxc.net/bindex.php'
request_url(test_url)
