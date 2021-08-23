#!/usr/bin/env python
# coding=utf-8
'''
python 生成二维码
原载:https://haiyong.blog.csdn.net/article/details/119801735
对于使用 python 生成 QR 码，我们将使用一个名为QRcode的 python 模块。
链接： https://pypi.org/project/qrcode/
'''

import qrcode  # pip install qrcode
import cv2  # pip install opencv-python OpenCV 是一个专注于实时计算机视觉任务的编程函数库

img = qrcode.make('https://blog.csdn.net/jsship?spm=1011.2124.3001.5343')  # 需要编码的地址或文字
img.save('blog.jpg')  # 保存图像

tx = qrcode.make('ajjhehiwe●○☆☆№◆↑§№☆按时到位')
tx.save('wz.png')

# 识别解析二维码内容
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread('wz.png'))
print('识别结果:', val)
