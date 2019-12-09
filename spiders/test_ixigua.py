# coding=utf-8
# Author: Amos.Li
# date: 2019/11/28 13:37
import requests
from scrapy.selector import Selector

from spiders.common.random_proxy import RandomProxy


def get_ixigua(url):
    headers = {
        'cookie':'xiguavideopcwebid=6764246150318786061',
        # 'cookie':'xiguavideopcwebid=%s',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    proxy = {
        'http': RandomProxy().SHORT_PROXY,
        'https': RandomProxy().SHORT_PROXY,
    }

    # res = requests.get('https://www.ixigua.com/')
    # cookies = res.cookies.get_dict()
    # print(cookies['xiguavideopcwebid'])
    # headers['cookie'] = headers['cookie']%cookies['xiguavideopcwebid']
    # print(headers['cookie'])
    response = requests.get(url, headers=headers, proxies=proxy)
    selector = Selector(response)
    title = selector.css('h1.hasSource::text').extract_first()
    print(title)





if __name__ == '__main__':
    get_ixigua('https://www.ixigua.com/i6733912289876902414/')