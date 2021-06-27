#!/usr/bin/env python
# coding=utf-8
'''
自动编辑word文档,来自b站视频
https://www.bilibili.com/video/BV1o64y1k7y1

运行程序后先打开文档,否则无法输入
'''

import pyautogui  # 用于控制键盘鼠标
import pyperclip  # 控制剪贴板
import time

content = """
在pycharm中建立蜘蛛项目很多坑,一路摸爬滚打过来,总结以下流程

python建议使用3.6版本,3.7版运行时会出错,得修改一个文件,参加本站相关文章


更新pip到最新版

python -m pip install --upgrade pip

更新pip与scrapy的关联文件 https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 找对应的文件-->cp37对应python3.7

pip install e:\dl\Twisted-18.7.0-cp36-cp36m-win_amd64.whl

pip install e:\dl\Twisted-18.7.0-cp37-cp37m-win_amd64.whl

安装scrapy

pip install scrapy

"""

time.sleep(5)
pyautogui.click(600, 400)  # 在指定位置单击鼠标

for s in content:
    print(s)
    pyperclip.copy(s)  # 把控制台输出的文字复制到剪贴板
    pyautogui.hotkey('ctrl', 'v')  # 把剪贴板的内容粘贴到word中
