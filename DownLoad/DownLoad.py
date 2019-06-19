from selenium import webdriver
import unittest,time


class DownLoad(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs"
                                     r"\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("https://pypi.org/project/selenium/")
        chromeOption=webdriver.ChromeOptions()
        prefs={"download.default_directory":r"D:\download"}
        chromeOption.add_experimental_option("prefs",prefs)

    def test_case(self):
        self.driver.find_element_by_xpath("//tr[1]/td[2]/a").click()
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()