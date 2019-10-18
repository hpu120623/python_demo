import os
import re
import time
import dateparser
import moment

from datetime import datetime
from dateparser.search import search_dates
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
def quote_url(url, encoding='utf-8'):
    return quote(url, encoding=encoding)


# 对url进行unquote处理
def unquote_url(url, encoding='utf-8'):
    return unquote(url, encoding=encoding)


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


# 解析时间
def parse_time(time_str):
    def _search_dates(str):
        datetime = search_dates(str,
                                languages=['zh'],
                                settings={
                                    'DATE_ORDER': 'YMD',
                                    'STRICT_PARSING': True,
                                    'PREFER_LANGUAGE_DATE_ORDER': True,
                                    'PREFER_DATES_FROM': 'past'
                                })
        return int(time.mktime(datetime[0][1].timetuple())) * 1000

    def _is_valid_hour_time(str):
        '''判断是否是一个有效的日期字符串'''
        try:
            time.strptime(str, '%H:%M')
            return True
        except:
            return False

    def _format_date(time_str):
        '''
            格式化时间以便可以正常解析
            1、转化 年、月、日 为 -
            2、去掉 . 为 -
        '''
        if '月' in time_str and '日' in time_str:
            time_str = time_str \
                .replace('年', '-') \
                .replace('月', '-') \
                .replace('日', ' ')

        if '.' in time_str:
            time_str = time_str \
                .replace('.', '-')
        return time_str

    time_str = _format_date(time_str)
    # 格式化时间
    if _is_valid_hour_time(time_str):
        time_str = ' '.join([
            datetime.now().strftime('%Y-%m-%d'),
            time_str
        ])

    if '刚刚' in time_str or '刚才' in time_str:
        return int(time.time() * 1000)
    elif len(time_str.split('-')) == 2 or '前' in time_str:
        date_tuple = search_dates(str(time_str))
        if date_tuple:
            return int(time.mktime(date_tuple[0][1].timetuple()) * 1000)
        else:
            parse_time = dateparser.parse(str(time_str))
            return int(time.mktime(parse_time.timetuple()) * 1000)
    else:
        timestamp = None
        try:
            timestamp = _search_dates(time_str)
        except:
            moment_time = moment.date(time_str)
            if moment_time:
                timestamp = _search_dates(moment_time.format('YYYY-M-D H:m:s'))
        finally:
            return timestamp
