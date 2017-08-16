#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from plugins import PluginPoints
from widgets.treeviews import TreeView, TreeViewOptions, TreeViewHome
from widgets.texteditor import Editor
from common.node import Node

class CourseWareTreeViewHome(TreeViewHome):
    def __init__(self, parent, root):
        TreeViewHome.__init__(self, parent, root)

class CourseWareSection(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeOptions(self):
        return TreeViewOptions(self)
    def MakeTree(self):
        return CourseWareTreeViewHome(self, Node('manual'))

class CourseWare(PluginPoints):
    def __init__(self):
        PluginPoints.__init__(self)
    def MustBeCustomized(self):
        self.explorer = CourseWareSection(PluginPoints.EXPLORER)
        self.explorer.SetName('Outline')
        self.interpreter = Editor(PluginPoints.INTERPRETER)
        self.interpreter.SetName('Log')
        self.media = Editor(PluginPoints.MEDIA)
        self.media.SetName('Box')

PluginPoints.SecureRegister('"Course&Ware"[CTRL+W](As UI for Course.)<>', CourseWare)
