import time
import datetime
now_time = datetime.datetime.now()

for i in range(1, 8):
    # 当前时间减去一天 获得昨天当前时间
    ago_time = (now_time + datetime.timedelta(days=-i)).strftime('%Y-%m-%d')
    print(ago_time)

timeStamp = 1567041263
dateArray = datetime.datetime.fromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d")
print(otherStyleTime)