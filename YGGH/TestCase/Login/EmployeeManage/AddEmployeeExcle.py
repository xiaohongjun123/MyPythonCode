import ExcelUtill
from LogCommon import logger
from LoginCommon import LoginL
import traceback
import unittest
from selenium.common.exceptions import NoSuchElementException
import ddt
import time
Data=ExcelUtill.ParaExcel(r"G:\addemployee.xlsx","Sheet1")
logger=logger.mylog("test").getlog()
@ddt.ddt
class AddemployyeExcel(unittest.TestCase):
    def setUp(self):
        self.driver=LoginL.LoginMode().LoginT()
    @ddt.data(*Data.getDataFromSheet())
    def test_case(self,data):
        name,jobnumber,phone=tuple(data)
        self.driver.implicitly_wait(10)
        try:
            self.driver.switch_to.frame("content")
            self.driver.find_element_by_xpath('''//*[@id="TheSix"]/div[2]/img''').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('''//*[@id="list"]/div[1]/button[1]''').click()
            self.driver.find_element_by_xpath('''//*[@id="username"]''').send_keys(name)
            self.driver.find_element_by_xpath('''//*[@id="jobNumber"]''').send_keys(jobnumber)
            self.driver.find_element_by_xpath('''//*[@id="phone"]''').send_keys(phone)
            self.driver.find_element_by_xpath('''//*[@id="tijiao"]''').click()
            self.assertIn("导入员工",self.driver.page_source)
        except NoSuchElementException as e:
            logger.error("没有发现元素"+str(traceback.format_exc()))
        except AssertionError as e:
            logger.error("添加失败")
        else:
            logger.info("添加成功")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
