#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

class Parent(object):
    def __setattr__(self, attr, val):
        self.__dict__[attr] = val
    def __getattr__(self, attr):
        return self.__dict__.get(attr)
    def a(self):
        return 'a'
    def b(self):
        return 'b'

class Kid(Parent):
    def __init__(self):
        self.__dict__ = {}
        super(Kid, self).__init__()
        self.a = lambda : None
        #self.b = lambda : True

k = Kid()
k.c = lambda : False
print k.a(), k.b(), k.c()
