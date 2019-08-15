import re


test = 'http://xdrug.dxy.cn/bbs/board/114'
res = re.findall(r'board/(.*)', test)
print(res)