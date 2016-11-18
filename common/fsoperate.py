#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import os

def MakeBasePath():
    return os.path.dirname(os.path.dirname(__file__))

def JoinPath(*args):
    return os.path.join(*args)

def DoesExist(path):
    return os.path.exists(path)

def IsFolder(path):
    return os.path.isdir(path)

def IsFile(path):
    return os.path.isfile(path)

def IsAbsolutePath(path):
    return os.path.isabs(path)

def MakeAbsolutePath(relativepath):
    return os.path.abspath(relativepath)

def ListPath(path):
    ret = {'files': [], 'folders': []}
    if IsFile(path):
        ret['files'].append(path)
        return ret
    elif IsFolder(path):
        things = os.listdir(path)
        for thing in things:
            _path = JoinPath(path, thing)
            if IsFolder(_path):
                ret['folders'].append(thing)
            else:
                assert IsFile(_path)
                ret['files'].append(things)
    return ret

def ChangeWorkPath(path):
    if IsFolder(path):
        os.chdir(path)
        return True
    else:
        return False

def MakePath(path):
    if not DoesExist(path):
        os.makedirs(path)

def RmvPath(path):
    if IsFolder(path):
        os.removedirs(path)
    elif IsFile(path):
        os.remove(path)
    else:
        return False
    return True

class FSOperate:
    def __init__(self):
        pass
    def Open(self):
        pass
    def Close(self):
        pass
    def Save(self):
        pass
    def SaveAs(self, path):
        pass
    def OverWrteAlert(self):
        pass
    def Delete(self):
        pass






