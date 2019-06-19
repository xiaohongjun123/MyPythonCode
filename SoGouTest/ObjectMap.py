
import configparser
from selenium.webdriver.support.ui import WebDriverWait
import os
class ObjectMap(object):
    def __init__(self):
        self.uiObjectMappath=os.path.dirname(os.path.abspath(__file__))+r"\\UiObjectMap.ini"
        print(self.uiObjectMappath)

    def getElementObject(self,driver,webSiteName,elementName):
        try:
            cf=configparser.ConfigParser()#创建一个读取配置文件的实例
            cf.read(self.uiObjectMappath)
            locators=cf.get(webSiteName,elementName).split(">")#获取配置文件中的页面元素的定位以及定位表达式的组成字符串并用>分隔开
            locatorMethod=locators[0]
            locatorExpression=locators[1]
            print(locatorMethod,locatorExpression)
            element=WebDriverWait(driver,10).until(lambda x:x.find_element(locatorMethod,locatorExpression))

        except Exception as e:
            raise e
        else:
            return element

