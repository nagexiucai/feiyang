#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: nagexiucai
@license: gpl
@url: www.thisstack.com
'''

#TODO: 实现在Windows上针对Openstack的远程DevOps
#DevOps
#    |-Deploy
#        |-Install
#        |-Version Update
#        |-Module Orchestrate
#    |-Monitor
#        |-Status
#        |-Log
#        |-Alarm
#    |-CI(Continious Integrate)
#        |-Source Code
#        |-Test
#        |-Package
#        |-Commit
#        |-Bug Trace
#以上便是个人对DevOps的理解

from plugins import PluginPoints
from widgets.treeviews import TreeView, TreeViewHome
from widgets.wxbasics import FyLayoutMixin
from common.node import Node
from config.constants import *

class Deploy:
    def Install(self):pass
        #在任意主机启动vm（2CPU/4GB-RAM/60G-DISK/Bridged-Network/SSH）
        #在此vm上安装all-in-one（开启本地安装包缓存）
        #以此vm上的安装包缓存创建本地源
        #配置其余远程主机到该本地源
        #根据各远程主机的角色安排分别安装

class Cluster(TreeView):
    def MakeOptions(self):
        class Options(FyLayoutMixin):pass
        return Options(self)
    def MakeTree(self):
        class CrossDevOpsTreeViewHome(TreeViewHome):pass
        return CrossDevOpsTreeViewHome(self, Node('Test'))
class Message(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        class Options(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
                self.aspect = self._horizental
                self._2sz_deploy = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Deploy'), Auto
                self._2sz_monitor = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Monitor'), Auto
                self._2sz_ci = wx.Button(self, size=(DefaultButtonWidth, Auto), label='CI'), Auto
                self.FyLayout()
        self._2sz_options = Options(self), Fixed
        class Filters(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
        self._2sz_filters = Filters(self), Fixed
        class Bill(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
        self._2sz_bill = Bill(self), Auto
        self.FyLayout()
class Dashboard(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        class Options(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
                self.aspect = self._horizental
                self._2sz_load = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Load'), Auto
                self._2sz_save = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Save'), Auto
                self.FyLayout()
        self._2sz_options = Options(self), Fixed
        class Config(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
                self._2sz_properties = PPG.PropertyGridManager(self, style=PPG.PG_TOOLBAR|PPG.PG_AUTO_SORT), Auto
                self.FyLayout()
        self._2sz_config = Config(self), Auto
        self.FyLayout()
        self.Bind(wx.EVT_BUTTON, self.OnOptions)
        self.Bind(PPG.EVT_PG_CHANGED, self.OnPropertyChanged)
        self.Bind(PPG.EVT_PG_PAGE_CHANGED, self.OnPropertyPageChanged)
    def OnOptions(self, evt):
        act = self.FindWindowById(evt.GetId()).GetLabel()
        if 'Load' == act:
            pass
    def OnPropertyChanged(self, evt):pass
    def OnPropertyPageChanged(self, evt):pass

class CrossDevOps(PluginPoints):
    def __init__(self):
        PluginPoints.__init__(self)
    def MustBeCustomized(self):
        self.explorer = Cluster(PluginPoints.EXPLORER)
        self.explorer.SetName('Cluster')
        self.interpreter = Message(PluginPoints.INTERPRETER)
        self.interpreter.SetName('Message')
        self.media = Dashboard(PluginPoints.MEDIA)
        self.media.SetName('Dashboard')

PluginPoints.SecureRegister('"!Cross&DevOps"[CTRL+D](As UI for DevOps.)<>', CrossDevOps)
