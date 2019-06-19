from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class XuanFkuang(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.sogou.com")

    def test_case(self):
        search=self.driver.find_element_by_xpath('''//*[@id="query"]''')
        search.send_keys("测试")
        time.sleep(1)
        for i in range(3):
            search.send_keys(Keys.DOWN)
            time.sleep(0.5)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        def tearDown(self):
            self.driver.quit()

if __name__=="__main__":
    unittest.main()