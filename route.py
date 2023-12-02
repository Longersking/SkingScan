import os

# 定义全局路径变量
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
REPORTS_DIR = os.path.join(PROJECT_ROOT,'reports')
SCANNER_DIR = os.path.join(PROJECT_ROOT,'scanner')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
CONFIG_DIR = os.path.join(PROJECT_ROOT, 'config')
UTIL_DIR = os.path.join(PROJECT_ROOT, 'utils')

# 其他路径定义...

# 示例函数：展示如何在其他项目中导入这些路径
def dirs_function():
    print("项目根目录:", PROJECT_ROOT)
    print("导入文件目录",REPORTS_DIR)
    print("扫描器目录:", SCANNER_DIR)
    print("数据目录:", DATA_DIR)
    print("日志目录:", LOG_DIR)
    print("配置文件目录:", CONFIG_DIR)
    print("工具目录",UTIL_DIR)
