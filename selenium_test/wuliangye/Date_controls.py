from selenium import webdriver
import unittest
import time
import pytesseract
from PIL import Image
from urllib import request
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
class DateControls(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://192.168.2.200:8081/login")

    def verify_code(self):
        jpg_link = "http://192.168.2.200:8081/verifycode/?0.8974717357155602"
        path = r"C:\Users\Administrator\Desktop\xiao\xiao\test.png"
        request.urlretrieve(jpg_link, path)

        image = Image.open(r'C:\Users\Administrator\Desktop\xiao\xiao\test.png')

        code = pytesseract.image_to_string(image)
        time.sleep(2)
        print(code)
        new_code = []
        value = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in code:
            if i in value:
                new_code.append(i)
        print(new_code)
        ls2 = (str(new_value) for new_value in new_code)
        YZM = "".join(ls2)
        print(YZM)
        return YZM


    def test_case(self):
        self.driver.find_element_by_xpath('''//*[@id="M_username"]''').send_keys("mc_admin")
        self.driver.find_element_by_xpath('''//*[@id="M_password"]''').send_keys("Aa123456")
        print(verify_code())

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
