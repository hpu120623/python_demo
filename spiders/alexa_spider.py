import re
import json
import requests

from pprint import pprint
from utils.common import parse_domain

from spiders.common.user_agent import FakeChromeUA

class AlexaIndexSpider:
    """
    获取网站Alexa国内国外排名
    """
    # 获取请求token
    alexa_token_url = 'http://www.alexa.cn/rank/{domain}'

    # 排名请求api
    alexa_index_api = 'http://www.alexa.cn/api/alexa/free?token={token}&url={domain}'

    def __init__(self, domain):
        self.url_domain = domain
        self.headers = {
            'User-Agent': FakeChromeUA.get_ua()
        }

    def request_alexa(self):
        # request_url = self.alexa_token_url.format(domain=self.url_domain)
        request_url = 'http://www.alexa.cn/rank/xjtu.edu.cn'
        response = requests.get(request_url, headers=self.headers)
        token = re.findall(r'token : \'(.*)\', domain.*', response.text, re.S)[0]
        return token

    def request_index(self, alexa_token):
        request_api = self.alexa_index_api.format(
            token=alexa_token,
            domain=self.url_domain
        )
        # request_api = 'http://www.alexa.cn/api/alexa/free?token=ce9afad407Jbi9jViUB-EIqqwgBGN1p1aJqbJKmiY5dsnzUt6lj4i9jUBrwPd8-HA-N&url=pumch.cn'
        index_response = requests.get(request_api, headers=self.headers)
        result = json.loads(index_response.text)['data']
        world_index = result['world_rank']              # 全球排名
        country_index = result['country_rank']          # 国家排名
        country_area = result['country_code']           # 国家/地区
        pprint(result)




if __name__ == '__main__':
    test_url = 'https://www.sina.com.cn/'
    test_domain = parse_domain(test_url)

    alexa = AlexaIndexSpider(test_domain)
    alexa_token = alexa.request_alexa()
    print(alexa_token)
    # alexa.request_index(alexa_token)

