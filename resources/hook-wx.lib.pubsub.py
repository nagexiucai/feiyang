#!/usr/bin/env python
#coding=utf-8
'''
@author: nagexiucai
@license: gpl
'''

'''
http://www.pythonismus.com/2014/01/pyinstaller-and-pubsub.html

Packing the project into an executable with Pyinstaller (back then at version 1.5.1)
proved to be difficult due to pubsub, which lived in the core of wxPython (back then 2.8.x).
After much perusing the Pyinstaller docs and some try and error approach I ended up
developing a "pyinstaller hook" for the generation of the executable and gave it back (anonymously)
to the community.

import os

def hook(mod):
    pth = str(mod.__path__[0])
    if os.path.isdir(pth):
        mod.__path__.append(os.path.normpath(os.path.join(pth, 'kwargs')))
    return mod

A couple of years later and now Pyinstaller is at version 2.1, wxPython at 3.0.0 and
I use pubsub directly as a library and not the included one in wxPython.
And I hit the same wall once again (even if the aforementioned is "closed")

Luckily and with the experience gained back then and using my own contribution to
the community it was a lot easier and faster to solve my issue:

My hook was for wx.lib.pubsub.core and not for pubsub.core,
Rename the hook from hook-wx.lib.pubsub.core.py to hook-pubsub.core.py

See where I put the code in the Pyinstaller specfile to call the hook,
actually only the path to my own personal "hooks" directory has to be added
Spec file sample

# -*- mode: python -*-
a = Analysis(['src/test.pyw'],
             pathex=['./scripts'],
             hiddenimports=[],
             hookspath=['./scripts/hooks'], # PATH TO THE HOOK
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test.exe',
          debug=False,
          strip=None,
          upx=False,
          console=False )

Notice the "PATH TO THE HOOK" comment

Place the hook code from above with the name "hook-pubsub.core.py" and done
'''

#TODO: 注意开发模式下运行
#查看“Python\Lib\site-packages\wx-3.0-msw\wx\lib\pubsub\core\__init__.py”
#policies.msgDataProtocol
#确认实际使用的pubsub协议（kwargs/arg1）,本例是kwargs

#TODO: 注意需要把“\Python\Lib\site-packages\PyInstaller\building\imphookapi.py”中
#PostGraphAPI的
#self.___path__ = tuple(self.module.packagepath) if self.module.packagepath is not None else None
#改为
#self.___path__ = self.module.packagepath if self.module.packagepath is not None else None
#否则mod.__path__.append报错

#TODO: 注意还需要把“Python\Lib\site-packages\wx-3.0-msw\wx\lib\pubsub\core\kwargs”下的
#六个文件拷贝到“Python\Lib\site-packages\wx-3.0-msw\wx\lib\pubsub\core”下
#datamsg.py
#listenerimpl.py
#publisher.py
#publishermixin.py
#topicargspecimpl.py
#topicmgrimpl.py

import os

def hook(mod):
    pth = str(mod.__path__[0])
    if os.path.isdir(pth):
        # print 'START=====', pth, mod.__path__, type(mod)
        mod.__path__.append(os.path.normpath(os.path.join(pth, 'core', 'kwargs')))
        # print 'END=======', mod.__path__
    return mod
