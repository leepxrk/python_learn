#!/usr/bin/python
# -*- coding: UTF-8 -*-


（1）主程序与模块程序在同一目录下:
如下面程序结构:
`-- src
    |-- mod1.py
    `-- test1.py
    若在程序test1.py中导入模块mod1, 则直接使用import mod1或from mod1 import *;

（2）主程序所在目录是模块所在目录的父(或祖辈)目录
如下面程序结构:
`-- src
    |-- mod1.py
    |-- mod2
    |   `-- mod2.py
    `-- test1.py
    若在程序test1.py中导入模块mod2, 需要在mod2文件夹中建立空文件__init__.py文件(也可以在该文件中自定义输出模块接口); 然后使用 from mod2.mod2 import * 或import mod2.mod2.

（3）主程序导入上层目录中模块或其他目录(平级)下的模块
如下面程序结构:
`-- src
    |-- mod1.py
    |-- mod2
    |   `-- mod2.py
    |-- sub
    |   `-- test2.py
    `-- test1.py
    若在程序test2.py中导入模块mod1和mod2。首先需要在mod2下建立__init__.py文件(同(2))，src下不必建立该文件。然后调用方式如下:
   下面程序执行方式均在程序文件所在目录下执行，如test2.py是在cd sub;之后执行python test2.py
而test1.py是在cd src;之后执行python test1.py; 不保证在src目录下执行python sub/test2.py成功。
   import sys
   sys.path.append("..")
   import mod1
   import mod2.mod2