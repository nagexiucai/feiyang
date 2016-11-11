#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import wx
import re

#System
DEBUG = True
IdBase = wx.NewId()
Smallest = None

#Regular Expression Machine
ReXMMenu = re.compile('"(.*?)"\[(.*?)\]\((.*?)\)<(.*?)>')

#Layout
Horizental = 0
Vertical = 1
Fixed = 0
Auto = -1

#Judge
NotFound = -1
NotHas = 0

#Index
First = 0
Last = -1
MustBeOne = 0

#Pixels
Pix32 = 32
Pix16 = 16

#Default UI
DefaultMainFrameSize = (640, 480)
DefaultExplorerWidth = 300
DefaultExplorerHeight = 100
DefaultInterpreterWidth = 140
DefaultInterpreterHeight = 140
DefaultFyMediaWidth = 320
DefaultFyMediaHeight = 240

#Built-in Widgets ID
IdTreeCollapseAll = IdBase + 1
IdTreeExpandAll = IdBase + 2
IdTreeCollapseThis = IdBase + 3
IdTreeExpandThis = IdBase + 4
