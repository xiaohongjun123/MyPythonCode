import HTMLTestRunner_PY3
import unittest
import os
import time
case_path=r"E:\Users\Administrator\PycharmProjects\untitled\YGGH\TestCase\Login"
if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*Test.py")
    suite=unittest.TestSuite()
    suite.addTest(discover)
    report_dir = os.path.dirname(os.path.abspath(__file__)) # 生成文件存放的路径
    report_name =os.path.join(report_dir,time.strftime("H-%M-%S", time.localtime(time.time())) + ".html")  # 给文件命名
    fp = open(report_name, 'wb')  # 打开report_name文件，并以二进制写入内容
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u'web自动化测试报告',description=u'result:')  # 调用HTMLTestRunner里面的方法，报告的结构方式
    runner.run(suite)  # 执行这个测试集
    fp.close()