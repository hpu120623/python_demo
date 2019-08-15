import json
import re
import hashlib

from pprint import pprint

import requests
from retrying import retry
from scrapy.selector import Selector



def shop_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
        'Cookie': '_hc.v=1234',
        'Referer': 'http://www.dianping.com/shenzhen/education'
    }
    response = requests.get(url, headers=headers)
    print(response.url)

    # 调用Scrapy中选择器进行解析
    selector = Selector(response)
    shop_list = selector.css('.shop-list li')
    for shop in shop_list:
        shop_url = shop.css('div.tit a::attr(href)').extract_first()
        shop_name = shop.css('div.tit a::attr(title)').extract_first()
        print(f'{shop_name}: {shop_url}')
        # yield shop_url

def shop_detail(url, category):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
        'Cookie': '_hc.v=1234',
        'Referer': 'http://www.dianping.com/shenzhen/education'
    }
    response = requests.get(url, headers=headers)
    selector = Selector(response)
    shop_item = {}
    shop_item['url'] = response.url
    shop_item['city'] = '深圳'
    shop_item['column'] = '学习培训'
    shop_item['category'] = category
    shop_item['name'] = selector.css('div.shop-name h1::text').extract_first()
    pprint(shop_item)


def main():
    category_dict = {
        '语言培训': 'g2872',
        # '美术培训': 'g2874',
        # '音乐培训': 'g2873',
        # '升学辅导': 'g2876',
        # '留学': 'g32722',
        # '教育院校': 'g260',
        # '书法培训': 'g33757',
        # '兴趣生活': 'g2878',
        # '在线教育网校': 'g34107',
        # '运动培训': 'g34129'
    }
    column_url = 'http://www.dianping.com/shenzhen/ch{column_id}/{category_id}p{page_num}'

    for page in range(1, 51):
        for category in category_dict:
            request_url = column_url.format(
                column_id=75,
                category_id=category_dict[category],
                page_num=page
            )
            shop_list(request_url)
            # for shop_url in shop_list(request_url):
            #     shop_detail(shop_url, category)

if __name__ == '__main__':
    main()
