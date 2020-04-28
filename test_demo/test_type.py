# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 23:54
# @Author  : Amos.Li

a=2019
b="一切皆对象"
print(type(2019))
print(type(int))
print(type(b))
print(type(str))

class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))
print(type(type))