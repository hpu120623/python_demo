# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/11/14 10:54
'''
import random


# 默认配置
class RandomProxy:
    '''
    外部服务
    '''
    # 云打码平台
    YUNDAMA_API_URL = 'http://api.yundama.com/api.php'
    YUNDAMA_USER_NAME = 'pangjiafu'
    YUNDAMA_PWD = '123qweasd'
    YUNDAMA_APP_ID = '4572'
    YUNDAMA_APP_KEY = '103af5ee800640a8e29746f2b4c65491'

    # 实时代理
    REALTIME_PROXYS = [
        ('YIDAKJGC2J9NMS0', 'BJcfbVX1', 'http-proxy-t3.dobel.cn:9180',)
    ]

    # 短效代理
    SHORT_PROXYS = [
        ('YIDAKJ6CCJRL7S0', 'DzsLfR8e', 'http-proxy-t1.dobel.cn:9180',),
        ('YIDAKJG2CJR1RS1', '4PUNttKK', 'http-proxy-t1.dobel.cn:9180',),
        ('YITAKJ6EHASL3O1', 'SwdRGpdd', 'http-proxy-t1.dobel.cn:9180',),
        ('YITAKJG4HASLN40', 'vNwKO5rO', 'http-proxy-t1.dobel.cn:9180',),
    ]

    @property
    def REALTIME_PROXY(self):
        REALTIME_PROXY = self.REALTIME_PROXYS[random.randint(0, 0)]
        return 'http://%(username)s:%(password)s@%(host)s' % {
            'username': REALTIME_PROXY[0],
            'password': REALTIME_PROXY[1],
            'host': REALTIME_PROXY[2]
        }

    @property
    def SHORT_PROXY(self):
        REALTIME_PROXY = self.SHORT_PROXYS[random.randint(0, 3)]
        return 'http://%(username)s:%(password)s@%(host)s' % {
            'username': REALTIME_PROXY[0],
            'password': REALTIME_PROXY[1],
            'host': REALTIME_PROXY[2]
        }
