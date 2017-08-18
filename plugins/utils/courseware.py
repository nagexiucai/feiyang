#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from config.constants import *
from plugins import PluginPoints
from widgets.wxbasics import FyLayoutMixin, FyMenuMixin
from widgets.treeviews import TreeView, TreeViewHome
from widgets.texteditor import Editor, Board
from widgets.imagengine import ImageBox
from widgets.popups import TextEntry
from widgets.clipboard import GetClipboard
from common.node import Node
from common.fsoperate import JoinPath
from drivers.msword import MSWord

class CourseWareTreeViewHome(TreeViewHome):
    def __init__(self, parent, root):
        TreeViewHome.__init__(self, parent, root)
        EM.eventManager.Register(self.OnOptions, OPTIONS_BD, self.GetParent())
    def OnDumping(self):
        def NewImagePath(suffix):
            return JoinPath(RESOURCES_ROOT, 'pictures', UUID()) + suffix
        def R(t, i):
            item, cookie = self._2sz__tree.GetFirstChild(t)
            while item.IsOk():
                caption = self.GetUserText(item)
                data = self.GetUserData(item)
                picture = data.GetAttribute('picture')
                explain = data.GetAttribute('explain')
                if picture.IsOk(): #IsNull
                    jpeg = NewImagePath('.jpeg')
                    picture.SaveFile(jpeg, wx.BITMAP_TYPE_JPEG)
                else:
                    jpeg = None
#                 itemtext = u'├─%s[%d] %s "%s" {%s}' % ('─'*i, i, caption, jpeg, explain)
#                 yield itemtext
                yield (i, caption, jpeg, explain)
                if self._2sz__tree.GetChildrenCount(item):
                    i+=1
                    for _ in R(item, i):
                        yield _
                    i-=1
                item, cookie = self._2sz__tree.GetNextChild(item, cookie)
        those = []
        root = self.GetRoot()
        name = self.GetUserText(root)
        rootdata = self.GetUserData(root)
        logo = rootdata.GetAttribute('picture', wx.NullBitmap)
        if logo.IsOk():
            logopath = NewImagePath('.jpeg')
            logo.SaveFile(logopath, wx.BITMAP_TYPE_JPEG)
        else:
            logopath = None
        tips = rootdata.GetAttribute('explain')
        i = 0
#         print u'┌', name
        those.append((i, name, logopath, tips))
        for _ in R(root, i):
#             print _
            those.append(_)
#         PP(those)
        mw = MSWord()
        out = JoinPath(RESOURCES_ROOT, name) + '.docx'
        mw.CreateDocx(those, out)

class CourseWarePopupMenu(FyMenuMixin):
    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        self.switch = None
        self.Bind(wx.EVT_MENU, self.OnMenu)
        self.ParseDescription('"Renamed"[](Text Things.)<>"|"[]()<|>"Subject"[](Paragraph Things.)<>')
    def OnMenu(self, evt):
        self.switch = self.FindItemById(evt.GetId()).GetLabel()

class CourseWareSection(TreeView):
    def __init__(self, parent):
        TreeView.__init__(self, parent)
    def MakeOptions(self):
        class CourseWareSectionOption(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
                self._2sz_dumping = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Dumping'), Fixed
                self.FyLayout()
        return CourseWareSectionOption(self)
    def MakeTree(self):
        return CourseWareTreeViewHome(self, Node('manual'))
    def OnNodeActivated(self, evt):
        item = evt.GetItem()
#         self._2sz_tree_pane.GetUserText(item)
        node = self._2sz_tree_pane.GetUserData(item)
        self.GangedMedia(node, node)
    def OnNodeMenu(self, evt):
        popup = CourseWarePopupMenu(self)
        self.PopupMenu(popup, evt.GetPoint())
        try:
            assert popup.switch in ('Renamed', 'Subject')
        except AssertionError:pass
        else:
            item = evt.GetItem()
            if popup.switch == 'Subject':
                name = TextEntry(self, 'Give new section a name', 'Caption')
#                 name = name.decode('utf-8').encode('gbk') #XXX: 通过wx.SetDefaultPyEncoding做了全局配置 
                if name:
                    node = Node(name)
                    self._2sz_tree_pane.AddItems(item, (node,))
#                     self.GangedMedia(node, node) #XXX: 在AddItems调用中触发OnHover已经都做过[保存]刷新
            if popup.switch == 'Renamed':
                name = TextEntry(self, 'Give section a new name', 'Caption')
                if name:
                    self._2sz_tree_pane.SetUserText(item, name)
                    node = self._2sz_tree_pane.GetUserData(item)
                    node.SetName(name)
#                     self.GangedMedia(node, node) #XXX: 名称已经修改并保存
        finally:
            popup.Destroy()
    def OnHover(self, evt):
        nodepre = self._2sz_tree_pane.GetUserData(evt.GetOldItem())
        nodecur = self._2sz_tree_pane.GetUserData(evt.GetItem()) #XXX: 没有设置PyData的TreeItem默认所绑定的PyData为None
        self.GangedMedia(nodepre, nodecur)
    def GangedMedia(self, prenode, curnode):
        #参数curnode：展示
        #参数prenode：保存
        #TODO: 监控数据是否发生变化以及只更新变化的部分
        if prenode is not None:
            picture = self.reference['m']._2sz_picture.GetImage()
            explain = self.reference['m']._2sz_explain.GetContent()
            prenode.SetAttribute('picture', picture)
            prenode.SetAttribute('explain', explain)
        #把现场保存到上一时刻的节点中
        #用当前时刻节点的内容刷新现场
        if curnode is not None:
            picture = curnode.GetAttribute('picture', wx.NullBitmap)
            self.reference['m']._2sz_picture.ChangeImage(picture)
            self.reference['m'].sizer.Layout()
            explain = curnode.GetAttribute('explain', 'nothing')
            self.reference['m']._2sz_explain.SetContent(explain)

class CourseWareComposer(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        class CourseWareComposerOption(FyLayoutMixin):
            def __init__(self, parent):
                FyLayoutMixin.__init__(self, parent)
                self._2sz_import = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Import'), Auto
                self._2sz_export = wx.Button(self, size=(DefaultButtonWidth, Auto), label='Export'), Auto
                self.aspect = FyLayoutMixin._horizental
                self.FyLayout()
        self._2sz_command = CourseWareComposerOption(self), Fixed
        self._2sz_picture = ImageBox(self), Auto
        self._2sz_explain = Editor(self), Auto
        self._2sz_explain.SetContent('nothing')
        self.FyLayout()
        self.Bind(wx.EVT_BUTTON, self.OnCommand)
    def OnCommand(self, evt):
        inout = self.FindWindowById(evt.GetId()).GetLabel()
        if inout == 'Import':
            self._2sz_picture.ChangeImage(GetClipboard('bmp'))
            self.sizer.Layout()

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
