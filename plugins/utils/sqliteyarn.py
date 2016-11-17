#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from plugins import M, V, C, MVC

class RecordM(M):
    def Define(self):
        self.record = []

class TableM(M):
    def Define(self):
        self.structure = None
        self.records = []

class DatabaseM(M):
    def Define(self):
        self.schema = {}

class RecordV(V):
    def Show(self):
        pass

class TableV(V):
    def Show(self):
        pass

class DatabaseV(V):
    def Show(self):
        pass

class RecordC(C):
    def Operate(self):
        pass

class TableC(C):
    def Operate(self):
        pass

class DatabaseC(C):
    def Operate(self):
        pass

class SQLiteYarn(MVC):
    def Plugin(self):
        pass
