#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from wxbasics import FyLayoutMixin
import wx.grid
from config.constants import *

class SimpGridViewOptions(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self.aspect = self._horizental
        self._2sz_new = wx.Button(self, size=(DefaultButtonWidth, Auto), label='New'), Auto
        self._2sz_open = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Open'), Auto
        self._2sz_save = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Save'), Auto
        self._2sz_close = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Close'), Auto
        self.FyLayout()

class SimpGridView(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self._2sz_options = SimpGridViewOptions(self), Fixed
        self._2sz_grid = wx.grid.Grid(self), Auto
        self.FyLayout()
    def Create(self, r, c, mih=wx.grid.GRID_DEFAULT_ROW_HEIGHT, miw=wx.grid.GRID_DEFAULT_COL_WIDTH):
        self._2sz_grid.CreateGrid(r, c)
        self._2sz_grid.SetRowMinimalAcceptableHeight(mih)
        self._2sz_grid.SetColMinimalAcceptableWidth(miw)
    def SetRowLabel(self, r, label):
        self._2sz_grid.SetRowLabelValue(r, label)
    def SetColLabel(self, c, label):
        self._2sz_grid.SetColLabelValue(c, label)
    def InsertRows(self, at, rows):
        self._2sz_grid.InsertRows(at, rows)
    def InsertCols(self, at, cols, labels=None):
        self._2sz_grid.InsertCols(at, cols)
    def DeleteRows(self, at, rows):
        self._2sz_grid.DeleteRows(at, rows)
    def DeleteCols(self, at, cols):
        self._2sz_grid.DeleteCols(at, cols)
