#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from plugins import M, PluginPoints
from widgets.grids import SimpGridView
from widgets.treeviews import TreeView, TreeViewHome
from common.node import Node

class SQLiteYarn(M):
    def __init__(self):
        M.__init__(self)
        self.database = TreeView(PluginPoints.EXPLORER)
        self.table = SimpGridView(PluginPoints.MEDIA)
    def Plugin(self):
        PluginPoints.EXPLORER.AddPage(self.database, 'database', select=True)
        PluginPoints.MEDIA.AddPage(self.table, 'table', select=True)

PluginPoints.SecureRegister('"S&QLiteYarn"[CTRL+Q](As UI for SQLite.)<>', SQLiteYarn)
