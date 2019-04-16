# -*- coding: utf-8 -*-
# @Author  : Amos.Li
# @Time    : 2019/3/28 18:22
import logging
from study import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()