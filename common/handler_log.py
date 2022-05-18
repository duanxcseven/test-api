import logging
import os
from common.handler_conf import conf
from common.handler_path import logs_dir

def log_handler(name='log_handler', level='DEBUG', shlevel='DEBUG', filename='log.txt', fhlevel='DEBUG', ):
    # 创建一个日志收集器
    log = logging.getLogger(name)
    # 设置日志收集等级
    log.setLevel(level)

    # 设置日志输出等级,输出渠道
    # 输出到控制台
    sh = logging.StreamHandler()
    # 设置输出到控制台的等级
    sh.setLevel(shlevel)
    # 收集器与输出器绑定
    log.addHandler(sh)

    # 输出到文件
    fh = logging.FileHandler(filename=filename, encoding='utf-8')
    # 设置输出到文件的等级
    fh.setLevel(fhlevel)
    # 收集器与输出器绑定
    log.addHandler(fh)

    # 设置日志输出格式
    formatter = '%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s:%(message)s'
    formats = logging.Formatter(formatter)
    # 输出到控制台
    sh.setFormatter(formats)
    # 输出到文件
    fh.setFormatter(formats)

    return log


# 使用conf读取配置文件的日志配置
name = conf.get('log', 'name')
level = conf.get('log', 'level')
shlevel = conf.get('log', 'shlevel')
filename = os.path.join(logs_dir,conf.get('log','filename'))
fhlevel = conf.get('log', 'fhlevel')
# 为了避免创建多个收集器，重复收集问题，在这里创建一个日志收集器，使用时直接调用此收集器即可
log = log_handler(name, level, shlevel, filename, fhlevel)
 