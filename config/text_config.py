logo = """  ____    _      _                   ____                         
 / ___|  | | __ (_)  _ __     __ _  / ___|    ___    __ _   _ __  
 \___ \  | |/ / | | | '_ \   / _` | \___ \   / __|  / _` | | '_ \ 
  ___) | |   <  | | | | | | | (_| |  ___) | | (__  | (_| | | | | |
 |____/  |_|\_\ |_| |_| |_|  \__, | |____/   \___|  \__,_| |_| |_|
                             |___/                                

 
 项目以放入github:https://github.com/Longersking/SkingScan                            
"""
# skingscan模块提示
help_text = """
                "Usage:"
                "  -u : 请输入目标网站url"
                "  help :查看参数帮助"
                "  vulscan :进入漏洞利用模块"
                " update poc_dic : 更新poc字典索引"
                "  -add 请输入要添加的poc文件路径"
            """
# vulscan模块提示
vulscan_help_text =  """
                "Usage:"
                使用run命令前需要使用set payload，使用set payload 前必须设置目标的参数，包括rhost,rport,values
                " show options : 查看参数信息"
                " set rhost : 设置目标主机host(ip或者域名)"
                
                " set rport : 设置目标主机端口"
      
                " set values : 设置攻击参数"
                " set payload : 设置攻击载荷"
                " run :开始攻击"
                " help :查看参数帮助"
          
            """

#提供poc数据包模板
# poc_model = """
#     name= 漏洞名称(必填)
#     type= 漏洞类型
#     software_name= 影响软件
#     software_version= 影响软件版本
#     method= 漏洞利用方式(必填只能填http或者command) http表示http数据包,command表示系统执行命令
#     lhost=利用攻击机ip(非必填)
#     lport=利用攻击机port(非必填)
#     rhost=目标主机ip(非必填)
#     rport=目标主机port(非必填)
#     values=漏洞利用方式为command，则表示命令执行时可控命令，漏洞利用方式为http，则表示http数据包中可控字段名，
#     payload=（必填，http数据包或者系统命令）
# """

#  "  -r : 请输入数据包对应的文件"
# " set lhost : 设置攻击主机host(ip或者域名)"
# " set lport : 设置攻击主机端口"

#定义全局参数

green = 0
yellow = 1
red = 2
IP = 3
PORT = 4
URL = 5
OTHER = 6