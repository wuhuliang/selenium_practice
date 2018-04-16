# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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

        username = zentao.find_element_by_name('account')
        username.clear()
        username.send_keys('wuhuliang')

        password = zentao.find_element_by_name('password')
        password.clear()
        password.send_keys('aaaaaa')

        zentao.find_element_by_id('submit').click()
        zentao.implicitly_wait(5)
        self.assertIn(u'华栖云科技hhh', self.br.find_element_by_id('companyname').text)



    def tearDown(self):
        self.br.quit()


if __name__ == '__main__':
    unittest.main()

