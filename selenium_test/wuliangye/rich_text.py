import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time

class RichText(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("https://mail.sohu.com/fe/#/login")
        time.sleep(3)

    def test_case(self):
        self.driver.find_element_by_xpath('''//*[@id="theme"]/form/div[1]/div[1]/input''').send_keys("xiaoceres")
        self.driver.find_element_by_xpath('''//*[@id="theme"]/form/div[2]/div[1]/input''').send_keys("Aa123456")
        self.driver.find_element_by_xpath('''//*[@id="theme"]/form/div[5]/input''').click()
        self.driver.implicitly_wait(10)
        try:
            #wait=WebDriverWait(self.driver,10)
            #wait.until(EC.element_to_be_clickable((By.XPATH,'''//*[@id="addSkinClass"]/div[4]/div/ul/li[1]''')))
            self.driver.find_element_by_xpath('''//*[@id="addSkinClass"]/div[4]/div/ul/li[1]''').click()
            self.driver.find_element_by_xpath('''//*[@id="mailContent"]/div/div[1]/div[1]/div[1]/div[1]/div/span/input''').send_keys("979669145@qq.com")
            self.driver.find_element_by_xpath('''//*[@id="mailContent"]/div/div[1]/div[1]/div[4]/input''').click()
            self.driver.find_element_by_xpath('''//*[@id="mailContent"]/div/div[1]/div[1]/div[4]/input''').send_keys("哈哈哈哈哈哈哈哈哈哈或或")
            time.sleep(2)
            self.driver.switch_to.frame("ueditor_0")
            self.driver.find_element_by_xpath('''/html/body''').send_keys("这是测试邮件")
            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath('''//*[@id="mailContent"]/div/div[2]/span[1]''').click()
            time.sleep(2)
        except TimeoutException:
            print("超时")
        except NoSuchElementException:
            print("没有页面元素")
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
