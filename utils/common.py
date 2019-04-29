import os
import re

import moment
from tld import get_fld
from urllib.parse import quote, unquote


# 获取文件路径
def create_path(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, r'work_data\%s' % filename)
    return DATA_PATH


# 解析url域名
def parse_domain(url):
    result = get_fld(url, fail_silently=True)

    return result


# 对url进行quote处理
def quote_url(url):
    return quote(url)


# 对url进行unquote处理
def unquote_url(url):
    return unquote(url)


# 正则去除字符串中多个字符
def sub_str(words):
    # 例如：words = ' ni \t  "   * :::: #$@#$@   很  )_+_  $%#$%#     hao, 加油, #$%  \nhello '
    res = re.sub(r'[\'":\s\*@#$%)_+-]*', '', words)
    return res

def create_date():
    for query_type in ['day', 'week', 'month']:
        if query_type == 'day':
            date = moment.now().subtract(days=1).format('YYYYMD')
        elif query_type == 'week':
            date = moment.now().subtract(weeks=1).replace(weekday=1).format('YYYYMD')
        else:
            date = moment.now().subtract(weeks=4).replace(days=1).format('YYYYMD')
        return date


