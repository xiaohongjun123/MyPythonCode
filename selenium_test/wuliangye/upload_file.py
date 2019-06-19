from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class UploadFile(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get(r"D:\web\shangcuanwenjian.html")

    def test_case(self):
        try:
            wait=WebDriverWait(self.driver,10,0.2)
            wait.until(EC.element_to_be_clickable((By.ID,"file")))
        except  Exception as e:
            print(traceback.print_exc())
        else:
            filebox=self.driver.find_element_by_id("file")
            filebox.send_keys(r"D:\web\test.html")
            time.sleep(5)
            self.driver.find_element_by_id("filesubmit").click()
            time.sleep(5)
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()

