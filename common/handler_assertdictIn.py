
from jsonpath import jsonpath


# 处理字典的成员断言
def assertDictIn(expect, res):
    for k, v in expect.items():
        if res.get(k) == v:
            pass
        else:
            raise AssertionError('{} not in {}'.format(expect, res))

#处理多数据的返回形式的成员断言
def assertDictsIn(expect, res):
    for k,v in expect.items():
        if jsonpath(res,'$..{}'.format(k)):
            if jsonpath(res,'$..{}'.format(k))[0]==v:
                pass
            else:
                raise AssertionError('{} not in {}'.format(expect, res))
        else:
            raise AssertionError('{} not in {}'.format(expect, res))