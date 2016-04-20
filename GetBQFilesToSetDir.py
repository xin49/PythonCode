# -*- coding: utf-8 -*-
import os
import shutil
import glob
from shutil import copytree, ignore_patterns

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name.decode('utf-8') in files:
            result.append(os.path.join(root, name))
        else:
            result.extend('1.bmp')
    return result

def getfiletopath(Path):
    dstdir = Path
    findresult = glob.glob('.\*' + dstdir.decode('utf-8') + '*.bmp')
    for Idx in range(len(findresult)):
        shutil.copy(findresult[Idx], dstdir.decode('utf-8'))
        Idx = Idx + 1;

Path1 = '正常'
Path2 = '漏墨'
Path3 = '缺墨'
Path4 = '未定义'
Path5 = '未找到'
Path6 = '断线'
if not os.path.exists(Path1.decode('utf-8')):
    os.mkdir(Path1.decode('utf-8'))
if not os.path.exists(Path2.decode('utf-8')):
    os.mkdir(Path2.decode('utf-8'))
if not os.path.exists(Path3.decode('utf-8')):
    os.mkdir(Path3.decode('utf-8'))
if not os.path.exists(Path4.decode('utf-8')):
    os.mkdir(Path4.decode('utf-8'))
if not os.path.exists(Path5.decode('utf-8')):
    os.mkdir(Path5.decode('utf-8'))
if not os.path.exists(Path6.decode('utf-8')):
    os.mkdir(Path6.decode('utf-8'))

getfiletopath(Path1)
getfiletopath(Path2)
getfiletopath(Path3)
getfiletopath(Path4)
getfiletopath(Path5)
getfiletopath(Path6)


#because in windows file and path operation 
#with ansii coding so when we need operation file need use ansii coding 
#utf-8 --> decode(utf-8)
