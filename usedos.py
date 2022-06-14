#!/usr/bin/env python
# coding=utf-8

'''
使用dos并返回输出结果
原文
https://blog.csdn.net/boysoft2002/article/details/120888355
'''

import os


def dir(Drive):
    command = 'dir ' + Drive + ':'
    dirlist = os.popen(command).readlines()
    for d in dirlist:
        print(d, end='')
    print()

dir('g')