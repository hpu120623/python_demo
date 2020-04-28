# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 23:57
# @Author  : Amos.Li
from threading import Thread, Event

def f(event):
    print('wait Event')
    event.wait()
    print('f end...')

e = Event()
thread = Thread(target=f, args=(e,))
thread.start()
e.set()