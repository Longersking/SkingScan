from route import *
import sys

def main():
    args = sys.argv[1:]  # 获取除了脚本名称之外的参数列表
    if '--help' in args:
        print("Usage:")
        print("  -u : 请输入目标网站url")
        print("  -r : Description for -r")
        print("  -add <value> : Description for -add")
    elif '-u' in args:
        print("-u 参数被指定")
        u_index = args.index('-u')
        if u_index + 1 < len(args):
            url = args[u_index + 1]  # 获取 -u 参数后的URL
            print(f"用户输入的URL是: {url}")

            # 在这里调用你的函数，并将URL作为参数传递
            # route_function(url)
        else:
            print("缺少 -u 参数后的URL")

    elif '-r' in args:
        print("-r 参数被指定")
        # 在这里执行 -r 参数的操作
    elif '-add' in args:
        index = args.index('-add')
        additional_arg = args[index + 1] if index + 1 < len(args) else None
        print("-add 参数的值是:", additional_arg)
        # 在这里执行 -add 参数的操作
    else:
        print("未指定参数或使用了无效参数，请使用 --help 查看可用参数")

if __name__ == "__main__":
    main()

