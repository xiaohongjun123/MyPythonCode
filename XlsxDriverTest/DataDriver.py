from selenium import webdriver
import unittest,time
from LogCommon import logger
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
import ExcelUtil
logger=logger.mylog("log").getlog()
Data=ExcelUtil.ParaExcel(r"G:\Test.xlsx","Sheet1")

@ddt.ddt
class TestDome(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(
            r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.baidu.com")
    @ddt.data(*Data.getDataFromSheet())
    def test_case(self,data):
        testdata,exceptdata=tuple(data)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(1)
            self.assertIn(exceptdata,self.driver.page_source)
        except NoSuchElementException as e:
            logger.error("查找页面元素失败"+str(traceback.format_exc()))
        except AssertionError as e:
            logger.info("搜索%s,期望%s失败"%(testdata,exceptdata))
            raise AssertionError
        except Exception as e:
            logger.error("未知信息错误"+str(traceback.format_exc()))
        else:
            logger.info("搜索%s,期望%s通过"%(testdata,exceptdata))

if __name__=="__main__":
    unittest.main()

