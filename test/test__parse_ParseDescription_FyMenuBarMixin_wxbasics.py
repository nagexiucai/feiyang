#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

#TODO: 如何非递归的解决任意层数菜单的定制

from config.constants import NotFound

#正则表达式修正
import re
ReXMMenu = re.compile('#([^#]*?):\{(.*?)\}#[^#]')

def parse(ustr):
    sections = ReXMMenu.findall(ustr)
    for item, ustr in sections:
        if ustr.find(':') != NotFound:
            yield item, True
            ustr = ustr.replace('##', '#')
            parse(ustr)
        else:
            yield item, True
            yield ustr, False

ustr = '''
       #"&File"[]()<normal>:{
           ##"&New"[CTRL+N](Build Something To Operate.)<normal>:{
               ###"&Project"[]()<>"&Text"[]()<>"&Binary"[]()<>}
           ##"Save&As"[]()<>:{}}
       #"&Edit"[]()<normal>:{}
       #"|"[]()<|>:{}
       #"Plug&Ins"[]()<normal>:{}
       #"|"[]()<|>:{}
       #"&Help"[]()<normal>:{}
       '''

for title, status in parse(ustr.replace('\n', '').replace(' ', '').replace('    ', '')):
    print title, status
