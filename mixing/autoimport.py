#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

# __import__(name, globals={}, locals={}, fromlist=[], level=-1) -> module
# 
# Import a module.
# Because this function is meant for use by the Python interpreter
# and not for general use
# it is better to use importlib.import_module() to programmatically import a module.
# 
# The globals argument is only used to determine the context; they are not modified.
# The locals argument is unused.
# The fromlist should be a list of names to emulate 'from name import ...',
# or an empty list to emulate 'import name'.
#   When importing a module from a package, note that __import__ ('A.B', ...)
#   returns package A when fromlist is empty,
#   but its submodule B when fromlist is not empty.
# level is used to determine whether to perform absolute or relative imports.
#   -1 is the original strategy of attempting both absolute and relative imports,
#   0 is absolute,
#   a positive number is the number of parent directories to search relative to the current module.

import sys
from common.fsoperate import MakeBasePath, JoinPath
PLUGINS = JoinPath(MakeBasePath(), 'plugins')
sys.path.append(PLUGINS)

#TODO: 实现监控指定目录下脚本的改动并重新加载
from plugins.utils.sqliteyarn import SQLiteYarn
from plugins.utils.crossdevops import CrossDevOps
