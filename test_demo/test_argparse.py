# coding=utf-8
# Author: Amos.Li
# date: 2019/11/29 14:49
import argparse


def get_options():
    parser = argparse.ArgumentParser()

    # 爬虫类型
    parser.add_argument('-s', '--spider', dest='spider_name', help='choose a spider to run')

    return parser.parse_args()

def bootstrap():
    options = get_options()
    run_spider(options.spider_name)
