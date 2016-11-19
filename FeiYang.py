#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

__mark__ = 'FeiYang'
__version__ = '0.0.1'

import wx.aui
import sys
import os
from config.constants import *

START_PATH = os.getcwdu()
RESOURCES_ROOT = os.path.join(START_PATH, 'resources')
APPLICATION_LOG_PATH = os.path.join(START_PATH, 'FeiYang.error')
APPLICATION_NAME_VERSION = '%s V%s' % (__mark__, __version__)

from mixing.autoimport import *
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
        self.AddPane(self.__fyinterpreter, Editor(self.__fyinterpreter), title='Console')
        self.AddPane(self.__fymedia, Editor(self.__fymedia), title='Paper')
    def AddPane(self, target, pane, **kws):
        target.AddPage(pane, kws.get('title', 'pane'))
        target.Update()
    def EvtBind(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_MENU, self.OnMenu)
        self.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.Cascade)
        self.Bind(NEW_PROJECT_BD, self.OnCommandDefault)
    def OnCommandDefault(self, evt):
        print 'command default'
    def OnClose(self, evt):
        self.Destroy()
    def RedirectStdIO(self, stdin, stdout, stderr):pass
        #TODO: 将标准流定向到Console窗口
    def Cascade(self, evt):
        #TODO: 减少代码行数实现同样的逻辑
        #NotFound: 插件的三模块每加载一个都会触发wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED并执行此方法，导致尚未加载完成的模块找不到
        #print evt.GetSelection(), evt.GetOldSelection()
        if evt.GetEventObject().GetId() == self.__fyexplorer.GetId():
            cp = self.__fyexplorer.GetCurrentPage()
            if not hasattr(cp, 'reference'):
                return
            e = cp.reference.get('e')
            if e and cp.GetId() == e.GetId():
                i = cp.reference.get('i')
                if i:
                    n = self.__fyinterpreter.GetPageIndex(i)
                    if n != NotFound:
                        self.__fyinterpreter.SetSelection(n)
                m = cp.reference.get('m')
                if m:
                    n = self.__fymedia.GetPageIndex(m)
                    if n != NotFound:
                        self.__fymedia.SetSelection(n)
                return
        elif evt.GetEventObject().GetId() == self.__fyinterpreter.GetId():
            cp = self.__fyinterpreter.GetCurrentPage()
            if not hasattr(cp, 'reference'):
                return
            i = cp.reference.get('i')
            if i and cp.GetId() == i.GetId():
                e = cp.reference.get('e')
                if e:
                    n = self.__fyexplorer.GetPageIndex(e)
                    if n != NotFound:
                        self.__fyexplorer.SetSelection(n)
                m = cp.reference.get('m')
                if m:
                    n = self.__fymedia.GetPageIndex(m)
                    if n!= NotFound:
                        self.__fymedia.SetSelection(n)
                return
        elif evt.GetEventObject().GetId() == self.__fymedia.GetId():
            cp = self.__fymedia.GetCurrentPage()
            if not hasattr(cp, 'reference'):
                return
            m = cp.reference.get('m')
            if m and cp.GetId() == m.GetId():
                e = cp.reference.get('e')
                if e:
                    n = self.__fyexplorer.GetPageIndex(e)
                    if n != NotFound:
                        self.__fyexplorer.SetSelection(n)
                i = cp.reference.get('i')
                if i:
                    n = self.__fyinterpreter.GetPageIndex(i)
                    if n != NotFound:
                        self.__fyinterpreter.SetSelection(n)
                return
        evt.Skip()
    def OnMenu(self, evt):
        wid = evt.GetId()
        item = self.GetMenuBar().FindItemById(wid)
        name = item.GetLabel()
        if 'Project' == name:
            event = wx.PyCommandEvent(NEW_PROJECT, self.GetId())
            self.GetEventHandler().ProcessEvent(event)
        try:
            exec('%s().Plugin()' % name) #TODO: 不安全
        except Exception as e:
            print e.message
        else:pass
        finally:pass

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
