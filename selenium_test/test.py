import unittest
import time
from selenium import webdriver

class GrorRoad(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Ie()
        self.driver.get("http://www.baidu.com")

    def test_open(self):
        time.sleep(3)
        shuru=self.driver.find_element_by_xpath('''//*[@id="kw"]''')
        shuru.send_keys("光荣之路自动化测试")
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        assert u"吴晓华" in self.driver.page_source,"页面中不存在寻找的关键字"

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
