#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import wx
from wxbasics import FyLayoutMixin
from config.constants import *

class TreeView(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self._Set('_2sz_options_pane', (self.MakeOptions(), Fixed))
        self._Set('_2sz_tree_pane', (self.MakeTree(), Auto))
        self.FyLayout()
    def MakeOptions(self):
        return FyLayoutMixin(self)
    def MakeTree(self):
        return FyLayoutMixin(self)

class TreeViewOptions(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self.aspect = self._horizental
        self._Set('_2sz_collapse_all', (wx.Button(self, id=IdTreeCollapseAll, label='CollapseAll'), Auto))
        self._Set('_2sz_expand_all', (wx.Button(self, id=IdTreeExpandAll, label='ExpandAll'), Auto))
        self._Set('_2sz_collapse_this', (wx.Button(self, id=IdTreeCollapseThis, label='CollapseThis'), Auto))
        self._Set('_2sz_expand_this', (wx.Button(self, id=IdTreeExpandThis, label='ExpandThis'), Auto))
        self.FyLayout()

class TreeViewHome(FyLayoutMixin):
    def __init__(self, parent, root):
        '''
        root : must be instance of Node.node.common or its subclass
        '''
        FyLayoutMixin.__init__(self, parent)
        self._Set('_2sz__tree', (wx.TreeCtrl(self), Auto))
        self.FyLayout()
        self.__root = self._2sz__tree.AddRoot(text=`root`)
        self._2sz__tree.SetPyData(self.__root, root)
        self.AddItems(self.__root, root.GetKids())
        self._2sz__tree.Update()
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
        return TreeViewHome(self, root)
    def __Test(self):
        from common.node import UString2Node
        return UString2Node()
