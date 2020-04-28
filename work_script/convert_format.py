# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 18:20
# @Author  : Amos.Li

import json

industry_list = [
  {
     "parent_ind" : "女装",
     "name" : "你好"
  },
  {
     "name": "女装"
  },
  {
     "parent_ind" : "女装",
     "name" : "半身裙"
  },
  {
     "parent_ind" : "女装",
     "name" : "A字裙"
  },
  {
     "name": "数码"
  },
  {
    "parent_ind" : "数码",
     "name": "电脑配件"
  },
  {
    "parent_ind" : "电脑配件",
     "name": "内存"
  },
]


def convert_format(data):
    result_dict = {}

    test_key = [i['name'] for i in data if len(i) == 1]
    test_value = list(i for i in data if len(i) == 2)

    for key in test_key:
        result_dict[key] = {}
        for item in test_value:
            if key == item['parent_ind']:
                result_dict[key][item['name']] = {}
            elif item['parent_ind'] not in test_key and item['parent_ind'] in result_dict[key]:
                result_dict[key][item['parent_ind']][item['name']] = {}

    print(json.dumps(result_dict,ensure_ascii=False))
convert_format(industry_list)