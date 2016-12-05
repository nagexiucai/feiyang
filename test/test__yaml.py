#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: nagexiucai
@license: gpl
'''

import yaml
from common.fsoperate import MakeBasePath, JoinPath
config = file(JoinPath(MakeBasePath(), 'resources', 'devops.yaml'))
data = config.read()
config.close()
data = yaml.load(data)
print 'y2py return type', type(data)
print yaml.dump(data)
