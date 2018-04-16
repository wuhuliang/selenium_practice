# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 访问url
        self.driver.get('http://10.10.28.211:81/bugfree')
        # 放大浏览器
        self.driver.maximize_window()
        # 判断浏览器title中是否包含Bugfree字段
        self.assertIn("BugFree",self.driver.title)
        # 登录浏览器
        user_elem = self.driver.find_element_by_xpath("//*[@id='LoginForm_username']")
        user_elem.clear()
        user_elem.send_keys("wuhuliang")
        password_elem = self.driver.find_element_by_xpath("//*[@id='LoginForm_password']")
        password_elem.clear()
        password_elem.send_keys("123456")
        login_button = self.driver.find_element_by_xpath("//*[@id='SubmitLoginBTN']")
        login_button.click()
        # 判断是否登录成功，解决了编码问题
        self.assertIn("吴虎亮",self.driver.find_element_by_xpath("//*[@id='top']/div[3]").text)

    def test_select_project(self):
        bf = self.driver
        elem = Select(bf.find_element_by_xpath("//*[@id='product_name']"))
        elem.select_by_value("3")
        # 与该句作用一样，但是value的值是固定的，option[4]的值不固定，所以这个不推荐
        # op = bf.find_element_by_xpath("//*[@id='product_name']/option[4]").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
