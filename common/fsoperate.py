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

def FileName(path):
    return os.path.basename(path)

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

class FSOperate(object):
    TEXT = 'a'
    BINARY = 'ba'
    def Open(self, path, mode=None):
        self.path = path
        self.file = file(path, mode or FSOperate.TEXT)
    def Read(self):
        return self.file.read()
    def LazyRead(self):
        return self.file.xreadlines()
    def Write(self, things):pass
    def Close(self):
        self.file.flush()
        self.file.close()
    def Save(self):pass
    def SaveAs(self, path):pass
    def OverWrteAlert(self):pass
    def Delete(self):pass
    def TransportIntoNodeTree(self, data, whatsit='indent', parser=None):pass #TODO: indent类型就是TreeView的测试数据格式，对应parser是StructuredByIndent2NodeTree
