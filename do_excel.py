#!/usr/bin/env python
# coding=utf-8


'''
xlwings的研究
参考
https://zhuanlan.zhihu.com/p/82783751
'''
import xlwings as xw
import os

path = os.getcwd()

app = xw.App(visible=False, add_book=False)
wb = app.books.open(path + r'\test.xlsx')
sht = wb.sheets["sheet1"]
sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
wb.save()
wb.close()
app.quit()