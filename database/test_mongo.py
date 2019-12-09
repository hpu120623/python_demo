# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/10/31 9:56
'''
from pprint import pprint

from pymongo import MongoClient


client = MongoClient('192.168.1.209', 31016)
collection = client['dxy_hospital_index']['hospital_crawl_detail']
# search_result = list(collection.find({'hospitalName':'浙江省医疗健康集团', 'type': 'search', 'pubTime': '2019-11-19'}))
# search_result = list(collection.find())
# count_result = []
# for result in search_result:
#     hospital_name = result['name']
#     hospital_domain = result.get('domain', '')
#     # if not hospital_domain:
#     print(f'{hospital_name} {hospital_domain}')
common_aggregate = [
    {'$match': {'pubTime': {'$gte': '2019-11-24', '$lte': '2019-11-25'}}},
    {"$group": {
        "_id": {"type": "$type", "hospitalName": "$hospitalName", "pubTime": "$pubTime"},
        "pubNum": {"$sum": 1},
        "avgReadNum": {"$avg": "$readNum"},
        "avgPraiseNum": {"$avg": "$praiseNum"},
        "avgCommentNum": {"$avg": "$commentNum"},
        "commentNum": {"$sum": "$commentNum"},
        "forwardNum": {"$sum": "$forwardNum"},
        "readNum": {"$sum": "$readNum"},
        "praiseNum": {"$sum": "$praiseNum"},
        'baidu': {'$sum': '$baidu'},
        'so': {'$sum': '$so'},
        'sogou': {'$sum': '$sogou'},
        'alexaWorld': {'$sum': '$alexaWorld'},
        'alexaCN': {'$sum': '$alexaCN'}
    }
    }]
result = list(collection.aggregate(common_aggregate))
for hospital in result:
    pprint(hospital)
    # print(f"{hospital['_id']['hospitalName']}-{hospital['baidu']}-{hospital['so']}-{hospital['sogou']}")





