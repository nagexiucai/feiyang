#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from wxbasics import FyLayoutMixin
from config.constants import *
from common.node import Node
from selectors import SimpleSelector

class TreeView(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self._2sz_options_pane = self.MakeOptions(), Fixed
        self._2sz_tree_pane = self.MakeTree(), Auto
        self.FyLayout()
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnNodeActivated)
    def MakeOptions(self):
        return FyLayoutMixin(self)
    def MakeTree(self):
        return FyLayoutMixin(self)
    #TODO: BEGIN 消息转发
    def OnButton(self, evt):
        label = self.FindWindowById(evt.GetId()).GetLabel()
        event = wx.PyCommandEvent(OPTIONS, self.GetId())
        event.SetClientData(label)
        self.GetEventHandler().ProcessEvent(event)
    def OnNodeActivated(self, evt):pass
#         name = self._2sz_tree_pane._2sz__tree.GetItemText(evt.GetItem())
#         print self.__class__.__name__, name
#         event = wx.PyCommandEvent(NODE_ACTIVATED, self.GetId())
#         event.SetClientData(name)
#         self.GetEventHandler().ProcessEvent(event)
    #END 消息转发

class TreeViewOptions(FyLayoutMixin):
    class Flex(FyLayoutMixin):
        def __init__(self, parent):
            FyLayoutMixin.__init__(self, parent)
            self.aspect = self._horizental
            self._2sz_collapse_all = wx.Button(self, size=(DefaultButtonWidth, Auto), label='CA'), Auto
            self._2sz_expand_all = wx.Button(self, size=(DefaultButtonWidth, Auto), label='EA'), Auto
            self._2sz_collapse_this = wx.Button(self, size=(DefaultButtonWidth, Auto), label='C'), Auto
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
        self.SetUserData(self.__root, root)
        self.AddItems(self.__root, root.GetKids())
        self._2sz__tree.Update()
    def GetRoot(self):
        return self.__root
    def SetUserText(self, node, text):
        self._2sz__tree.SetItemText(node, text)
    def SetUserData(self, node, data):
        self._2sz__tree.SetPyData(node, data)
    def GetUserData(self, node):
        return self._2sz__tree.GetPyData(node)
    def OnOptions(self, evt):
        act = evt.GetClientData()
        exec('self.On%s()' % act)
    def OnNew(self):pass
    def OnOpen(self):
        #TODO: Bug——正确选择一次，后边放弃选择会继续使用上次选择过的文件
        slt = SimpleSelector(self.GetTopLevelParent(), 'database source (*.db)|*.db')
        self.selected = slt.GetPath()
    def OnSave(self):pass
    def OnClose(self):pass
    def OnCA(self):pass
    def OnEA(self):pass
    def OnC(self):pass
    def OnE(self):pass
    def AddItems(self, parent, kids):
        '''
        add items recursively
        '''
        for kid in kids:
            item = self._2sz__tree.AppendItem(parent, text=`kid`)
            self.SetUserData(item, kid)
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
