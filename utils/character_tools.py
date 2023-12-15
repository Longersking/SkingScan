import difflib
from bs4 import BeautifulSoup

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
    def join_strings(string_list):
        if not string_list:
            return ""  # 如果列表为空，返回空字符串

        result = "".join(string_list)
        return result



if __name__ == "__main__":
    character_tools = CharacterTools()
    # 测试
    string_list = [
        'your uid:1  your email is: pikachu',
        'your uid:1  your email is: root@localhost',
        'your uid:1  your email is: Win64',
        'your uid:1  your email is: 5.7.26'
    ]
    result = character_tools.longest_common_substring(string_list)
    print(character_tools.remove_substring(string_list,result))

