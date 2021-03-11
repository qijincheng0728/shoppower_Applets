'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 14:27
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : BaseDriver.py
# @Software: PyCharm

'''

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

test_url = 'http://www.shop2power10.top/admin/login/index'

class Driver():
    def login(self):
        driver = webdriver.Chrome()
        driver.get(url=test_url)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('// *[ @ id = "username"]').send_keys('1234567')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('1234567')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/button').click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="tabContent"]/div/iframe'))
        driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[5]/button[2]').click()
        driver.switch_to.default_content()
        time.sleep(2)
        EC.frame_to_be_available_and_switch_to_it('//*[@id="tabContent"]/div[1]/iframe11')

        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="tabContent"]/div[1]/iframe'))
        return driver

if __name__=='__main__':
    Driver().login()
