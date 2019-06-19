import unittest
from selenium import webdriver
import time
class  Traverse(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://192.168.2.200:8081/login")
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        username=self.driver.find_element_by_id("M_username")
        username.send_keys("mc_admin")
        password=self.driver.find_element_by_id("M_password")
        password.send_keys("Aa123456")
        code=self.driver.find_element_by_id("code")
        code.send_keys("5847")
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(2)


if __name__=="__main__":
    unittest.main()