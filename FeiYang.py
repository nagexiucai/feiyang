#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

__mark__ = 'FeiYang'
__version__ = '0.0.1'

import wx
import wx.aui
import sys
import os
from config.constants import *

START_PATH = os.getcwdu()
RESOURCES_ROOT = os.path.join(START_PATH, 'resources')
APPLICATION_LOG_PATH = os.path.join(START_PATH, 'FeiYang.error')
APPLICATION_NAME_VERSION = '%s V%s' % (__mark__, __version__)

from plugins import PluginPoints
from config.images import PyImage_MainFrame
from widgets.wxbasics import FyMenuBarMixin, FyStatusBarMixin, FyNotebookMixin
from widgets.treeviews import FSTreeView
from widgets.texteditor import Editor

class FyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title)
        self.SetMinSize(DefaultMainFrameSize)
        self.SetIcon(PyImage_MainFrame.GetIcon())
        FyMenuBarMixin(self)
        self.AuiLayout()
        FyStatusBarMixin(self)
        self.EvtBind()
    def AuiLayout(self):
        self.__wmanager = wx.aui.AuiManager(self)
        self.__fyexplorer = FyNotebookMixin(self)
        self.__fyinterpreter = FyNotebookMixin(self)
        self.__fymedia = FyNotebookMixin(self)
        PluginPoints.TOP = self
        PluginPoints.EXPLORER = self.__fyexplorer
        PluginPoints.INTERPRETER = self.__fyinterpreter
        PluginPoints.MEDIA = self.__fymedia
        self.__wmanager.AddPane(self.__fyexplorer, wx.aui.AuiPaneInfo().Name('FyExplorer').Caption('FyExplorer').Left().MinSize((DefaultExplorerWidth, DefaultExplorerHeight)).MaximizeButton().CloseButton(False))
        self.__wmanager.AddPane(self.__fyinterpreter, wx.aui.AuiPaneInfo().Name('FyInterpreter').Caption('FyInterpreter').Bottom().MinSize((DefaultInterpreterWidth, DefaultInterpreterHeight)).MaximizeButton().CloseButton(False))
        self.__wmanager.AddPane(self.__fymedia, wx.aui.AuiPaneInfo().Name('FyMedia').Caption('FyMedia').CenterPane().CaptionVisible().MinSize((DefaultFyMediaWidth, DefaultFyMediaHeight)).MaximizeButton())
        self.__wmanager.Update()
        self.AddPane(self.__fyexplorer, FSTreeView(self.__fyexplorer), title='Directions')
        self.AddPane(self.__fymedia, Editor(self.__fymedia), title='Paper')
    def AddPane(self, target, pane, **kws):
        target.AddPage(pane, kws.get('title', 'pane'))
        target.Update()
    def EvtBind(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_MENU, self.OnMenu)
    def OnClose(self, evt):
        self.Destroy()
    def RedirectStdIO(self, stdin, stdout, stderr):
        pass
    def OnMenu(self, evt):
        wid = evt.GetId()
        item = self.GetMenuBar().FindItemById(wid)
        tag = item.GetText()
        print tag

class FyApp(wx.App):
    def __init__(self, frame):
        self.frame = frame
        wx.App.__init__(self, False, APPLICATION_LOG_PATH)
    def OnInit(self):
        self.frame = self.frame(APPLICATION_NAME_VERSION)
        self.frame.Show()
        self.frame.CenterOnScreen()
        return True
    def RedirectStdIO(self):
        self.frame.RedirectStdIO(sys.stdin, sys.stdout, sys.stderr)
    def OnExit(self):
        return True

class Main:
    hasmain = False
    def __init__(self):
        if Main.hasmain:
            raise
        Main.hasmain = True
        self.__stdin = sys.stdin
        self.__stdout = sys.stdout
        self.__stderr = sys.stderr
    def __del__(self):
        sys.stdin = self.__stdin
        sys.stdout = self.__stdout
        sys.stderr = self.__stderr
    def __call__(self, *args):
        feiyang = FyApp(FyFrame)
        feiyang.RedirectStdIO()
        feiyang.MainLoop()

if __name__ == '__main__':
    Main()(sys.argv)
