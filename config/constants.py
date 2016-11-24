#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import wx
import wx.lib.evtmgr as EM
import re
import os

#System
DEBUG = True
IdBase = wx.NewId()
Smallest = None
NEWLINE = os.linesep

#Framework Event
ONLY_INNER = 0
CAN_LISTEN_ONE_SOURCE = 1
CAN_LISTEN_SOURCE_RANGE = 2
NEW_PROJECT = wx.NewEventType()
NEW_PROJECT_BD = wx.PyEventBinder(NEW_PROJECT, CAN_LISTEN_ONE_SOURCE)
'''
Bind(EventTypeBD, method, source/{id}) @ WhoCatchesTheEvent
event = wx.PyCommandEvent(EventType, IdForWhoMakeTheEvent) @ WhereGenerateTheEvent #TODO: should travel up to parent windows looking for a handler!
wx.PostEvent(wx.Window/wx.EvtHandler, event) @ WhereEver
GetEventHandler().ProcessEvent(event)

wx.lib.evtmgr.eventManager
Invoke any of the following methods.
These methods are 'safe'; duplicate registrations or de-registrations will have no effect.
Registering a listener:
  EventManager.Register(listener, event, source)
De-registering by window:
  EventManager.DeregisterWindow(event-source)
De-registering by listener:
  EventManager.DeregisterListener(listener)

EventManager.Register(listener, event, source, win, id)
listener can be any callable object.
win for specific where the event is delivered; id of event source.
'''
OPTIONS = wx.NewEventType()
OPTIONS_BD = wx.PyEventBinder(OPTIONS, CAN_LISTEN_ONE_SOURCE)

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
