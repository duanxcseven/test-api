"""
此模块专门处理用例中的绝对路径
"""
# 导入识别路径的包
import os

# 获取项目的根目录绝对路径=获取当前文件的目录（获取当前文件的目录（获取当前文件的绝对路径（获取当前文件名）））
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取用例数据文件夹所在目录的绝对路径
datas_dir = os.path.join(base_dir, "datas")

# 配置文件的根目录
conf_dir = os.path.join(base_dir, "conf")

# 日志文件的目录
logs_dir = os.path.join(base_dir, "logs")

# 报告文件的目录
reports_dir = os.path.join(base_dir, "reports")

# 用例的目录
testcases_dir = os.path.join(base_dir, "testcases")





