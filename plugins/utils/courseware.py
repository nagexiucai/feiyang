#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from plugins import PluginPoints
from widgets.wxbasics import FyLayoutMixin, FyMenuMixin
from widgets.treeviews import TreeView, TreeViewHome
from widgets.texteditor import Editor, Board
from widgets.imagengine import ImageBox
from common.node import Node
from config.constants import *

class CourseWareTreeViewHome(TreeViewHome):
    def __init__(self, parent, root):
        TreeViewHome.__init__(self, parent, root)

class CourseWarePopupMenu(FyMenuMixin):
    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        self.switch = None
        self.Bind(wx.EVT_MENU, self.OnMenu)
        self.ParseDescription('"Description"[](Text Things.)<>"Picture"[](BMP Things.)<>"|"[]()<|>"Subject"[](Paragraph Things.)<>')
    def OnMenu(self, evt):
        self.switch = self.FindItemById(evt.GetId()).GetLabel()

class CourseWareSection(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeTree(self):
        return CourseWareTreeViewHome(self, Node('manual'))
    def OnNodeActivated(self, evt):pass
    def OnNodeMenu(self, evt):
        popup = CourseWarePopupMenu(self)
        self.PopupMenu(popup, evt.GetPoint())
        if popup.switch == 'Description':
            section = Editor(self.reference['m'])
        elif popup.switch == 'Picture':
            section = ImageBox(self.reference['m'])
        elif popup.switch == 'Subject':
            section = Board(self.reference['m'])
        else:
            section = None
        if section:
            self.reference['m'].sizer.Add(section, proportion=Auto, flag=wx.EXPAND|wx.ALL)
            self.reference['m'].sizer.Layout()
            self._2sz_tree_pane._2sz__tree
        popup.Destroy()

class CourseWareComposer(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self.FyLayout()

class CourseWare(PluginPoints):
    def __init__(self):
        PluginPoints.__init__(self)
    def MustBeCustomized(self):
        self.explorer = CourseWareSection(PluginPoints.EXPLORER)
        self.explorer.SetName('Outline')
        self.interpreter = Editor(PluginPoints.INTERPRETER)
        self.interpreter.SetName('Log')
        self.interpreter.Disable()
        self.media = CourseWareComposer(PluginPoints.MEDIA)
        self.media.SetName('Box')

PluginPoints.SecureRegister('"Course&Ware"[CTRL+W](As UI for Course.)<>', CourseWare)
