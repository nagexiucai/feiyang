#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from wxbasics import FyLayoutMixin
from config.constants import *

class TextAttribute(wx.TextAttr):
    def __init__(self):
        wx.TextAttr.__init__(self)
    def Set(self):
        pass

class Text(wx.TextCtrl):
    __styles = {
                'poor': wx.TE_RICH, 
                'rich': wx.TE_RICH2, 
                'readonly': wx.TE_READONLY, 
                'multiline': wx.TE_MULTILINE, 
                'autoscroll': wx.TE_AUTO_SCROLL, 
                'novscroll': wx.TE_NO_VSCROLL, 
                'autourl': wx.TE_AUTO_URL, 
                'capitalize': wx.TE_CAPITALIZE, 
                'left': wx.TE_LEFT, 
                'right': wx.TE_RIGHT, 
                'center': wx.TE_CENTER, 
                'centre': wx.TE_CENTRE, 
                'bestwrap': wx.TE_BESTWRAP, 
                'linewrap': wx.TE_LINEWRAP, 
                'wordwrap': wx.TE_WORDWRAP, 
                'charwrap': wx.TE_CHARWRAP, 
                'nonwrap': wx.TE_DONTWRAP, 
                'htbefore': wx.TE_HT_BEFORE, 
                'htbelow': wx.TE_HT_BELOW, 
                'htbeyond': wx.TE_HT_BEYOND, 
                'htontext': wx.TE_HT_ON_TEXT, 
                'htunknown': wx.TE_HT_UNKNOWN, 
                'nonhidenselection': wx.TE_NOHIDESEL, 
                'password': wx.TE_PASSWORD, 
                'processenter': wx.TE_PROCESS_ENTER, 
                'processtab': wx.TE_PROCESS_TAB
                }
    __nonstyle = 0
    def __init__(self, parent, *styles, **kws):
        wx.TextCtrl.__init__(self, parent, style=self._StyleGenerator(styles))
        self.SetName(kws.get('name', wx.TextCtrlNameStr))
        self.SetValidator(kws.get('validator', wx.DefaultValidator))
        self.SetValue(kws.get('value', wx.EmptyString))
    def _StyleGenerator(self, styles):
        return reduce(lambda a, b: self.__styles.get(a, self.__nonstyle)|self.__styles.get(b, self.__nonstyle), styles)
    def _TextAttributeGenerator(self, style):
        if not style:
            self.__nonstyle
        return TextAttribute(**style)
    def Set(self, **kws):
        value = kws.get('value')
        style = kws.get('style')

class Editor(FyLayoutMixin):
    #两层（底层——图案；顶层——符号）
    #TODO: 如何实现窗口透视同时不影响编辑
    __syntax_hight_light_set = {
                                'python': Ellipsis, 
                                'c': Ellipsis, 
                                'c++': Ellipsis, 
                                'java': Ellipsis, 
                                'javascript': Ellipsis, 
                                'ruby': Ellipsis, 
                                'php': Ellipsis
                                }
    def __init__(self, parent, content_type='text'):
        FyLayoutMixin.__init__(self, parent)
        self._2sz_paper = Text(self, 'rich', 'multiline', 'autoscroll', 'bestwrap', 'autourl', 'left'), Auto
        self.__content_type = type
        self.FyLayout()
    def SetContent(self, content):
        pass
    def GetContent(self):
        pass
