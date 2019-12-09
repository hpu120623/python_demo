# coding=utf-8
# Author: Amos.Li
# date: 2019/11/14 13:13
import re

import requests

from scrapy import Selector
from spiders.common.random_proxy import *
from utils.common import md5

from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
collection = client['search_cookies']['so_cookies']



proxy = {
    'http': RandomProxy().SHORT_PROXY,
    'https': RandomProxy().SHORT_PROXY,
}

def get_guid():
    url = 'https://www.so.com'

    response = requests.get(url, headers=None)
    response.encoding = 'utf8'
    # guid = response.cookies.get_dict().get('QiHooGUID', '')
    cookies = response.request.headers['Cookie']
    if 'QiHooGUID' in cookies:
        guid = re.findall(r'QiHooGUID=(.*?);', cookies)[0]
        collection.insert_one({'_id':md5(guid),'guid': guid})
        print(f'insert_ok:{guid}')
    else:
        print(cookies)

def so_search(guid):
    search_url = 'https://www.so.com/s?q=%E6%98%86%E6%98%8E%E5%8C%BB%E7%A7%91%E5%A4%A7%E5%AD%A6%E7%AC%AC%E4%B8%80%E9%99%84%E5%B1%9E%E5%8C%BB%E9%99%A2'

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Cookie': 'QiHooGUID=%s'%guid
        # 'Referer': 'https://www.so.com/haosou.html',
        # 'Host': 'www.so.com'
    }

    response = requests.get(search_url, headers=headers, proxies=proxy)
    selector = Selector(response)
    result = selector.css('.nums::text').extract_first()
    print(result)

if __name__ == '__main__':
    guid = list(collection.find().limit(1))[0]['guid']
    for i in range(100):
        so_search(guid)


