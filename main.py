#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/06/02
@Author  :   Yaronzz
@Version :   1.0
@Contact :   yaronhuang@foxmail.com
@Desc    :   
'''
import json
import os

def getFileSize(path):
    try:
        if os.path.isfile(path) is False:
            return 0
        return os.path.getsize(path)
    except:
        return 0


def getFileContent(path, isBin=False):
    mode = 'r'
    if isBin:
        mode = 'rb'
    try:
        size = getFileSize(path)
        if size <= 0:
            return ""
        with open(path, mode, encoding='utf-8', errors='ignore') as fd:
            content = fd.read(size)
        return content
    except Exception as e:
        return ""


def write(path, content, mode):
    try:
        with open(path, mode, encoding="utf-8") as fd:
            fd.write(content)
        return True
    except Exception as e:
        return False

oCN = getFileContent("OLD_CN.json")
oEN = getFileContent("CUR_EN.json")
oCN = json.loads(oCN)
oEN = json.loads(oEN)

for item in oEN:
    if item in oCN:
        oEN[item] = oCN[item]

content = json.dumps(oEN, ensure_ascii=False)
write("messages.json", content, 'w')



