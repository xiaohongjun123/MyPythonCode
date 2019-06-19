from selenium import webdriver
import time
from Verify_Code import chaojiying
from PIL import Image
cjy=chaojiying.Chaojiying_Client('xhj123456', 'qazwsx123', '899485')

class LoginMode(object):
    def LoginT(self):
        driver=webdriver.Chrome(r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        driver.get("http://192.168.2.200:8081/login")
        filename="image.png"
        driver.save_screenshot(filename)
        ele=driver.find_element_by_xpath('''//*[@id="form"]/ul[3]/li[3]/img''')
        left = ele.location['x']
        top = ele.location['y']
        right = ele.location['x'] + ele.size['width']
        bottom = ele.location['y'] + ele.size['height']
        im = Image.open(filename)
        im = im.crop((left, top, right, bottom))
        im.save(filename)
        pic=open(filename,"rb").read()
        code=cjy.PostPic(pic, 1902)["pic_str"]
        driver.find_element_by_xpath('''//*[@id="M_username"]''').send_keys("mc_admin")
        driver.find_element_by_xpath('''//*[@id="M_password"]''').send_keys("Aa123456")
        driver.find_element_by_xpath('''//*[@id="code"]''').send_keys(code)
        driver.find_element_by_xpath('''//*[@id="form"]/input''').click()
        time.sleep(2)
        return driver
if __name__=="__main__":
    A=LoginMode()
    A.LoginT()

