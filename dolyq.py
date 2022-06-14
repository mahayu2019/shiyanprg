#!/usr/bin/env python
# coding=utf-8

'''
控制路由器
'''

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
import time

driver = Chrome()

driver.get('http://192.168.1.1/cgi-bin/index2.asp')

driver.find_element(By.ID, 'Username').send_keys('CMCCAdmin')
driver.find_element(By.ID, 'Password').send_keys('aDm8H%MdA')
driver.find_element(By.ID, 'btnSubmit').click()
time.sleep(2)

# 目标丢失
driver.find_element(By.ID, 'Menu_L1_Active').click()
driver.find_element(By.ID, 'Menu_L2_Link').click()
driver.find_element(By.NAME, 'btnReboot').click()
