#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

class PluginPoints(object):
    TOP = None
    EXPLORER = None
    INTERPRETER = None
    MEDIA = None

class M(object):
    def Define(self):
        pass

class V(object):
    def Show(self):
        pass

class C(object):
    def Operate(self):
        pass

class MVC(M, V, C):
    def __init__(self, m, v, c):
        M.__init__()
        V.__init__()
        C.__init__()
        self.m = m
        self.v = v
        self.c = c
    def Plugin(self):
        pass
    def Pullout(self):
        pass
