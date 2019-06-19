from appium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'meizu-m6_note-721QECRS388U2'
        desired_caps['appPackage'] = 'com.hexinpass.welfare'
        desired_caps['appActivity'] = 'com.hexinpass.welfare.mvp.ui.activity.SplashActivity'
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        cls.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_01(self):
        self.driver.find_element_by_id("com.hexinpass.welfare:id/et_phone").send_keys("lhy_006151")
        self.driver.find_element_by_id("com.hexinpass.welfare:id/et_pwd").send_keys("Aa123456")
        self.driver.find_element_by_id("com.hexinpass.welfare:id/btn_login").click()
        sleep(3)
        value=self.driver.find_element_by_id("com.hexinpass.welfare:id/title")
        value_string=''.join(value.text)
        self.assertTrue("阳光福利汇",value_string,"Test result is fail")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()