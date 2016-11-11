#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from config.constants import *

class Node:
    def __init__(self, name, level=0):
        self.__name = name
        self.__level = level
        self.__parent = None
        self.__kids = []
        self.__attributes = {}
    def GetName(self):
        return self.__name
    def GetLevel(self):
        return self.__level
    def SetParent(self, parent):
        self.__parent = parent
    def GetKids(self):
        return self.__kids
    def GetAttribute(self, attr):
        return self.__attributes.get(attr)
    def AppendKid(self, kidnode):
        self.__kids.append(kidnode)
    def SetAttribute(self, k, v):
        self.__attributes[k] = v
    def __str__(self):
        template = ' '.join(map(lambda key: '%s="%%(%s)s"' % (key, key), self.__attributes.keys()))
        attributes = template % self.__attributes
        indent = ' '*4*self.__level
        kids = ''.join(['%s' % kid for kid in self.__kids])
        if kids:
            return '\n%s<%s %s>%s\n%s</%s>' % (indent, self.__name, attributes, kids, indent, self.__name)
        else:
            return '\n%s<%s %s />' % (indent, self.__name, attributes)
    __unicode__ = __str__
    def __repr__(self):
        return self.__name
    def __nonzero__(self):
        return self.__kids and self.__attributes
    def __len__(self):
        return len(self.__kids) if len(self.__kids) >= len(self.__attributes) else len(self.__attributes)

def _CalculateIndent(ustr):
    return len(ustr) - len(ustr.lstrip())
cnt = 0
def StructuredByIndent2NodeTree(lines, node): #TODO: 广度优先BFS（Breadth First Search）
    #深度优先DFS（Depth-First Traversal）
    while True:
        try:
            line = lines.pop(0)
        except IndexError: #EOF
            return None
        name = line.strip()
        if name:
            break
    newnode = Node(name, _CalculateIndent(line)) #包装新节点newnode
    if newnode.GetLevel() > node.GetLevel(): #新节点newnode是老起点节点node的晚辈
        node.AppendKid(newnode) #老起点节点node添加以新节点newnode为根节点的子树（当前还仅是亚根节点，须待递归结束）
        while True: #获取新节点newnode下的森林（多棵树）
            x = StructuredByIndent2NodeTree(lines, newnode) #以此新节点newnode为新起点递归，获得起点节点以下的子树根节点X
            if x is None: #文本处理完
                break
            if x.GetLevel() > newnode.GetLevel():
                newnode.AppendKid(x)
            elif x.GetLevel() == newnode.GetLevel(): #X节点和新节点newnode是同辈，则是老起点节点node的晚辈
                node.AppendKid(x) #老起点节点node添加晚辈节点
                newnode = x #同辈节点X已经添加，此后换此同辈节点X做新起点递归！
            elif x.GetLevel() <= node.GetLevel(): #若新节点newnode层级等于或高于老起点节点node，必须退回上层谋求处理！
                return x
    else:
        return newnode #返回老起点节点node的长辈或同辈newnode

def UString2Node(ustr=None):
    '''
    HuaLingson's PC
        Desktop
            MyDocuments
                Pictures
                Musics
            MyDB
        Disk C
            operate system
            applications
                feiyang
                
                preadsheetx
        Disk D
            works
            diaries
        Disk E
        Disk F
        
        Disk G
    '''
    if ustr is None:
        ustr = UString2Node.__doc__
    lines = ustr.split('\n')
    root = Node('Root', Smallest)
    StructuredByIndent2NodeTree(lines, root)
    return root
