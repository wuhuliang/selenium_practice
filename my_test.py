# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import excel_table


class Zentao_demo(unittest.TestCase):

    def setUp(self):
        self.br = webdriver.Chrome()
        self.br.get('https://zentao.chinamcloud.com/zentao')
        self.br.maximize_window()
        # 使用函数unicode(content,"utf8")即可
        self.assertIn(unicode('用户登录 - 禅道', 'utf-8'), self.br.title)

    def test_login(self):
        """测试登录功能"""
        zentao = self.br

        listdata = excel_table.excel_table_byindex('F:\python practice\selenium_practice\\auto_testCase.xlsx')

        if len(listdata) <= 0:
            assert 0, u'Excel数据异常'

        for i in range(len(listdata)):
            username = zentao.find_element_by_name('account')
            username.clear()
            username.send_keys(listdata[i]['username'])
            password = zentao.find_element_by_name('password')
            password.clear()
            password.send_keys(listdata[i]['password'])

            zentao.find_element_by_id('submit').click()
            zentao.implicitly_wait(5)
            try:
                elem = zentao.find_element_by_id('companyname')
            except NoSuchElementException:
                assert 0, u'登录失败'

            zentao.find_element_by_xpath('//*[@id="topnav"]/a[1]').click()



    def tearDown(self):
        self.br.quit()


if __name__ == '__main__':
    unittest.main()

