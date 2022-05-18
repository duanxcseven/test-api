import re

from common.handler_conf import conf


# 一个替换的方法
def Handler_replace_attr(data, cls):
    # 循环查找#(.+?)#，找不到则停止
    while re.search('#(.+?)#', data):
        # 匹配对象
        res = re.search('#(.+?)#', data)
        item = res.group()
        # 取出内容
        attr = res.group(1)
        try:
            # 获取类属性
            value = getattr(cls, attr)
        except AttributeError:
            # 找不到类属性时，去配置文件中查找
            value = conf.get('testcase', attr)
        # 替换数据
        data = data.replace(item, str(value))
    # 返回被替换的数据
    return data


def Handler_replace_data(data, replace):
    # 循环查找#(.+?)#，找不到则停止
    while re.search('#(.+?)#', data):
        # 匹配对象
        res = re.search('#(.+?)#', data)
        item = res.group()
        # 取出内容
        attr = res.group(1)
        try:
            # 获取类属性
            value = replace[attr]
        except Exception as e:
            raise e
        # 替换数据
        data = data.replace(item, str(value))
    # 返回被替换的数据
    return data
