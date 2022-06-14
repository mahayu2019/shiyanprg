#!/usr/bin/env python
# coding=utf-8

'''
测试验证码识别技术
'''
import ddddocr

ocr = ddddocr.DdddOcr()
with open('yz1.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)
