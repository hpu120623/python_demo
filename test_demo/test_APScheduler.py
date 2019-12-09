# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@gmail.com

date: 2019/11/7 10:17
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, "cron", day_of_week="1-5", hour=16, minute=37)
# scheduler.add_job(job, "interval", seconds=3)
scheduler.start()
