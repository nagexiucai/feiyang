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
        self._2sz_grid.CreateGrid(InitRowCount, InitColumnCount) #BUG: 初始化时创建好
        self.FyLayout()
    def Create(self, r, c, mih=wx.grid.GRID_DEFAULT_ROW_HEIGHT, miw=wx.grid.GRID_DEFAULT_COL_WIDTH):
        #TODO: BUG——必须RESIZE父窗口才能显示正确，暂时采用“初始化时创建好、使用时增删行列”的方法规避
        self._2sz_grid.SetRowMinimalAcceptableHeight(mih)
        self._2sz_grid.SetColMinimalAcceptableWidth(miw)
        self._2sz_grid.CreateGrid(r, c)
        self.sizer.Fit(self)
    def Clear(self):
        self._2sz_grid.ClearGrid()
    def SetCell(self, r, c, value):
        self._2sz_grid.SetCellValue(r, c, value)
    def SetRowLabel(self, r, label):
        self._2sz_grid.SetRowLabelValue(r, label)
    def SetColLabel(self, c, label):
        self._2sz_grid.SetColLabelValue(c, label)
        self._2sz_grid.AutoSizeColLabelSize(c)
    def InsertRows(self, at, rows):
        self._2sz_grid.InsertRows(at, rows)
    def InsertCols(self, at, cols, labels=None):
        self._2sz_grid.InsertCols(at, cols)
    def DeleteRows(self, at, rows):
        self._2sz_grid.DeleteRows(at, rows)
    def DeleteCols(self, at, cols):
        self._2sz_grid.DeleteCols(at, cols)
