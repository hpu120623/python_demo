from pymongo import MongoClient


__all__ = ['ConnectMongo']


class ConnectMongo():
    """调用pymongo一些模块，实现对数据库的操作"""

    def __init__(self, HOST='127.0.0.1', PORT=27017, DB='test_data',
                 COLLECTION=''):
        self.client = MongoClient(HOST, PORT)
        self.collection = self.client[DB][COLLECTION]

    # 插入数据[]
    def insert_data(self, query=None, limit=None):
        self.collection.insert_one(query, limit)

    # 插入多条数据[]
    def insert_many_data(self, query=None):
        self.collection.insert_many(query)

    # 查询
    def find_data(self, query=None, limit=None):
        return list(self.collection.find(query, limit))

    # 查询
    def find_count_data(self, query=None, limit=None, count=1):
        return list(self.collection.find(query, limit).limit(count))

    # 查询数据条数
    def find_size(self, query=None, limit=None):
        return self.collection.find(query, limit)

    # 更新
    def update_data(self, query, data, ):
        self.collection.update_one(query, {'$set': data})

    # 更新多个参数
    def update_many_data(self, query, data, ):
        self.collection.update_many(query, {'$set': data})

    # 删除单个记录
    def delete_data(self, query):
        self.collection.delete_one(query)

    # 删除多个记录
    def delete_many_data(self, query):
        self.collection.delete_many(query)
