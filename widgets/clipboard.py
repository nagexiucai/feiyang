#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from config.constants import wx

def GetClipboard(fmt='text'):
    data = wx.BitmapDataObject() if fmt == 'bmp' else wx.TextDataObject()
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        wx.TheClipboard.GetData(data)
        wx.TheClipboard.Close()
        return data.GetBitmap() if fmt == 'bmp' else data.GetText()

def SetClipboard(data, fmt='text'):
    data = wx.BitmapDataObject() if fmt == 'bmp' else wx.TextDataObject()
    data.SetBitmap(data) if fmt == 'bmp' else data.SetText(data)
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        return wx.TheClipboard.SetData(data)
        wx.TheClipboard.Close()
