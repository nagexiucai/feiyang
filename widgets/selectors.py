#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from config.constants import *
from common.fsoperate import MakeBasePath

def SimpleSelector(parent, wildcard):
    dlg = wx.FileDialog(parent,
                        message="Select a file",
                        defaultDir=MakeBasePath(),
                        wildcard=wildcard,
                        style=wx.OPEN|wx.CHANGE_DIR)
    dlg.CenterOnParent()
    dlg.ShowModal()
    return dlg
