#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from config.constants import *

def ShowMessage(msg, tag):
    wx.MessageBox(msg, tag, wx.OK)

def TextEntry(parent, msg, tag):
    te = wx.TextEntryDialog(parent, msg, tag)
    if te.ShowModal() == wx.ID_OK:
        return te.GetValue()
    te.Destroy()
