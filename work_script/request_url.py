# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/22 17:56
import requests
from retrying import retry
from pyquery import PyQuery as pq


@retry(stop_max_attempt_number=3)
def request_url(request_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36',
        # 'Cookie': 'sessionid=D3886C66-E158-4B7A-A03C-174F99DF24C6%7C%7C2019-03-11+16%3A33%3A06.607%7C%7C0; __ah_uuid=ACB03960-39CB-4241-89E2-B851E725356B; fvlid=15522931810576hBpOk59mX; ahpau=1; cookieCityId=110100; autoid=13613cdee96f361b1d37147b6c278b06; sessionvid=CCA16A8E-2A01-4C2E-8607-D17CC68FAE98; sessionuid=D3886C66-E158-4B7A-A03C-174F99DF24C6%7C%7C2019-03-11+16%3A33%3A06.607%7C%7C0; sessionip=114.88.110.51; area=310106; papopclub=C82A2BE6EDCE81088629347479D49E83; pbcpopclub=55273bf8-428e-4d14-963c-88f45925f7a4; pepopclub=29E40913ADF553B8F99A9F5E64E447DB; ahpvno=6; ahrlid=155374300864934uWIpZ9Qb-1553743010820; ref=www.google.com%7C0%7C0%7C0%7C2019-03-28+11%3A16%3A54.546%7C2019-03-28+10%3A43%3A17.724',
        'Referer': 'http://so.eastmoney.com'
        }
    # proxies = {
    #     'https': 'http://103.46.128.41:57345'
    # }
    response = requests.get(request_url, headers=headers)
    # response.encoding = 'utf8'
    # dom = pq(response.text)
    # title = dom('title').text()
    print(response.text)


test_url = 'http://api.so.eastmoney.com/bussiness/Web/GetSearchList?type=701&pageindex=3&pagesize=10&keyword=%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD'

for i in range(10):
    request_url(test_url)
