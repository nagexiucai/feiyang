#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import wx
import wx.aui
from config.constants import *

class FyLayoutMixin(wx.Panel):
    #以‘_2sz_’开头命名的属性，纳入布局考虑范围，这种属性以元组（窗体，生长方向）初始化赋值
    _horizental = wx.HORIZONTAL
    _vertical = wx.VERTICAL
    __2sz_value_length = 2
    __2sz_instance_index = 0
    __2sz_proportion_index = 1
    def __init__(self, parent):
        self.aspect = FyLayoutMixin._vertical
        self.__2SZ_attr2proportion_map = {}
        self.__2SZ_order = []
        wx.Panel.__init__(self, parent)
    def _Set(self, attr, val):
        assert isinstance(val, tuple) and (len(val) == self.__2sz_value_length)
        self.__2SZ_order.append(attr)
        self.__2SZ_attr2proportion_map[attr] = val[self.__2sz_proportion_index]
        self.__dict__[attr] = val[self.__2sz_instance_index]
    def FyLayout(self):
        self.sizer = wx.BoxSizer(self.aspect)
        for _2sz in self.__2SZ_order:
            _proportion = self.__2SZ_attr2proportion_map[_2sz]
            self.sizer.Add(self.__getattribute__(_2sz), proportion=_proportion, flag=wx.EXPAND|wx.ALL)
        self.SetSizer(self.sizer)
        self.sizer.Layout()

class FyMenuMixin(wx.Menu):
    __styles = {'normal': wx.ITEM_NORMAL, 'radio': wx.ITEM_RADIO, 'check': wx.ITEM_CHECK}
    def __init__(self, *args, **kws):
        wx.Menu.__init__(self, *args, **kws)
    def ParseDescription(self, description=None):
        '''
        "&Hi"[CTRL+H](Say 'Hi' To User.)<normal>
        "|"[]()<|>
        "&Top"[CTRL+T](Always Show On Top.)<check>
        '''
        if description is None:
            description = self.ParseDescription.__doc__.strip()
        for shortname, shortcut, tip, style in ReXMMenu.findall(description):
            if shortname == style == '|':
                self.AppendSeparator()
                continue
            self.Append(wx.NewId(), text='%s\t%s' % (shortname, shortcut), help=tip, kind=self.__styles.get(style, wx.ITEM_NORMAL))

class FyMenuBarMixin(wx.MenuBar):
    def __init__(self, parent):
        wx.MenuBar.__init__(self)
        parent.SetMenuBar(self)
        self.ParseDescription(parent)
    def ParseDescription(self, parent, description=None):
        #支持三层菜单
        #‘&’分隔一二层；‘;’分隔第二层；‘:’分隔二三层；第三层无分隔
        #第二层空分分割线；第三层‘shortname’和‘style’均为‘|’标识分割线
        #第二层（含）一下各片段语法："shortname"[shortcut](tips)<style>，‘shortname’中快捷键字母前加‘&’
        #第一层片段仅包含‘shortname’
        '''
        &File$"&New"[CTRL+N](Create Or Open Existence.)<>:"&Project"[CTRL+P](Manage Works.)<>"|"[]()<|>"T&Ext"[CTRL+E](For Words Editing.)<>"&Binary"[CTRL+B](For Data Editing.)<>;;"Save&As"[CTRL+A](Record On Disk.)<>
        &Edit
        Plug&Ins
        S&Kin$"Blue"[]()<radio>"Black"[]()<radio>"Silver"[]()<radio>
        &Help
        '''
        if description is None:
            description = self.ParseDescription.__doc__.strip()
            testm = FyMenuMixin()
            testm.ParseDescription()
            self.Append(testm, 'Test')
        for line in description.split('\n'):
            line = line.strip()
            if not line:
                continue
            parentm = FyMenuMixin()
            if line.find('$') != NotFound:
                line, pieces = line.split('$')
                for piece in pieces.split(';'):
                    if not piece.strip():
                        parentm.AppendSeparator()
                        continue
                    kidm = FyMenuMixin()
                    if piece.find(':') != NotFound:
                        piece, grands = piece.split(':')
                        kidm.ParseDescription(grands)
                        shortname, shortcut, _, __ = ReXMMenu.findall(piece)[MustBeOne]
                        parentm.AppendMenu(wx.NewId(), '%s\t%s' % (shortname, shortcut), kidm)
                    else:
                        parentm.ParseDescription(piece)
            self.Append(parentm, line)

class FyStatusBarMixin(wx.StatusBar):
    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent)
        parent.SetStatusBar(self)

class FyNotebookMixin(wx.aui.AuiNotebook):
    def __init__(self, parent):
        wx.aui.AuiNotebook.__init__(self, parent)
