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
from common.fsoperate import FileName
from config.constants import *
from drivers import *

class SQLiteYarnTreeViewHome(TreeViewHome):
    def __init__(self, parent, root):
        TreeViewHome.__init__(self, parent, root)
        EM.eventManager.Register(self.OnOptions, OPTIONS_BD, self.GetParent())
#         EM.eventManager.Register(self.OnNodeActivated, NODE_ACTIVATED_BD, self.GetParent())
    def OnOpen(self):
        TreeViewHome.OnOpen(self)
        Database.DB = Database(self.selected)
#         Database.DB.SQL('CREATE TABLE MOVIE (NUMBER INT, NAME TEXT);')
#         Database.DB.SQL('INSERT INTO MOVIE VALUES (9527, "ZXC");')
#         Database.DB.SQL('SELECT * FROM TEST;')
        Database.DB.SQL('select name from sqlite_master where type="table" order by name;')
        root = self.GetUserData(self.GetRoot())
        self.SetUserText(self.GetRoot(), FileName(self.selected))
        for tbl in Database.DB.List():
            node = Node(tbl[First])
            root.AppendKid(node)
        self.AddItems(self.GetRoot(), root.GetKids())
#     def OnNodeActivated(self, evt):
#         print evt.GetClientData()

class SQLiteYarnDatabase(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeOptions(self):
        return TreeViewOptions(self)
    def MakeTree(self):
        return SQLiteYarnTreeViewHome(self, Node('Node'))
    #TODO: BEGIN 覆盖父类方法
    #实现同消息转发同样的效果
#     def OnButton(self, evt):
#         print self.__class__.__name__
    def OnNodeActivated(self, evt):
        self.reference['m'].Clear()
        item = evt.GetItem()
        name = self._2sz_tree_pane._2sz__tree.GetItemText(item)
        info = Database.DoesTableExist(name)
        if not info:return
        for c, datum in enumerate(info):
            _, f, t, _, _, _ = datum
            self.reference['m'].SetColLabel(c, '%s:%s' % (f, t))
        Database.DB.SQL('SELECT * FROM %s;' % name)
        for r, record in enumerate(Database.DB.List()):
            for c, cell in enumerate(record):
                self.reference['m'].SetCell(r, c, unicode(cell))
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
    def OnNewProject(self, evt):
        if self.IsCurrent():
            pass
        evt.Skip()

PluginPoints.SecureRegister('"!S&QLiteYarn"[CTRL+Q](As UI for SQLite.)<>', SQLiteYarn)
