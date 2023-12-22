import difflib
import re
from bs4 import BeautifulSoup
from config.text_config import *


class CharacterTools:
    def __init__(self):
        pass

    #选出两段字符串中的差异部分
    @staticmethod
    def find_different_chars(str1, str2):
        # 使用 ndiff 找到不同的部分
        diff = difflib.ndiff(str1, str2)
        # 从差异中提取不同的字符串
        diff_chars = ''.join(x[-1] for x in diff if x.startswith('- '))
        return diff_chars

    #去除html标签
    @staticmethod
    def remove_html_tags(html):
        # 使用BeautifulSoup去除标签
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator=" ")
        return text

    # 选出公共最长子串
    @staticmethod
    def longest_common_substring(strs):
        if not strs:
            return ""

        # 获取字符串列表中最短的字符串长度
        min_len = min(len(s) for s in strs)
        max_sub = ""

        for i in range(min_len):
            for j in range(i + 1, min_len + 1):
                sub = strs[0][i:j]  # 取第一个字符串的子串
                if all(sub in s for s in strs[1:]):  # 检查是否为所有字符串的子串
                    if len(sub) > len(max_sub):
                        max_sub = sub

        return max_sub

    # 去除指定字符
    @staticmethod
    def remove_substring(strs, substring):
        result = []

        for s in strs:
            # 使用 replace 函数去除指定子串
            updated_s = s.replace(substring, '')
            result.append(updated_s)

        return result


    #拼接多个字符串
    @staticmethod
    def join_strings(string_list):
        if not string_list:
            return ""  # 如果列表为空，返回空字符串

        result = "".join(string_list)
        return result

    #分隔ip和端口
    @staticmethod
    def split_ip_port(ip_port):
        if ':' in ip_port:
            a,b = ip_port.split(':')
            return a,b
        else:
            return ip_port

    #打印带有色彩的文本
    @staticmethod
    def show(string,model=0):
        string = str(string)
        if model == green:
            print('\033[32m' + string + '\033[0m')
        elif model == yellow:
            print('\033[93m' + string + '\033[0m')
        elif model == red:
            print('\033[31m' + string + '\033[0m')

    #检查输入的参数
    @staticmethod
    def check_input_type(input_string, mode=OTHER):
        if mode == URL:  # 检测URL
            url_pattern = r'^(http|https)://[^\s/$.?#].[^\s]*$'
            return bool(re.match(url_pattern, input_string))
        elif mode == IP:  # 检测IP地址
            ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
            return bool(re.match(ip_pattern, input_string))
        elif mode == PORT:  # 检测端口号（0 - 65535）
            try:
                port = int(input_string)
                return 0 <= port <= 65535
            except ValueError:
                return False
        else:
            return True

    # 将http数据包修改为poc_payload对应对的格式
    @staticmethod
    def get_payload_by_http(http_message, cmd=None):
        lines = http_message.split('\n')
        method, path, http_version = lines[0].split()
        headers = {}
        data = {}
        data_flag = False
        for line in lines[1:]:
            if not line.strip():
                data_flag = True
                continue

            if data_flag:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()

        exploit_payload = {
            "method": method,
            "path": path,
            "http_version": http_version,
            "headers": headers,
            "data": data,
            "body": None
        }
        # 如果存在可控参数
        if cmd:
           exploit_payload[cmd] = "{{ variables.value }}"

        return exploit_payload


if __name__ == "__main__":
    character_tools = CharacterTools()
    # # 测试
    # string_list = [
    #     'your uid:1  your email is: pikachu',
    #     'your uid:1  your email is: root@localhost',
    #     'your uid:1  your email is: Win64',
    #     'your uid:1  your email is: 5.7.26'
    # ]
    # result = character_tools.longest_common_substring(string_list)
    # print(character_tools.remove_substring(string_list,result))
    ip_host = "192.168.52.128:8080"
    k,v = character_tools.split_ip_port(ip_host)
    print(k)
    print(v)

