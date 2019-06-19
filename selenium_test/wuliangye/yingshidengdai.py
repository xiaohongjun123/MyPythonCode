from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import traceback
class Xianshidengdai(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.sogou.com")
    def test_case(self):
        self.driver.implicitly_wait(10)
        try:
            searchbox=self.driver.find_element_by_id("query")
            searchbox.send_keys("测试之路")
            self.driver.find_element_by_id("st").click()
        except(NoSuchElementException,TimeoutException) as e:
            traceback.print_exc()
            print(e)
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

