import unittest
from selenium import webdriver
import time
import logging


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=r"D:\web\test.log",
                    filemode="w")

def info(message):
    logging.info(message)

def highLight(driver,element):
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                          element,"background:green;border:2px solid red;")

class TestDame(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        info("登录网址")
        self.driver.get("http://www.sogou.com")
    def test_case(self):
        searchbox=self.driver.find_element_by_id("query")
        highLight(self.driver,searchbox)
        time.sleep(3)
        searchbox.send_keys("测试")
        button=self.driver.find_element_by_id("stb")
        highLight(self.driver,button)
        time.sleep(3)
        button.click()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()