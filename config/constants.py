#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

__mark__ = 'FeiYang'
__version__ = '0.1.0'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os
from pprint import pprint as PP
import uuid
import traceback
START_PATH = os.getcwdu()
RESOURCES_ROOT = os.path.join(START_PATH, 'resources')
APPLICATION_LOG_PATH = os.path.join(START_PATH, 'FeiYang.error')
APPLICATION_NAME_VERSION = '%s V%s' % (__mark__, __version__)

import wx
wx.SetDefaultPyEncoding('utf-8')
import wx.lib.evtmgr as EM
import wx.propgrid as PPG


#Walk Round
#begin: BUG——初始化时创建好
InitRowCount = 99
InitColumnCount = 26
#end

#System
DEBUG = True
IdBase = wx.NewId()
Smallest = None
NEWLINE = os.linesep
UUID = lambda: unicode(uuid.uuid1())

#Framework Event
ONLY_INNER = 0
CAN_LISTEN_ONE_SOURCE = 1
CAN_LISTEN_SOURCE_RANGE = 2
NEW_PROJECT = wx.NewEventType()
NEW_PROJECT_BD = wx.PyEventBinder(NEW_PROJECT, CAN_LISTEN_ONE_SOURCE)

# Bind(EventTypeBD, method, source/{id}) @ WhoCatchesTheEvent
# event = wx.PyCommandEvent(EventType, IdForWhoMakeTheEvent) @ WhereGenerateTheEvent #TODO: should travel up to parent windows looking for a handler
# wx.PostEvent(wx.Window/wx.EvtHandler, event) @ WhereEver
# GetEventHandler().ProcessEvent(event)
# 
# wx.lib.evtmgr.eventManager
# Invoke any of the following methods.
# These methods are 'safe'; duplicate registrations or de-registrations will have no effect.
# Registering a listener:
#   EventManager.Register(listener, event, source)
# De-registering by window:
#   EventManager.DeregisterWindow(event-source)
# De-registering by listener:
#   EventManager.DeregisterListener(listener)
# 
# EventManager.Register(listener, event, source, win, id)
# listener can be any callable object.
# win for specific where the event is delivered; id of event source.

OPTIONS = wx.NewEventType()
OPTIONS_BD = wx.PyEventBinder(OPTIONS, CAN_LISTEN_ONE_SOURCE)
#begin: used for comparing message transmission & method override
# NODE_ACTIVATED = wx.NewEventType()
# NODE_ACTIVATED_BD = wx.PyEventBinder(NODE_ACTIVATED, CAN_LISTEN_ONE_SOURCE)
#end

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
DefaultButtonWidth = 20

#Built-in Widgets ID
