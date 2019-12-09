import time
import execjs
import re
import requests
from scrapy import Selector

from spiders.common.user_agent import FakeChromeUA


class HandleCsdn(object):
    """
    实现csdn博客详情页面中acw_sc_v2的值，JS逆向解析
    """

    def __init__(self):
        self.index_url = 'https://blog.csdn.net/XinYueChangLE/article/details/102474117'
        self.header = {
            'User-Agent': FakeChromeUA.get_ua()
        }

    def handle_request(self):
        # 首先获取arg1值
        js_response = requests.get(url=self.index_url, headers=self.header)
        result = re.findall(r"arg1='(.*?)';", js_response.text, re.S)
        if result:
            arg1_value = result[0]
            # 该值固定
            _0x5e8b26 = '3000176000856006061501533003690027800375'
            # 读取破解JS
            with open('csdn.js', 'r', encoding='utf-8') as f:
                f_read = f.read()
            js = execjs.compile(f_read)
            acw_sc__v2 = js.call("hexXor", _0x5e8b26, arg1_value)

            self.header['Cookie'] = 'acw_sc__v2=' + acw_sc__v2
        response = requests.get(url=self.index_url, headers=self.header)

        # 测试，是否请求成功
        selector = Selector(response)
        title = selector.css('h1.title-article::text').extract_first()
        print(f'title: {title}')


if __name__ == '__main__':
    uxin = HandleCsdn()
    for i in range(50):
        uxin.handle_request()
        time.sleep(0.3)
