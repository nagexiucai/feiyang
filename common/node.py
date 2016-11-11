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
def StructuredByIndent2NodeTree(lines, node): #TODO: �������BFS��Breadth First Search��
    #�������DFS��Depth-First Traversal��
    while True:
        try:
            line = lines.pop(0)
        except IndexError: #EOF
            return None
        name = line.strip()
        if name:
            break
    newnode = Node(name, _CalculateIndent(line)) #��װ�½ڵ�newnode
    if newnode.GetLevel() > node.GetLevel(): #�½ڵ�newnode�������ڵ�node����
        node.AppendKid(newnode) #�����ڵ�node������½ڵ�newnodeΪ���ڵ����������ǰ�������Ǹ��ڵ㣬����ݹ������
        while True: #��ȡ�½ڵ�newnode�µ�ɭ�֣��������
            x = StructuredByIndent2NodeTree(lines, newnode) #�Դ��½ڵ�newnodeΪ�����ݹ飬������ڵ����µ��������ڵ�X
            if x is None: #�ı�������
                break
            if x.GetLevel() > newnode.GetLevel():
                newnode.AppendKid(x)
            elif x.GetLevel() == newnode.GetLevel(): #X�ڵ���½ڵ�newnode��ͬ�������������ڵ�node����
                node.AppendKid(x) #�����ڵ�node������ڵ�
                newnode = x #ͬ���ڵ�X�Ѿ���ӣ��˺󻻴�ͬ���ڵ�X�������ݹ飡
            elif x.GetLevel() <= node.GetLevel(): #���½ڵ�newnode�㼶���ڻ���������ڵ�node�������˻��ϲ�ı����
                return x
    else:
        return newnode #���������ڵ�node�ĳ�����ͬ��newnode

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
