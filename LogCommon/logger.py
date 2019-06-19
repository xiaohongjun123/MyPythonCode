import logging
import time
import os


class mylog(object):
    def __init__(self, logger_name):


        self.logger = logging.getLogger(logger_name)#创建一个logger，相当于定义了一个入口
        self.logger.setLevel(logging.INFO)#定义这个logger的整体信息输出等级


        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))#获取到日期，并已特定格式显示
        all_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))#获取到当前文件所在的上层路径
        error_log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

        all_log_name = os.path.join(all_log_path, rq + '.log')#命名所有日志的文件名（所在地址和文件名拼接）
        error_log_name = os.path.join(error_log_path, rq + 'error.log')#命名错误日志的文件名


        fh = logging.FileHandler(all_log_name)#所有log的输出存放（存放到指定文件）
        fh.setLevel(logging.DEBUG)#定义所有log的输出等级

        eh = logging.FileHandler(error_log_name)#所有错误log的输出存放（存放到指定文件）
        eh.setLevel(logging.ERROR)#定义所有错误log的输出等级

        ch = logging.StreamHandler()#所有log的输出存放（存放到控制台显示）
        ch.setLevel(logging.INFO)


        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')#输出信息显示的格式

        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

        fh.setFormatter(all_log_formatter)#将输出格式应用到输出所有log的handler中
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)


        self.logger.addHandler(fh)# 给logger添加handler
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


