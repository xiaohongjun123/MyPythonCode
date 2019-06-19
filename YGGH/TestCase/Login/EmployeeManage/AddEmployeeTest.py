
from LoginCommon import LoginL
import unittest
from LogCommon import logger
from selenium.common.exceptions import NoSuchElementException
import traceback
logger=logger.mylog("log").getlog()

class AddEmp(unittest.TestCase):
    '''添加员工模块'''
    driver = LoginL.LoginMode().LoginT()
    def test_addEmp(self):
        '''添加员工用例'''

        self.driver.implicitly_wait(10)
        try:
            self.driver.switch_to.frame("content")
            self.driver.find_element_by_xpath('''//*[@id="TheSix"]/div[2]/img''').click()
            self.driver.find_element_by_xpath('''//*[@id="list"]/div[1]/button[1]''').click()
            self.driver.find_element_by_xpath('''//*[@id="username"]''').send_keys("吓跑")
            self.driver.find_element_by_xpath('''//*[@id="jobNumber"]''').send_keys("741852")
            self.driver.find_element_by_xpath('''//*[@id="idNumber"]''').send_keys("513101199208302119")
            self.driver.find_element_by_xpath('''//*[@id="phone"]''').send_keys("18227101093")
            self.driver.find_element_by_xpath('''//*[@id="tijiao"]''').click()
            self.assertIn("导入员工",self.driver.page_source)
        except NoSuchElementException as e:
            logger.error("没有发现元素"+str(traceback.format_exc()))
        except AssertionError as e:
            logger.error("添加员工失败")
            raise AssertionError
        else:
            logger.info("添加成功")
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()

