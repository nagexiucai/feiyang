#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from config.constants import *

class PluginPoints(object):
    REGISTER = {}
    TOP = None
    EXPLORER = None
    INTERPRETER = None
    MEDIA = None
    @staticmethod
    def SecureRegister(name, plugin):
        assert ReXMMenu.match(name)
        assert issubclass(plugin, M)
        PluginPoints.REGISTER[name] = plugin

class M(object):
    def __init__(self, *args):
        pass
    def Plugin(self):
        pass
