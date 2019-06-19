from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException

class New_add_meni(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://192.168.2.107:35080/puhuihuaPboc/back/loginUI")
        self.driver.maximize_window()
        self.driver.get

    def isElementexist(self,element):#判断某个元素是否出现的方法
        flag=True
        try:
            self.driver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag

    def test_case01(self):
        if
        name = self.driver.find_element_by_xpath('''//*[@id="account"]''')
        name.send_keys("admin")
        self.driver.find_element_by_xpath('''//*[@id="passwd"]''').send_keys("wliangy123")
        self.driver.find_element_by_xpath('''//*[@id="position"]''').send_keys("1234")
        self.driver.find_element_by_xpath('''//*[@id="login_submit"]''').click()
        try:
            WebDriverWait(self.driver, 5,0.2).until(
                EC.presence_of_element_located((By.XPATH, '''/html/body/header/div/div/spa'''))
            )
            WebDriverWait(self.driver, 5, 0.2).until(
                EC.alert_is_present()).text
            WebDriverWait(self.driver,5,0.2).until(
                EC.element_to_be_clickable((By.LINK_TEXT,)))
            )
        except TimeoutException as e:
            print(traceback.print_exc())

        except NoSuchElementException as e:
            print(traceback.print_exc())
        finally:
            self.driver.find_element_by_xpath("/html/body/aside/div/dl[3]/dt").click()
            time.sleep(1)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath("/html/body/aside/div/dl[3]/dd/ul/dl[8]/dt").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/aside/div/dl[3]/dd/ul/dl[8]/dd/ul/li[1]/a").click()
            for i in range(5):
                self.driver.switch_to.frame(1)
                self.driver.find_element_by_xpath("/html/body/div/form[1]/div/a").click()
                self.driver.switch_to.frame(0)
                self.driver.find_element_by_xpath('''//*[@id="title"]''').send_keys("这是一个测试标题%d"%(i))
                self.driver.find_element_by_xpath('''//*[@id="submit"]''').click()
                self.driver.switch_to.default_content()
                time.sleep(3)
            self.driver.switch_to.frame(1)
            self.assertIn("这是一个测试标题%d"%(i),self.driver.page_source,"页面源码中不存在该字段")

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
