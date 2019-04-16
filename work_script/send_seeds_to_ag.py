import csv
import json
import requests


ag_url = 'http://cain.1datatech.cn/api/seed'

def get_seed(row):
    data = {
        "description": row['desc'],
        "majorCategory": "seed_non_keyword",
        "minorCategory": "seed_jinritoutiao_user_id",
        "relationCode": "seed_jinritoutiao_user_id",
        "templateId": 123,
        "val": row['val']
    }
    return data

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': 'whereareyou',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
}

with open('今日头条ID.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        response = requests.post(ag_url, headers=headers, data=json.dumps(get_seed(row)))
        print(response.text)