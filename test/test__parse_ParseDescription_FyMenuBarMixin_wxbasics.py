#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

#TODO: ��ηǵݹ�Ľ����������˵��Ķ���

from config.constants import NotFound

#������ʽ����
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
