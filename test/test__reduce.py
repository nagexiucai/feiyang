#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

def xiucai(a, b):
    print a,b
    return a + '|' + b

# babies = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
# print reduce(xiucai, babies)

def nagexiucai(*args):
#     print reduce(xiucai, args) #xiucai后续一直用历史结果替代第一个入参
    print reduce(lambda a,b: a+'|'+b, args)
nagexiucai('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
