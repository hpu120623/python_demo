# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 0:06
# @Author  : Amos.Li




# class Test:
#     def __init__(self):
#         print(f'the class is {Test.__name__}')
#
# obj_list = []
# obj_list.append(func)
# obj_list.append(Test)
#
# for item in obj_list:
#     print(item())

def func(name='Python'):
    print(f'the func is {name}')

def decorator_func():
    print(f'the decorator_func is running')
    return func

my_test = decorator_func()
my_test('木子的三维世界')