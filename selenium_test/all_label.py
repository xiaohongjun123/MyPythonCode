from selenium import webdriver
import unittest
import time

class Seach(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
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
        all_label=self.driver.find_elements_by_xpath("//h3/a")
        for label in all_label:
            print(label.text)

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
