from selenium import webdriver
import unittest
import time

class Seach(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
    def test_case(self):
        self.driver.set_window_position(y=400,x=400)
        self.driver.get_window_size(800.800)
        now_handle=self.driver.current_window_handle
        #print(now_handle)
        shuru=self.driver.find_element_by_xpath('''//*[@id="kw"]''')
        shuru.send_keys("selenium")
        click_=self.driver.find_element_by_xpath('''//*[@id="su"]''')
        click_.click()
        time.sleep(3)
        self.driver.find_element_by_xpath('''//*[@id="2"]/h3/a''').click()
        time.sleep(3)
        all_handles=self.driver.window_handles
        for handle in all_handles:
            if handle!=now_handle:
                self.driver.switch_to.window(handle)
        page=self.driver.page_source
        self.assertTrue(u"hahahahah " in page,"页面中存在元素")

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
