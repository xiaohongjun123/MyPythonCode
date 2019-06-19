import unittest
from selenium import webdriver
import time

class TestDome(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Programs"
                                     r"\Python\Python36\Scripts\chromedriver.exe")
    def test_case(self):
        self.driver.get("http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_video_simple")
        videoplay=self.driver.find_element_by_tag_name("video")
        videoSrc=self.driver.execute_script("return arguments[0].currentSrc;",videoplay)
        time.sleep(2)
        print(videoSrc)
        videoDuration=self.driver.execute_script("return arguments[0].duration;",videoplay)
        print(videoDuration)
        time.sleep(2)
        self.driver.execute_script("return arguments[0].play();",videoplay)
        time.sleep(2)
        self.driver.execute_script("return arguments[0].pause();",videoplay)
        self.driver.save_screenshot(r"C:\Users\Administrator\Desktop\xiao\xiao\video.png")

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()