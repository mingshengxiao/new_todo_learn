# -*- coding: utf-8 -*-
import logging
import time

"""
日志分为5个等级，分别为：CRITICAL 严重错误；ERROR 错误；WARNING 警告；INFO 提示信息；DEBUG 详细的信息
"""
# 获取logger实例
logger = logging.getLogger(__name__)
# 获取文件handler,以追加的方式打开文件
logname = 'test%s.log' % time.strftime('%Y-%m-%d')
fh = logging.FileHandler(logname, 'a')
# ch = logging.StreamHandler()  获取控制台handler
# 指定日志的输出格式
formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] -fuc:%(funcName)s-%(levelname)s:%(message)s')
"""
日志输出格式：
	%(evelno)s : 打印日志级别的数值
	%(evelname)s : 打印日志级别名称
	%(pathname)s : 打印当前执行程序的路径，相当于sys.argv[0]
	%(filename)s : 打印当前执行程序名
	%(funcName)s : 答应日志的当前函数
	%(lineno)d : 打印日志的当前行号
	%(asctime)s : 打印日志的时间
	%(thread)d : 打印线程ID
	%(threadName)s : 打印线程名称
	%(process)d : 打印进程ID
	%(message)s : 打印日志信息
"""
fh.setFormatter(formatter)
# 指定日志的最低输出级别
logger.setLevel(logging.INFO)
# 添加处理器
logger.addHandler(fh)
# 写日志
logger.critical('1')
logger.error('2')
logger.warning('3')
logger.info('4')
logger.debug('5')
# 移除日志处理器
logger.removeHandler(fh)
# 关闭文件
fh.close()