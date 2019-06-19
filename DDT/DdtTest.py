from selenium import webdriver
import unittest, time
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from LogCommon import logger

logger = logger.mylog("test").getlog()


@ddt.ddt
class DdtTest(unittest.TestCase):
    logger.info("开始测试")

    def setUp(self):
        self.driver = webdriver.Chrome(
            r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")

    @ddt.data(["神奇动物字在哪里", "叶茨"],
              ["疯狂动物城", "古德温"],
              ["大话西游之月光宝盒", "周星驰"])
    @ddt.unpack
    def test_dataDrivernByObj(self,testdata,expectdata):
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(10)  # 设置全局等待时间，之后出现的元素在10s内每隔05s检查一次，最大时间超过10s才会报错
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertIn(expectdata, self.driver.page_source)

        except NoSuchElementException as e:
            logger.error("页面元素不存在:" + str(traceback.format_exc()))
        except AssertionError as e:
            logger.info("搜索,%s期望,%s失败" % (testdata, expectdata))
        except Exception as e:
            logger.error("未知错误：" + str(traceback.format_exc()))
        else:
            logger.info("搜索:%s期望：%s通过"%(testdata,expectdata))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
