#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

from widgets.wxbasics import FyLayoutMixin

class ImageBox(FyLayoutMixin):
    def __init__(self, parent):
        FyLayoutMixin.__init__(self, parent)
        self.FyLayout()
