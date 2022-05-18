"""
用来处理python在jenkins上的环境配置问题
"""


class Handler_module:

    def module(self):

        try:
            import os
        except:
            import os
        try:
            import re
        except:
            import os
            os.system('pip install re')
        try:
            import logging
        except:
            import os
            os.system('pip install logging')
        try:
            import pymysql
        except:
            import os
            os.system('pip install pymysql')
        try:
            import pymssql
        except:
            import os
            os.system('pip install pymssql')
        try:
            import pymssql
        except:
            import os
            os.system('pip install pymssql')
        try:
            import openpyxl
        except:
            import os
            os.system('pip install openpyxl')
        try:
            import datetime
        except:
            import os
            os.system('pip install datetime')
        try:
            import unittest
        except:
            import os
            os.system('pip install unittest')
        try:
            import requests
        except:
            import os
            os.system('pip install requests')
        try:
            from time import sleep
        except:
            import os
            os.system('pip install time')
        try:
            from jsonpath import jsonpath
        except:
            import os
            os.system('pip install jsonpath')
        try:
            from configparser import ConfigParser
        except:
            import os
            os.system('pip install configparser')
        try:
            from unittestreport import ddt, list_data
        except:
            import os
            os.system('pip install unittestreport')
        try:
            from requests_toolbelt import MultipartEncoder
        except:
            import os
            os.system('pip install requests_toolbelt')

        try:
            import re
            import logging
            import pymysql
            import pymssql
            import openpyxl
            import datetime
            import unittest
            import requests
            from time import sleep
            from jsonpath import jsonpath
            from configparser import ConfigParser
            from unittestreport import ddt, list_data
            from requests_toolbelt import MultipartEncoder
        except ImportError as e:
            raise e






















