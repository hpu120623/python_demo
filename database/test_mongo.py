
from database.conn_mongo import ConnectMongo
from spiders.common.user_agent import FakeChromeUA

headers = {
    'User-Agent': FakeChromeUA.get_ua()
}

for i in range(10):
    ConnectMongo(COLLECTION='ua').insert_data({'ua': headers})