from route import *
from utils.character_tools import CharacterTools
from config.text_config import *
from config.config import *
from scanner.collect_message import collect_message
from scanner.exploiter import vulscan
import logging
import sys
import traceback

# 配置日志记录器
logging.basicConfig(filename=error_log, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def global_exception_handler(exctype, value, tb):
    # 记录异常信息到日志文件
    logging.error(f"Unhandled exception: {exctype}, {value}")
    logging.error("".join(traceback.format_tb(tb)))

    # 提示用户输入错误，并提示查看日志信息
    CharacterTools.show("[-]出现异常，请检查输入内容是否正确，并查看error.log错误日志信息",blue)
    # 继续程序执行
    pass

# 设置全局异常处理器
sys.excepthook = global_exception_handler


def main():
    CharacterTools.show(logo)
    while True:

        command = input("SkingScan > ").strip()  # 获取用户输入的命令并去除首尾空格

        if command == 'help':
            CharacterTools.show(help_text)

        elif command.startswith('-u'):
            parts = command.split()
            if len(parts) > 1:
                url = parts[1]
                CharacterTools.show(f"[*]输入的URL是: {url}")
                message_data = collect_message.main(url)
                print(vulscan.handle_message(message_data))
                # 在这里调用你的函数，并将URL作为参数传递
                # route_function(url)
            else:
                CharacterTools.show("缺少 -u 参数后的URL",blue)

        elif command == '-r':
            CharacterTools.show("-r 参数被指定")
            # 在这里执行 -r 参数的操作
        elif command == 'vulscan':
            CharacterTools.show("[+]漏洞利用交互模块",red)
            vulscan.vulscan()
        elif command.startswith('-add'):
            parts = command.split()
            if len(parts) > 1:
                additional_arg = parts[1]
                CharacterTools.show(f"-add 参数的值是:{additional_arg}")
                # 在这里执行 -add 参数的操作
            else:
                CharacterTools.show("缺少 -add 参数的值",blue)
        elif command == 'exit':
            CharacterTools.show("退出程序")
            break
        else:
            CharacterTools.show("未指定参数或使用了无效参数，请使用 help 查看可用参数",blue)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        global_exception_handler(type(e), e, e.__traceback__)

