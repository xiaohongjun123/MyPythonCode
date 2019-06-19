from selenium import webdriver
import time
import ddt
from Verify_Code import chaojiying
import unittest
from PIL import Image
from LogCommon import logger
logger=logger.mylog("log").getlog()
cjy=chaojiying.Chaojiying_Client('xhj123456', 'qazwsx123', '899485')
@ddt.ddt
class ErrorLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(
            r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://192.168.2.200:8081/login")
    @ddt.file_data(r"E:\Users\Administrator\PycharmProjects\untitled\YGGH\TestCase\TestData\ErrorLoginData.json")
    def test_case(self,value):
        filename=r"E:\Users\Administrator\PycharmProjects\untitled\YGGH\TestCase\pic\image.png"
        self.driver.save_screenshot(filename)
        ele=self.driver.find_element_by_xpath('''//*[@id="form"]/ul[3]/li[3]/img''')
        left = ele.location['x']
        top = ele.location['y']
        right = ele.location['x'] + ele.size['width']
        bottom = ele.location['y'] + ele.size['height']
        im = Image.open(filename)
        im = im.crop((left, top, right, bottom))
        im.save(filename)
        pic=open(filename,"rb").read()
        code=cjy.PostPic(pic, 1902)["pic_str"]
        username,passwd=tuple(value.strip().split("||"))
        self.driver.find_element_by_xpath('''//*[@id="M_username"]''').send_keys(username)
        self.driver.find_element_by_xpath('''//*[@id="M_password"]''').send_keys(passwd)
        self.driver.find_element_by_xpath('''//*[@id="code"]''').send_keys(code)
        time.sleep(5)
        self.driver.find_element_by_xpath('''//*[@id="form"]/input''').click()
        time.sleep(5)
        self.driver.implicitly_wait(10)
        self.assertIn("账户或密码错误",self.driver.page_source)
        logger.info("登录成功ErrorLogin")

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()