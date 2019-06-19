import unittest
from selenium import webdriver
import time

class HuaDong(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.baidu.com")

    def test_case(self):
        self.driver.find_element_by_xpath('''//*[@id="kw"]''').send_keys("测试")
        self.driver.find_element_by_xpath('''//*[@id="su"]''').click()
        '''
        self.driver.execute_script(
            "window.scrollTo(100,document.body.scrollHeight);"
        )
        '''
        for i in range(10):
            self.driver.execute_script(
                "window.scrollBy(0,20);"
            )
            time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()