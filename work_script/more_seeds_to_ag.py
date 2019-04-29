import csv
import json
import requests
from pprint import pprint

from utils.common import create_path

# 线上自建系统
ag_url = 'http://cain.search.1datatech.cn/api/seed'

def get_seed(row):
    val_list = ['val', 'val1', 'val2', 'val3', 'val4', 'val5']
    id_list = [
        ['seed_jinritoutiao_user_id', 29],
        ['seed_sohu_author_id', 48],
        ['seed_netease_app_user_id', 199],
        ['seed_baijia_author_id', 79],
        ['seed_36kr_user_id', 195],
        ['seed_xueqiu_author_id', 53]
    ]
    row_dict = dict(zip(val_list, id_list))
    for key in row_dict:
        if row[key]:
            data = {
                "description": row['desc'], # 种子描述
                "majorCategory": "seed_non_keyword",
                "minorCategory": row_dict[key][0],    # 种子的分类，查看字典管理中种子类别
                "relationCode": row_dict[key][0],
                "templateId": row_dict[key][1],  # 种子对应的模板id
                "val": row[key],  # 导入种子的值
                "isAjax": 1
            }
            yield data

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': 'whereareyou',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
}

file = create_path('we_media_account.csv')
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for data in get_seed(row):
            response = requests.post(ag_url, headers=headers, data=json.dumps(data))
            print(response.text)
