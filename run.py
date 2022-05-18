from common.handler_module import Handler_module

Handler_module().module()
from jsonpath import jsonpath
import json
import unittest
import requests
from unittestreport import TestRunner
from common.handler_conf import conf
from common.handler_wxfile import WXFile
from common.handler_path import testcases_dir


def run(url):
    # 运行的文件目录
    res = unittest.defaultTestLoader.discover(testcases_dir)
    # 生成测试报告
    runner = TestRunner(res,
                        tester='XXX',
                        desc='接口测试报告')
    data = runner.run()
    # 发送邮箱
    to_addrs = conf.get('email', 'to_addrs')
    input_str = to_addrs.strip(' ').strip("'").strip('"').strip(',').strip('，')
    output_list = input_str.split(',')
    if conf.getint("email", "yes or no email") == 1:
        runner.send_email(
            host=conf.get('email', 'host'),
            port=conf.getint('email', 'port'),
            user=conf.get('email', 'user'),
            password=conf.get('email', 'password'),
            to_addrs=output_list)

    # 【{{title}}】测试结果
    title = jsonpath(data, "$.desc")[0]
    #   测试人员： {{tester}}
    tester = jsonpath(data, "$.tester")[0]
    #   开始时间： {{begin_time}}
    begin_time = jsonpath(data, "$.begin_time")[0]
    #   执行时间： {{runtime}}
    runtime = jsonpath(data, "$.runtime")[0]
    #   用例总数： {{all}}
    all = jsonpath(data, "$.all")[0]
    #   成功用例： {{success}}
    success = jsonpath(data, "$.success")[0]
    #   失败用例： {{fail}}
    fail = jsonpath(data, "$.fail")[0]
    #   错误用例： {{error}}
    error = jsonpath(data, "$.error")[0]
    #   跳过用例： {{skip}}
    skip = jsonpath(data, "$.skip")[0]

    res_text = "【{}】  \n  测试人员:   {}\n  开始时间:   {}\n  执行时间:   {}\n  用例总数:   {}\n  成功用例:   {}\n  失败用例:   {}\n  错误用例:   {}\n  跳过用例:   {}".format(
        title, '测试', begin_time, runtime, all, success, fail, error, skip)
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + url
    payload = json.dumps({
        "msgtype": "text",
        "text": {"content": res_text}})
    headers = {'Content-Type': 'application/json'}
    requests.post(url=url, headers=headers, data=payload)

    WXFile().wxfile()


if __name__ == '__main__':
    run(url=conf.get("qywx", "group"))

