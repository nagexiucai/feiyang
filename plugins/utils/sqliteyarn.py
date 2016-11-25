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
from drivers import *

class SQLiteYarnTreeViewHome(TreeViewHome):
    def __init__(self, parent, root):
        TreeViewHome.__init__(self, parent, root)
        EM.eventManager.Register(self.OnOptions, OPTIONS_BD, self.GetParent())
        EM.eventManager.Register(self.OnNodeActivated, NODE_ACTIVATED_BD, self.GetParent())
    def OnOpen(self):
        TreeViewHome.OnOpen(self)
        self.db = Database(self.selected)
#         self.db.SQL('CREATE TABLE MOVIE (NUMBER INT, NAME TEXT);')
#         self.db.SQL('INSERT INTO MOVIE VALUES (9527, "ZXC");')
#         self.db.SQL('SELECT * FROM TEST;')
#         self.db.SQL('select name from sqlite_master where type="table" order by name;')
        self.db.SQL('PRAGMA table_info(TEST)')
        root = self.GetUserData(self.GetRoot())
        for tbl in self.db.List():
            node = Node(','.join([str(_) for _ in tbl]))#Node(tbl[First])
            root.AppendKid(node)
        self.AddItems(self.GetRoot(), root.GetKids())
    def OnNodeActivated(self, evt):
        print evt.GetClientData()

class SQLiteYarnDatabase(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeOptions(self):
        return TreeViewOptions(self)
    def MakeTree(self):
        return SQLiteYarnTreeViewHome(self, Node('Node'))
    #TODO: BEGIN 覆盖父类方法
    #实现同消息转发同样的效果
    def OnButton(self, evt):
        print self.__class__.__name__
#     def OnNodeActivated(self, evt):
#         print self.__class__.__name__
    #END 覆盖父类方法

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
