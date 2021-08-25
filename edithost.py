#!/usr/bin/env python
# coding=utf-8

'''
修改host文件
原载:https://blog.csdn.net/skylibiao/article/details/119838131
'''

import ctypes, sys

host = "c:\Windows\System32\drivers\etc\hosts"
exit = "please press enter exit"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def show():
    lineNum = 1
    with open(host, 'r') as f:
        linelist = f.readlines()
    for i in linelist:
        print(str(lineNum) + " " + i, end="'")
        lineNum = lineNum + 1
    input(exit)


def add():
    addStr = input('新增内容:')
    with open(host, 'a+') as f:
        f.write(addStr + '\n')
    print(addStr + '\thava add')
    input(exit)


def edit():
    lineNum = 1
    with open(host, 'r') as f:
        linesList = f.readlines()
    for i in linesList:
        print(str(lineNum) + " " + i, end="")
        lineNum = lineNum + 1
    lineNummber = int(input('please enter lineNumber:'))
    if linesList[lineNummber - 1].startswith('#'):
        linesList[lineNummber - 1] = linesList[lineNummber - 1].replace('#', "", 1)
    else:
        linesList[lineNummber - 1] = "#" + linesList[lineNummber - 1]
    with open(host, 'a+') as f:
        f.truncate(0)
        f.writelines(linesList)
    input(exit)


if __name__ == '__main__':
    if is_admin():
        print('host编辑器:')
        operateType = input("查看hosts:1\n编辑:2\n新增host:3")
        if (operateType == "1"):
            show()
        if (operateType == "2"):
            edit()
        if (operateType == "3"):
            add()
    else:
        ctypes.windll.shell32.ShellExcutew(None, 'runas', sys.executable, __file__, None, 1)
