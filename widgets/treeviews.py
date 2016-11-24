#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import wx
from wxbasics import FyLayoutMixin
from config.constants import *
from common.node import Node

class TreeView(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self._2sz_options_pane = self.MakeOptions(), Fixed
        self._2sz_tree_pane = self.MakeTree(), Auto
        self.FyLayout()
        self.Bind(wx.EVT_BUTTON, self.OnOptions)
    def MakeOptions(self):
        return FyLayoutMixin(self)
    def MakeTree(self):
        return FyLayoutMixin(self)
    def OnOptions(self, evt):
        print self.__class__.__name__, evt.GetId()
        event = wx.PyCommandEvent(OPTIONS, self.GetId())
        self.GetEventHandler().ProcessEvent(event)

class TreeViewOptions(FyLayoutMixin):
    class Flex(FyLayoutMixin):
        def __init__(self, parent):
            FyLayoutMixin.__init__(self, parent)
            self.aspect = self._horizental
            self._2sz_collapse_all = wx.Button(self, size=(DefaultButtonWidth, Auto), label='-A'), Auto
            self._2sz_expand_all = wx.Button(self, size=(DefaultButtonWidth, Auto), label='EA'), Auto
            self._2sz_collapse_this = wx.Button(self, size=(DefaultButtonWidth, Auto), label='-'), Auto
            self._2sz_expand_this = wx.Button(self, size=(DefaultButtonWidth, Auto), label='E'), Auto
            self.FyLayout()
    class Manipulate(FyLayoutMixin):
        def __init__(self, parent):
            FyLayoutMixin.__init__(self, parent)
            self.aspect = self._horizental
            self._2sz_new = wx.Button(self, size=(DefaultButtonWidth, Auto), label='New'), Auto
            self._2sz_open = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Open'), Auto
            self._2sz_save = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Save'), Auto
            self._2sz_close = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Close'), Auto
            self.FyLayout()
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self._2sz_flex = TreeViewOptions.Flex(self), Fixed
        self._2sz_manipulate = TreeViewOptions.Manipulate(self), Fixed
        self.FyLayout()

class TreeViewHome(FyLayoutMixin):
    def __init__(self, parent, root):
        '''
        root : must be instance of Node.node.common or its subclass
        '''
        FyLayoutMixin.__init__(self, parent)
        self._2sz__tree = wx.TreeCtrl(self), Auto
        self.FyLayout()
        self.__root = self._2sz__tree.AddRoot(text=`root`)
        self._2sz__tree.SetPyData(self.__root, root)
        self.AddItems(self.__root, root.GetKids())
        self._2sz__tree.Update()
        self.RegisterEvent()
    def RegisterEvent(self):
        EM.eventManager.Register(self._OnOptions, OPTIONS_BD, self.GetParent())
    def _OnOptions(self, evt):
        print self.__class__.__name__
    def AddItems(self, parent, kids):
        '''
        add items recursively
        '''
        for kid in kids:
            item = self._2sz__tree.AppendItem(parent, text=`kid`)
            self._2sz__tree.SetPyData(item, kid)
            self.AddItems(item, kid.GetKids())

class FSTreeView(TreeView):
    def MakeOptions(self):
        return TreeViewOptions(self)
    def MakeTree(self, root=None):
        if DEBUG and root is None:
            root = self.__Test()
        assert isinstance(root, Node)
        return TreeViewHome(self, root)
    def __Test(self):
        from common.node import UString2Node
        return UString2Node()
