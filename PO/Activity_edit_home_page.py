'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:38
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : Activity_edit_home_page.py
# @Software: PyCharm

'''

from common.BaseDriver import Driver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import autoit
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


path = "C:\\Users\Administrator\Pictures\AutomaticPicture"

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


class activity_edit_home_page():
    # 活动主副标题
    def Activity_title(self):
        # 在clear不能有效删除input框内的数据的时候，调用键盘删除
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/input').click()
        time.sleep(1)
        # 光标放到右面
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/input').send_keys(Keys.RIGHT)
        # 取出输入框内的数据，然后循环删除输入框内的数据
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/input').get_attribute('value')
        # b = len(a)
        for i in a:
            # 循环变量体
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # 主标题判空
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 输入主标题
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/input').send_keys('小程序自动化主标题')
        time.sleep(2)
        # 保存
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        # 清空后输入副标题
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/input').clear()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/input').send_keys('小程序自动化副标题')
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    def Activity_time(self):
        # 起始时间时间判空
        Driver.find_element_by_xpath('//*[@id="start_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[1]').click()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 判断起始时间不能大于结束时间
        Driver.find_element_by_xpath('//*[@id="start_date"]').click()
        # 起始时间选择当前月最后一天
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="start_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 结束时间选择当前月第一天
        Driver.find_element_by_xpath('//*[@id="end_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="end_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 结束时间时间判空
        Driver.find_element_by_xpath('//*[@id="end_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[2]/div/span[1]').click()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 保存正确时间
        Driver.find_element_by_xpath('//*[@id="start_date"]').click()
        # 起始时间选择当前月第一天
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="start_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 结束时间选择当前月最后一天
        Driver.find_element_by_xpath('//*[@id="end_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="end_date"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate2"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
    # 活动状态
    def Active_state(self):
        # 暂停
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[4]/div/div/div[1]').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 开始
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[2]/div[4]/div/div/div[2]/i').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    # 多商品购买开关
    def Multi_commodity(self):
        # 关闭多商品
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/i').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 开启多商品
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/i').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    # 商品名称
    def Trade_name(self):
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/input').send_keys('自动化小程序商品')
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    # 商品图片
    def Trade_picture(self):
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/span[1]').click()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/img').click()
        time.sleep(2)
        # 利用pyautogui进行鼠标和键盘操作windows文本框
        pyautogui.click(x=403, y=43, duration=1)
        pyautogui.typewrite(path)
        pyautogui.click(x=1676, y=47)
        pyautogui.click(x=308, y=975)
        pyautogui.typewrite("motianlun.jpg")
        pyautogui.click(x=1751, y=1007)
        time.sleep(2)
        # 利用pyautogui使鼠标移动到图片的目标位置
        pyautogui.moveTo(x=1053,y=430, duration=2)
        # 利用pyautogui拽动鼠标到目标位置
        pyautogui.dragTo(x=1054, y=365, duration=2)
        Driver.find_element_by_xpath('//*[@id="sureCut"]').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    # 商品核销时间
    def Write_off_time(self):
        js = "var q=document.documentElement.scrollTop=700"
        Driver.execute_script(js)
        time.sleep(3)
        # 起始时间时间判空
        Driver.find_element_by_xpath('//*[@id="start_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[2]/div/span[1]').click()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 判断起始时间不能大于结束时间
        Driver.find_element_by_xpath('//*[@id="start_date0"]').click()
        # 起始时间选择当前月最后一天
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="start_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 结束时间选择当前月第一天
        Driver.find_element_by_xpath('//*[@id="end_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="end_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 结束时间时间判空
        Driver.find_element_by_xpath('//*[@id="end_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[2]/div/span[1]').click()
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 保存正确时间
        Driver.find_element_by_xpath('//*[@id="start_date0"]').click()
        # 起始时间选择当前月第一天
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="start_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate6"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 结束时间选择当前月最后一天
        Driver.find_element_by_xpath('//*[@id="end_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="end_date0"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate5"]/div[2]/div/span[3]').click()
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

    # 无阶梯购买模式
    def No_ladder_purchase(self):
        js = "var q=document.documentElement.scrollTop=700"
        Driver.execute_script(js)
        time.sleep(3)
        Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/div/input").click()
        time.sleep(2)
        # 选择无阶梯购买模式
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/dl/dd[1]').click()
        time.sleep(2)
        # 商品原价输入框
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').send_keys('50.00')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 商品现价输入框
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/input').send_keys('0.01')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 活动限购次数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').click()
        for i in a:
            Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').send_keys('1000')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 每人购买次数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').send_keys('50')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # Driver.quit()
    # 阶梯购买模式
    def ladder_purchase(self):
        # 通过JS计算屏幕长度 下拉浏览器的页面
        js = "var q=document.documentElement.scrollTop=700"
        Driver.execute_script(js)
        time.sleep(3)
        Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/div/input").click()
        time.sleep(2)
        # 选择阶梯购买模式
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/dl/dd[2]').click()
        time.sleep(2)
        # 商品原价输入框
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/input').send_keys('50.00')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 现价阶梯
        js = "var q=document.documentElement.scrollTop=1000"
        Driver.execute_script(js)
        time.sleep(3)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/span[3]').click()
        time.sleep(1)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/span[3]').click()
        time.sleep(1)
        # 第一阶梯人数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[1]').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[1]').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[1]').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[1]').send_keys('1')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 第一阶梯价格
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[2]').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[2]').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[2]').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/input[2]').send_keys('0.01')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 第二阶梯人数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[3]/input[1]').send_keys('2')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 第二阶梯价格
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[3]/input[2]').send_keys('0.02')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # # 活动限购
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').click()
        # a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').get_attribute('value')
        # for i in a:
        #     Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[1]/input').send_keys('1000')
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        # time.sleep(2)
        # # 每人限购
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').click()
        # a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').get_attribute('value')
        # for i in a:
        #     Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/input').send_keys('50')
        # time.sleep(2)
        # Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        # time.sleep(2)
        # Driver.quit()

    def add_delete_commodity(self):
        js = "var q=document.documentElement.scrollTop=1000"
        Driver.execute_script(js)
        time.sleep(3)
        # # 删除商品
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/span').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 新增商品
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 商品二名称
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/input').send_keys('自动化小程序商品')
        time.sleep(2)
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/img').click()
        time.sleep(2)
        # 利用pyautogui进行鼠标和键盘操作windows文本框
        pyautogui.click(x=403, y=43, duration=1)
        pyautogui.typewrite(path)
        pyautogui.click(x=1676, y=47)
        pyautogui.click(x=308, y=975)
        pyautogui.typewrite("langren.jpeg")
        pyautogui.click(x=1751, y=1007)
        time.sleep(2)
        # 利用pyautogui使鼠标移动到图片的目标位置
        pyautogui.moveTo(x=1053, y=430, duration=2)
        # 利用pyautogui拽动鼠标到目标位置
        pyautogui.dragTo(x=1054, y=365, duration=2)
        Driver.find_element_by_xpath('//*[@id="sureCut"]').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[6]/div/div/div/input").click()
        time.sleep(2)
        # 选择无阶梯购买模式
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[6]/div/div/dl/dd[1]').click()
        time.sleep(2)
        # 商品原价输入框
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/input').click()
        a = Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/input').get_attribute('value')
        for i in a:
            Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/input').send_keys('50.00')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        # 商品核销时间
        # 开始时间 如果不需要删除商品就用@id="layui-laydate10" 如果需要删除商品就用@id="layui-laydate12"
        Driver.find_element_by_xpath('//*[@id="start_date1"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate12"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="start_date1"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate12"]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate12"]/div[2]/div/span[3]').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 结束时间
        Driver.find_element_by_xpath('//*[@id="end_date1"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate11"]/div[2]/div/span[2]').click()
        time.sleep(2)
        Driver.find_element_by_xpath('//*[@id="end_date1"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate11"]/div[2]/div/span[2]').click()
        Driver.find_element_by_xpath('//*[@id="end_date1"]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate11"]/div[1]/div[2]/table/tbody/tr[6]/td[7]').click()
        Driver.find_element_by_xpath('//*[@id="layui-laydate11"]/div[2]/div/span[3]').click()
        time.sleep(2)

        # 商品现价输入框
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[4]/div/input').send_keys('0.01')
        time.sleep(2)
        # 活动限购次数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[7]/div/div[1]/input').click()
        for i in a:
            Driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[7]/div/div[1]/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[7]/div/div[1]/input').send_keys('1000')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 每人购买次数
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[8]/div/input').send_keys('50')
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)

        Driver.quit()

    def display_mode(self):
        js = "var q=document.documentElement.scrollTop=10000"
        Driver.execute_script(js)
        time.sleep(3)
        # 头像+昵称
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div').click()
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 头像+昵称+电话+购买时间
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div').click()
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        # 头像+昵称+电话+购买时间+支付金额
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div').click()
        # 保存
        Driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/button').click()
        time.sleep(2)
        Driver.quit()


if __name__=='__main__':
    activity_edit_home_page().Activity_title()
    # activity_edit_home_page().Activity_time()
    # activity_edit_home_page().Active_state()
    # activity_edit_home_page().Multi_commodity()
    # activity_edit_home_page().Trade_name()
    # activity_edit_home_page().Trade_picture()
    # activity_edit_home_page().Write_off_time()
    # activity_edit_home_page().No_ladder_purchase()
    # activity_edit_home_page().ladder_purchase()
    # activity_edit_home_page().add_delete_commodity()
    # activity_edit_home_page().display_mode()