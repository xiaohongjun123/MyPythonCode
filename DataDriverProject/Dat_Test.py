from selenium import webdriver
import unittest,time
from LogCommon import logger
import traceback
import ddt
import HTMLTestRunner
import os
from selenium.common.exceptions import NoSuchElementException
logger = logger.mylog('test').getlog()
@ddt.ddt
class TestData(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(
            r"C:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe")
        self.driver.get("http://www.baidu.com")
    @ddt.file_data("test_dade_list.json")
    def test_case01(self,value):
        print(value)
        testdata,expectdata=tuple(value.strip().split("||"))
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("u").click()
            time.sleep(2)
            self.assertIn(expectdata,self.driver.page_source)

        except NoSuchElementException as e:
            logger.info("页面元素不存在"+str(traceback.format_exc()))
        except AssertionError as e:
            logger.error("搜索%s,期望%s,失败"%(testdata,expectdata))
            raise AssertionError
        else:
            logger.info("搜索%s,期望%s,通过"%(testdata,expectdata))
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    suite1=unittest.TestLoader().loadTestsFromTestCase(TestData)
    suite=unittest.TestSuite(suite1)
    report_dir = os.path.dirname(os.path.abspath(__file__)) # 生成文件存放的路径
    report_name =os.path.join(report_dir,time.strftime("H-%M-%S", time.localtime(time.time())) + ".html")  # 给文件命名
    fp = open(report_name, 'wb')  # 打开report_name文件，并以二进制写入内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'web自动化测试报告',
                                           description=u'result:')  # 调用HTMLTestRunner里面的方法，报告的结构方式
    runner.run(suite)  # 执行这个测试集
    fp.close()