from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://192.168.2.107:35080/puhuihuaPboc/back/loginUI")

    def test_case01(self):
        name=self.driver.find_element_by_xpath('''//*[@id="account"]''')
        time.sleep(3)
        name.send_keys("admin")
        self.driver.find_element_by_xpath('''//*[@id="passwd"]''').send_keys("wliangy123")
        self.driver.find_element_by_xpath('''//*[@id="position"]''').send_keys("1234")
        self.driver.find_element_by_xpath('''//*[@id="login_submit"]''').click()
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,'''/html/body/header/div/div/span'''))
            )
        finally:
            Text=self.driver.find_element_by_xpath("/html/body/header/div/div/span").text
            #print(Text)
            #self.assertEqual(Text,'''人行成都分行“我们的家”运营管理系统''',"test result is fail")
            all_lible=self.driver.find_elements_by_xpath("/html/body/aside/div/dl")
            list_lible=[]
            for lible in all_lible:
                #print(lible.text)
                A=lible.text
                list_lible.append(A)
                ls3=(str(i) for i in list_lible)
                ls4="".join(ls3)
            print(ls4)
            self.assertIn(ls4,''''')

        def tearDown(self):
            self.driver.quit()

if __name__=="__main__":
    unittest.main()





