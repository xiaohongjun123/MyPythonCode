import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
import time

class FrameChange(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get(r"D:\web\frameset.html")

    def test_case(self):
        self.driver.switch_to.frame(0)
        leftframetext=self.driver.find_element_by_xpath("//p")
        print(leftframetext.text)
        self.assertEqual(leftframetext.text,u"这是左侧 frame 页面上的文字")
        self.driver.find_element_by_xpath("/html/body/input").click()
        
        try:
            alert=WebDriverWait(self.driver,10).until(EC.alert_is_present())#获取到弹出框
            print(alert.text)
            alert.accept()#点击弹出框的确定按钮
        except TimeoutException as e:
            print(e)
        self.driver.switch_to.default_content()#退出当前iframe才能进入到其他的iframe
        self.driver.switch_to.frame("middleframe")
        self.assertIn("这是中间frame上的文字",self.driver.page_source,"The result is fail")
        self.driver.find_element_by_xpath('''//*[@id="text"]''').send_keys("这是一个输入框")
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("rightframe")
        self.assertIn("这是右间frame上的文字",self.driver.page_source,"the result is fail")
        print("done")

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()

