import json
import requests

from pprint import pprint

from spiders.common.user_agent import FakeChromeUA






headers = {
    'User-Agent': FakeChromeUA.get_ua()
    }

form_data = {
    '__biz':'MzIxNjM4NDE2MA==',
    'mid':'2247491827',
    'sn':'2e41e2b83e00b17f404265db739c5175',
    'idx':1,
    'scene':38,
}

def get_wx_article(biz, uin, key, offset=0, count=10):
    article_list_api = 'https://mp.weixin.qq.com/mp/profile_ext'
    params = {
        '__biz': biz,
        'uin': uin,
        'key': key,
        'offset': offset,
        'count': count,
        'action': 'getmsg',
        'f': 'json'
    }
    res = requests.post(article_list_api, headers=headers, params=params)

    # pprint(json.loads(res.text))
    article_list = json.loads(res.text)['general_msg_list']
    result = json.loads(article_list)['list']
    # pprint(result)
    for article in result:
        article_data = article.get('app_msg_ext_info', {})
        if article_data:
            article_item = {}
            article_item['title'] = article_data['title']
            article_item['url'] = article_data['content_url']
            article_item['author'] = article_data['author']
            article_item['desc'] = article_data['digest']
            pprint(article_item)


if __name__ == '__main__':
    biz = 'MzUzNzg1NDk4NA%3D%3D'
    uin = 'ODkxNDAzMDc5'
    key = '28a0f481c5d883acb107a6b25e988c0b81a967c192e571547b4ed8e5bad77c2fa1d4a482835d7dc1932d4d89bb257005043754a06dd75a8a4b07613e0c733512b57f863e1ea904a93d9c7cbccb1e1526'
    get_wx_article(biz, uin, key)
