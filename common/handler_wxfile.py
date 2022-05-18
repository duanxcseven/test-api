"""
处理微信群发送测试报告
"""
import os
import requests
from common.handler_conf import conf
from common.handler_path import reports_dir

class WXFile:

    def wxfile(self):
        #上传文件
        try:
            file_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=' + conf.get("qywx", "group")+'&type=file'
            files = [('filename', ('report.html', open(os.path.join(reports_dir,'report.html'), 'rb'), 'text/html'))]
            response=requests.post(url=file_url,files=files)
            res=response.json()
            #发送群文件
            wxq_url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + conf.get("qywx", "group")
            media_id = res['media_id']
            data={
                    "msgtype": "file",
                    "file": {
                         "media_id": media_id
                            }
                        }
            res_wx=requests.post(url=wxq_url,json=data)
        except:
            print('测试报告发送失败')
        else:
            if res_wx.json() == {'errcode': 0, 'errmsg': 'ok'}:
                print('测试报告已发送企业微信群')





