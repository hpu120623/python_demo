import requests
import time
from urllib.parse import urlencode
import uuid
from pymongo import MongoClient
from scrapy import Selector


def get_cookie(url):
    response = requests.get(url, headers=headers)
    v_cookie = response.cookies.get_dict()
    snuid = v_cookie['SNUID']
    get_suv(snuid)


def get_suv(snuid):
    data = {
        "uigs_t": str(int(round(time.time() * 1000))),
        "uuid": uuid.uuid1(),
        "snuid": snuid.split("=")[-1],
    }
    suv_url = "https://pb.sogou.com/pv.gif?" + urlencode(data)

    response = requests.get(suv_url)
    suv = response.cookies.get_dict()['SUV']
    headers['Cookie'] = ('SNUID=%s'%snuid + ';' + 'SUV=%s'%suv).strip()
    collection = MongoClient('192.168.1.209', 31016)['dxy_hospital_index']['hospital_info']
    result_list = list(collection.find().limit(10))
    for result in result_list:
        search_url = 'https://www.sogou.com/web?query={}'.format(result['name'])
        res = requests.get(search_url, headers=headers)
        selector = Selector(res)
        result = selector.css('.search-info .num-tips::text').extract_first()
        print(result)
    # return res_cookie[-1]


if __name__ == '__main__':
    query_url = 'https://v.sogou.com'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }

    get_cookie(query_url)

