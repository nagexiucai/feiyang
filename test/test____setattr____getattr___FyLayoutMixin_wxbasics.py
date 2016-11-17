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
print '#####', k.a(), k.b(), k.c(), '#####'


class SampleP(object):
    def __setattr__(self, k, v):
        self.__dict__[k] = v
    def __getattr__(self, k):
        print '__getattr__'
        return self.__dict__.get(k)
#     def __getattribute__(self, k): #fall into infinite loop because self.__dict__ will call __getattribute again
#         print '__getattribute__'
#         return self.__dict__.get(k)
    def __init__(self):
        super(SampleP, self).__init__()
        self.x = 'x'
        self.y = 'y'
        self._ = '_'

class SampleQ(object):
    def __setattr__(self, k, v):
        super(SampleQ, self).__setattr__(k, v) #self.__setattr__(k, v) will fall into infinite loop till reach maximum depth
    def __getattr__(self, k):
        print '__getattr__'
        return self.__getattr__(k)
    def __getattribute__(self, k):
        print '__getattribute__'
        return super(SampleQ, self).__getattribute__(k)
    def __init__(self):
        super(SampleQ, self).__init__()
        self.x = 'x'
        self.y = 'y'
        self._ = '_'

p = SampleP()
q = SampleQ()
print '$$$$$', p.x, p.y, p._, '-----', q.x, q.y, q._, '$$$$$'

class KidSampleP(SampleP):
    def __init__(self):
        super(KidSampleP, self).__init__()
        self.z = 'z'

class KidSampleQ(SampleQ):
    def __init__(self):
        super(KidSampleQ, self).__init__()
        self.z = 'z'

kp = KidSampleP()
kq = KidSampleQ()
print '*****', kp.x, kp.y, kp.z, kp._, '-----', kq.x, kq.y, kq.z, kq._, '*****'
