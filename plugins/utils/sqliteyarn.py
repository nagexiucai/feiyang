#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from plugins import PluginPoints
from widgets.grids import SimpGridView
from widgets.treeviews import TreeView, TreeViewOptions, TreeViewHome
from widgets.texteditor import Editor
from common.node import Node
from config.constants import *

class SQLiteYarnDatabase(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeOptions(self):
        return TreeViewOptions(self)
    def MakeTree(self):
        return TreeViewHome(self, Node('Node'))

class SQLiteYarn(PluginPoints):
    def __init__(self):
        PluginPoints.__init__(self)
    def MustBeCustomized(self):
        self.explorer = SQLiteYarnDatabase(PluginPoints.EXPLORER)
        self.explorer.SetName('Database')
        self.interpreter = Editor(PluginPoints.INTERPRETER)
        self.interpreter.SetName('Sql')
        self.media = SimpGridView(PluginPoints.MEDIA)
        self.media.SetName('Table')
        EM.eventManager.Register(self.OnNewProject, NEW_PROJECT_BD, PluginPoints.TOP)
    def Plugin(self):
        PluginPoints.EXPLORER.AddPage(self.explorer, self.explorer.GetName(), select=True)
        PluginPoints.EXPLORER.Update()
        PluginPoints.INTERPRETER.AddPage(self.interpreter, self.interpreter.GetName(), select=True)
        PluginPoints.INTERPRETER.Update()
        PluginPoints.MEDIA.AddPage(self.media, self.media.GetName(), select=True)
        PluginPoints.MEDIA.Update()
    def OnNewProject(self, evt):
        if self.IsCurrent():
            print 'new project', self.__class__.__name__
        evt.Skip()

PluginPoints.SecureRegister('"S&QLiteYarn"[CTRL+Q](As UI for SQLite.)<>', SQLiteYarn)
