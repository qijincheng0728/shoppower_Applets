'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 9:44
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : Activity_edit_Image_Text.py
# @Software: PyCharm

'''

from common.BaseDriver import Driver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui

Driver = Driver().login()
Driver.switch_to.frame(Driver.find_element_by_xpath('//*[@id="tabContent"]/div/iframe'))
# 点击编辑编辑按钮，进入编辑页
Driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[5]/button[2]').click()
time.sleep(2)
# 退出iframe可以进入其他iframe
Driver.switch_to.default_content()
# 跳转编辑页所以还需要进入iframe
Driver.switch_to.frame(Driver.find_element_by_xpath('//*[@id="tabContent"]/div[2]/iframe'))
time.sleep(2)
# 进入图文内容模块
Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/ul/li[2]').click()
time.sleep(2)

class activity_edit_Image_Text():
    def Activity_map(self):
        # 主图判空
        Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/em").click()
        time.sleep(1)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        #
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/button').click()
        time.sleep(2)
        # Driver.switch_to.default_content()
        # Driver.switch_to.frame(Driver.find_element_by_xpath('//*[@id="ueditor_0"]'))
        Driver.find_element_by_xpath('//*[@id="upload_img"]').click()



if __name__=='__main__':
    activity_edit_Image_Text().Activity_map()
