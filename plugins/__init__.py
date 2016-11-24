#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from config.constants import *
from common.exceptions import Fatal

class PluginPoints(object):
    REGISTER = {}
    TOP = None
    EXPLORER = None
    INTERPRETER = None
    MEDIA = None
    @staticmethod
    def SecureRegister(name, plugin):
        assert ReXMMenu.match(name)
        assert issubclass(plugin, PluginPoints)
        PluginPoints.REGISTER[name] = plugin
    def __init__(self):
        self.MustBeCustomized()
        self.reference = {'e':self.explorer, 'i':self.interpreter, 'm':self.media}
        setattr(self.explorer, 'reference', self.reference)
        setattr(self.interpreter, 'reference', self.reference)
        setattr(self.media, 'reference', self.reference)
    def IsCurrent(self):
        #TODO: 暂时以explorer的当前页所属的插件为依据
        return self.explorer is PluginPoints.EXPLORER.GetCurrentPage()
    def MustBeCustomized(self):
        '''
        self.self.explorer = XXX
        self.interpreter = YYY
        self.media = ZZZ
        '''
        raise Fatal('please redefine MustBeCustomized!')
    def Plugin(self):
        '''
        PluginPoints.EXPLORER.AddPage(self.explorer, self.explorer.GetName(), select=True)
        PluginPoints.INTERPRETER.AddPage(self.interpreter, self.interpreter.GetName(), select=True)
        PluginPoints.MEDIA.AddPage(self.media, self.media.GetName(), select=True)
        '''
