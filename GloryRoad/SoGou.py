import unittest,os,time
from selenium import webdriver
from FileUtil import creatDir
import traceback

pickDir=creatDir()#全局变量
def takeScreenshot(driver,savepath,picName):
    picPath=os.path.join(savepath,picName+".png")
    try:
        driver.get_screenshot_as_file(picPath)
    except Exception as e:
        print(traceback.print_exc())
class TestFailCaptureScreem(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs"
                                     r" \Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.sogou.com")
    def testSogouSearch(self):
        try:
            self.driver.find_element_by_id("query").send_keys("光荣之路自动化测试")
            self.driver.find_element_by_id("stb").click()
            time.sleep(3)
            self.assertIn("事在人为",self.driver.page_source,"not find")
        except AssertionError as e:
            takeScreenshot(self.driver,pickDir,(str(e))[0:5])
        except Exception as e:
            takeScreenshot(self.driver,pickDir,str(e))
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main

