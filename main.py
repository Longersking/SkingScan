from route import *
from utils.character_tools import CharacterTools
from config.text_config import *
from scanner.collect_message import collect_message
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
                collect_message.main(url)
                # 在这里调用你的函数，并将URL作为参数传递
                # route_function(url)
            else:
                CharacterTools.show("缺少 -u 参数后的URL",blue)

        elif command == '-r':
            CharacterTools.show("-r 参数被指定")
            # 在这里执行 -r 参数的操作
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
    main( )
