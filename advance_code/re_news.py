import re

# 过滤新闻URL，截取后续不需要的部分
# pattern = r'.*52rd.com.*/\d{4}_\d+/\w+.HTM'
# pattern = r'.*sohu.com/a.*?_\d+'
pattern = r'.*qihoo.com/\w+'


# test_url = 'http://www.52rd.com/S_TXT/2019_3/TXT113874.HTM?WebShieldDRSessionVerify=F31NTuP3MxZFg1trmKRf'
# test_url = 'http://www.sohu.com/a/301395791_114988?spm=_155261507282'
test_url = 'https://sh.qihoo.com/994ec595465e12cc3'
result = re.search(pattern, test_url)
print(result.group())