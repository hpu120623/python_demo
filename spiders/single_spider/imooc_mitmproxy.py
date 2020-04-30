# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/24 12:39
'''

import json

def response(flow):
    # if 'high.m3u8?'in flow.request.url:
    if 'high.jpg?cdn=aliyun1'in flow.request.url:
        print(json.loads(flow.response.text)['msg'])
        with open('info.txt', 'a') as f:
            f.write(flow.response.text)
            # f.write(json.loads(flow.response.text)['data']['info'])