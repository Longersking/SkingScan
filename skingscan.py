from route import *
from utils.character_tools import CharacterTools
from utils.file_tools import FileTools
from config.text_config import *
from config.config import *
from scanner.collect_message import collect_message
from scanner.exploiter import vulscan
import logging
import sys
import traceback
import json

# 配置日志记录器
logging.basicConfig(filename=error_log, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def global_exception_handler(exctype, value, tb):
    # 记录异常信息到日志文件
    logging.error(f"Unhandled exception: {exctype}, {value}")
    logging.error("".join(traceback.format_tb(tb)))

    # 提示用户输入错误，并提示查看日志信息
    CharacterTools.show("[-]出现异常，请检查输入内容是否正确，并查看error.log错误日志信息",yellow)
    # 继续程序执行
    pass

# 设置全局异常处理器
sys.excepthook = global_exception_handler

#更新poc字典
def update_poc_dic():
    file_path = DATA_DIR + r"\pocs"
    files_index = FileTools.index_files(file_path)
    FileTools.save_index(poc_dic=files_index)

#添加poc数据包
def add_poc():
    required_fields = ["name", "method", "payload"]  # 必填字段列表
    # 创建一个POC字典
    poc = {
        "vulnerability": {
            "name": None,
            "type": None,
            "affected_software": None,
            "exploit": {
                "method": None,
                "variables": {
                    "rhost": None,
                    "rport": None,
                    "lhost": None,
                    "lport": None,
                    "values": None
                },
                "exploit_payload": None
            }
        }
    }
    CharacterTools.show("[*]poc参数如下\n"+str(poc)+"请输入对应字段")
    help = ("""[*]一下命令用来设置对应的poc字段
                -name : 添加漏洞名称(必填项)
                -type : 添加漏洞类型(选填项)
                -affected_software : 影响的软件应用(多个应用英文逗号隔开)(选填项)
                -method : 漏洞利用方式(必填项只能填http或者command) http表示http数据包,command表示系统执行命令
                -lhost : 利用攻击机ip(非必填)
                -lport : 利用攻击机port(非必填)
                -rhost : 目标主机ip(非必填)
                -rport : 目标主机port(非必填)
                -values : 漏洞利用方式为command，则表示命令执行时可控命令，漏洞利用方式为http，则表示http数据包中可控字段名，
                -payload :（必填，http数据包或者系统命令）
                help : 显示参数
                show options : 显示目前poc的输入配置
                exit : 退出
            """)
    CharacterTools.show(help)
    while True:
        command = input("请输入对应指令:")
        command = command.strip(" ")
        if command == "-name":
            poc["vulnerability"]["name"] = input(">>name ")
        elif command == "-type":
            poc["vulnerability"]["type"] = input(">>type ")
        elif command == "-affected_software":
            poc["vulnerability"]["affected_software"] = input(">>affected_software ")
        elif command == "-method":
            method = input(">>method ")
            # print(method)
            method = method.strip(" ")
            if method not in ["command", "http"]:
                CharacterTools.show("[-]输入参数无效!!!", yellow)
            else:
                poc["vulnerability"]["exploit"]["method"] = method
        elif command == "-lhost":
            poc["vulnerability"]["exploit"]["variables"]["lhost"] = input(">>lhost ")
        elif command == "-lport":
            poc["vulnerability"]["exploit"]["variables"]["lport"] = input(">>lport ")
        elif command == "-rhost":
            poc["vulnerability"]["exploit"]["variables"]["rhost"] = input(">>rhost ")
        elif command == "-rport":
            poc["vulnerability"]["exploit"]["variables"]["rport"] = input(">>rport ")
        elif command == "-values":
            poc["vulnerability"]["exploit"]["variables"]["values"] = input(">>values ")
        elif command == "-payload":
            if poc["vulnerability"]["exploit"]["method"] == 'command':
               payload_input = input(">>payload ")
               poc["vulnerability"]["exploit"]["exploit_payload"] = payload_input
            elif poc["vulnerability"]["exploit"]["method"] == 'http':
                payload_path = input(">>请输入http数据包的文件地址:")
                if payload_path.startswith('"') and payload_path.endswith('"'):
                    file_path = payload_path[1:-1]  # 去除首尾双引号
                else:
                    file_path = payload_path
                try:
                    with open(file_path,'r') as f:
                        payload = f.read()
                        CharacterTools.show(payload)
                        poc["vulnerability"]["exploit"]["exploit_payload"] = CharacterTools.get_payload_by_http(payload,cmd=poc["vulnerability"]["exploit"]["variables"]["values"])
                except FileNotFoundError or FileExistsError as e:
                    CharacterTools.show(f"[-]文件打开出错,error:{e}",yellow)
            else:
                CharacterTools.show("[-]未设置method,请先设置method方法!",yellow)
        elif command == "help":
            CharacterTools.show(help)
        elif command == "show options":
            CharacterTools.show("[*]poc参数如下\n" + str(poc))
        elif command == "exit":

            missing_fields = False
            if not poc["vulnerability"]["exploit"]["method"] or not poc["vulnerability"]["name"] or not poc["vulnerability"]["type"]:
                missing_fields = True
            if missing_fields:
                CharacterTools.show(f"[-]以下必填字段存在未填写项：{', '.join(str(missing_fields))}", yellow)
                choice = input("你确定要退出吗？按（N/n）取消")
                if choice == 'N' or choice == 'n':
                    continue
            break
        else:
            CharacterTools.show("[-]无效指令，请重新输入有效指令", yellow)

    # try:
    #     with open(file_path, 'r') as file:
    #         lines = [line.strip() for line in file.readlines()]  # 去除空格字符
    #         if "=" in "".join(lines):  # 检查是否有'='在其中
    #             http_payload_started = False
    #             http_payload_lines = []
    #             for line in lines:
    #                 if "=" in line:  # 如果在
    #                     key, value = line.split("=")
    #                     key = key.strip()
    #                     value = value.strip()
    #                     # print(value)
    #                     if http_payload_started:
    #                         http_payload_lines.append(line)
    #                     elif key == "name":
    #                         poc["vulnerability"]['name'] = value
    #                         print(value)
    #                     elif key == "type":
    #                         poc["vulnerability"]['type'] = value if value != "null" else None
    #                     elif key == "affected_software":
    #                         poc["vulnerability"]["affected_software"] = value if value != "null" else None
    #                     elif key == "method":
    #                         poc["vulnerability"]["exploit"]["method"] = value
    #                         if value == "http":
    #                             http_payload_started = True
    #                     elif key == "lhost":
    #                         poc["vulnerability"]["exploit"]["variables"]["lhost"] = value if value != "" else None
    #                     elif key == "lport":
    #                         poc["vulnerability"]["exploit"]["variables"]["lport"] = value if value != "" else None
    #                     elif key == "rhost":
    #                         poc["vulnerability"]["exploit"]["variables"]["rhost"] = value if value != "" else None
    #                     elif key == "rport":
    #                         poc["vulnerability"]["exploit"]["variables"]["rport"] = value if value != "" else None
    #                     elif key == "values":
    #                         poc["vulnerability"]["exploit"]["variables"]["values"] = [value] if value != "" else None
    #                     elif key == "payload":
    #                         if poc["vulnerability"]["exploit"]["method"] == 'command':
    #                             poc["vulnerability"]["exploit"]["exploit_payload"] = value
    #                         elif poc["vulnerability"]["exploit"]["method"] == 'http':
    #                             poc["vulnerability"]["exploit"]["exploit_payload"] = '\n'.join(http_payload_lines)
    #                     else:
    #                         if http_payload_started:
    #                             poc["vulnerability"]["exploit"]["exploit_payload"] = '\n'.join(http_payload_lines)
    #                         else:
    #                             continue
    #         else:
    #             CharacterTools.show("[-]poc数据格式错误，缺少'='字符", yellow)
    # except FileNotFoundError or FileExistsError as e:
    #     CharacterTools.show(f'[-]文件无法找到或无法打开,f{e}',yellow)
    #
    # print(1)
    # 检查必填字段是否都有值
    missing_fields = False
    if not poc["vulnerability"]["exploit"]["method"] or not poc["vulnerability"]["name"] or not poc["vulnerability"][
        "type"]:
        missing_fields = True
    # print(2)
    if missing_fields:
        CharacterTools.show(f"[-]以下必填字段存在未填写项：{', '.join(str(missing_fields))}",yellow)
        return None
    else:
        # print(3)
        return poc



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
                if CharacterTools.check_input_type(url,URL) is False:
                    CharacterTools.show("[-]输入的不是url类型参数",yellow)
                    continue
                CharacterTools.show(f"[*]输入的URL是: {url}")
                message_data = collect_message.main(url)
                print(vulscan.handle_message(message_data))
                # 在这里调用你的函数，并将URL作为参数传递
                # route_function(url)
            else:
                CharacterTools.show("缺少 -u 参数后的URL",yellow)

        elif command == '-r':
            CharacterTools.show("-r 参数被指定")
            # 在这里执行 -r 参数的操作
        elif command == 'vulscan':
            CharacterTools.show("[+]漏洞利用交互模块",red)
            vulscan.vulscan()
        elif command == 'update poc_dic':
            update_poc_dic()
        elif command.startswith('-add'):
            # parts = command.split()
            # if len(parts) > 1:
            #     additional_arg = parts[1]
            #     # 去除双引号
            #     if additional_arg.startswith('"') and additional_arg.endswith('"'):
            #         file_path = additional_arg[1:-1]  # 去除首尾双引号
            #     else:
            #         file_path = additional_arg
            #     # CharacterTools.show(f"-add 参数的值是:{additional_arg}")
            #     # 在这里执行 -add 参数的操作
            #     add_poc(file_path)
            # else:
            #     CharacterTools.show("缺少 -add 参数的值",yellow)
            poc = add_poc()
            choice = input("是否保存？按（N/n）取消")
            if choice == 'N' or choice == 'n':
                continue
            try:
                poc_dir = DATA_DIR + r"/pocs/" + str(poc["vulnerability"]["name"]) + r"/"
                if not os.path.exists(poc_dir):
                    os.mkdir(poc_dir)
                poc_outfile = poc_dir + r"/" + str(poc["vulnerability"]["name"]) + ".json"
                poc_json = json.dumps(poc)
            except Exception as e:
                CharacterTools.show(f"[-]出现错误,error:{e}", yellow)
            try:
                with open(poc_outfile,'w') as file:
                    file.write(poc_json)
            except Exception as e:
                CharacterTools.show(f"[-]出现错误,error:{e}",yellow)

        elif command == 'exit':
            CharacterTools.show("退出程序")
            break
        else:
            CharacterTools.show("未指定参数或使用了无效参数，请使用 help 查看可用参数",yellow)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        global_exception_handler(type(e), e, e.__traceback__)

