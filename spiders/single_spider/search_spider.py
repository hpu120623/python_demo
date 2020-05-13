# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/22 17:56
import requests
from retrying import retry
from parsel import Selector
from urllib.parse import urljoin


@retry(stop_max_attempt_number=3)
def search_data(request_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
    }

    response = requests.get(request_url, headers=headers)
    response.encoding = 'utf8'
    selector = Selector(response)
    result_list = selector.css('table tr.tr3')
    for result in result_list:
        url = result.css('h3 a::attr(href)').extract_first()
        title = result.css('h3 a::text').extract_first()
        if title and 'xxx' in title:
            print(f'title:{title}: {urljoin(response.url, url)}')


def main():
    request_url = 'http://z1.1080pgqzz.info/pw/thread.php?fid=22&type=2&page={page_num}'
    for i in range(1, 51):
        search_data(request_url.format(page_num=i))


if __name__ == '__main__':
    main()
