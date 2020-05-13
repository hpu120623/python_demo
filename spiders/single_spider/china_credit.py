import json
import requests

from pprint import pprint
from retrying import retry
from parsel import Selector
from urllib.parse import urljoin

from utils.common import unquote_url


@retry(stop_max_attempt_number=3)
def china_credit(request_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
    }

    response = requests.get(request_url, headers=headers)
    result = json.loads(response.text)
    pprint(result)

if __name__ == '__main__':
    # test_url = 'https://public.creditchina.gov.cn/private-api/catalogSearchHome?keyword=%E5%A3%B9%E6%B2%93%E7%A7%91%E6%8A%80&tableName=credit_xyzx_tyshxydm&searchState=2&page=1'
    test_url = 'https://public.creditchina.gov.cn/private-api/getTyshxydmDetailsContent?keyword=%E5%A3%B9%E6%B2%93%E7%A7%91%E6%8A%80(%E4%B8%8A%E6%B5%B7)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&entityType=1&searchState=1&uuid=b9e58f77cd29efe944a755483dd340e6&tyshxydm=91310114MA1GTPB26F'
    china_credit(test_url)
    # print(unquote_url(test_url))