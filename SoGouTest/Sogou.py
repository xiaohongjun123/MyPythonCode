from selenium import webdriver
import unittest
import time
from ObjectMap import ObjectMap
class TestSogouObjectMap(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.obj=ObjectMap()
        self.driver.get("http://www.sogou.com")

    def test_case(self):
        search=self.obj.getElementObject(self.driver,"sogou","searchBox")
        search.send_keys("Webdriver实战宝典")
        button=self.obj.getElementObject(self.driver,"sogou","searchButton")
        button.click()
        time.sleep(2)
        self.assertIn("吴晓华",self.driver.page_source,"result is error")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()