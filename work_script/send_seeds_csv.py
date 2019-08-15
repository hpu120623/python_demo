# -*- coding: utf-8 -*-

import csv
import json
import requests


ag_url = 'http://cain.search.1datatech.cn/api/seed'            # 示例：生产meta环境

def get_seed(row):
    data = {
        "description": row['desc'],                     # 种子描述
        "majorCategory": "seed_non_keyword",
        "minorCategory": "seed_forum_phpwind_url",   # 种子类型
        "relationCode": "seed_forum_phpwind_url",    # 种子类型
        "templateId": 121,                              # 种子对应的模板ID
        "val": row['val']                               # 种子值
    }
    return data

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': 'whereareyou',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
}

with open('phpwind.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        response = requests.post(ag_url, headers=headers, data=json.dumps(get_seed(row)))
        result = json.loads(response.text)
        if result['code'] == 500:
            print(f"种子导入重复: {row['val']}")
        elif result['code'] == 200:
            print(f"种子导入成功")
        else:
            print(response.status_code)
