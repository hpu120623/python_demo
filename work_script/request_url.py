# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/22 17:56
import json
from urllib.parse import quote

import requests
from retrying import retry
from pyquery import PyQuery as pq
from scrapy.selector import Selector


@retry(stop_max_attempt_number=3)
def request_url(request_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
        'Cookie': 'SINAGLOBAL=172.16.138.137_1552292496.215543; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdK_niWPrLe.gs43K78Ihb; UOR=,tech.sina.com.cn,; vjuids=857254ee9.169716a5e05.0.22aa3497e81b1; U_TRS1=00000097.278da96b.5c8787c7.ff037556; SUB=_2AkMr4efSf8PxqwJRmP0Wymnrbo1yzAvEieKdvRYJJRMyHRl-yD83qldbtRB6AGHJPQemKU5ssyiKsD-7T9ELXcYet_Uj; Apache=35.220.252.151_1556501449.799959; lxlrttp=1556243090; ULV=1556501503364:15:11:2:35.220.252.151_1556501449.799959:1556446618477; vjlast=1556502372; Hm_lvt_f31b3bde5ef6233a36928514fb59f9cd=1556502854; Hm_lpvt_f31b3bde5ef6233a36928514fb59f9cd=1556502854; UM_distinctid=16a66cde02c314-0e1afe26c3b52c-7a1b34-100200-16a66cde02d55b',
        # 'Referer': 'http://so.eastmoney.com'
        }
    # proxies = {
    #     'https': 'http://103.46.128.41:57345'
    # }
    response = requests.get(request_url, headers=headers)
    print(response.status_code)
    # response.encoding = 'utf8'
    # dom = pq(response.text)
    # title = dom('title').text()
    # print(response.text)
    selector = Selector(response)
    url_list = selector.css('h3 a::attr(href)').extract()
    return url_list

test_url = 'http://db.auto.sina.com.cn/search/?search_txt=%(keyword)s&page=%(page_num)s'

for i in range(1, 10 + 1):
    format_url = test_url % {
        'keyword': quote('奥迪'),
        'page_num': i
    }

    for url in request_url(format_url):
        print(f'第{i}页： {url}')

