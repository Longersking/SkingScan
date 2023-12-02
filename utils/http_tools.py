import requests
from urllib.parse import urlparse, urlencode, parse_qs
from copy import deepcopy

class HTTPTools:
    def __init__(self):
        pass

    @staticmethod
    def send_get_request(url, params=None, headers=None):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # 抛出异常如果请求不成功
            return response
        except requests.exceptions.RequestException as e:
            print(f"get请求error: {e}")
            return None

    @staticmethod
    def send_post_request(url, data=None, json=None, headers=None):
        try:
            response = requests.post(url, data=data, json=json, headers=headers)
            response.raise_for_status()  # 抛出异常如果请求不成功
            return response
        except requests.exceptions.RequestException as e:
            print(f"post请求error: {e}")
            return None

    @staticmethod
    def extract_urls(url):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        paths = parsed_url.path.split('/')
        # print(paths)
        extracted_urls = []

        temp_url = base_url
        for path in paths:
            if path:
                temp_url += f"/{path}"
                extracted_urls.append(temp_url)
            else:
                extracted_urls.append(temp_url)
        # print(extracted_urls)
        return extracted_urls

    @staticmethod
    def extract_domain(url):
        parsed_url = urlparse(url)
        return parsed_url.netloc

    @staticmethod
    def check_request_method(url):
        try:
            responses = requests.get(url)
            if responses.status_code not in (400,403,404):
                return "GET"
            else:
                return "POST"
        except requests.RequestException as e:
            print(f"发生错误：{e}")
            return None

    @staticmethod
    def get_argv(url):
        parsed_url = urlparse(url)
        query_parameters = parse_qs(parsed_url.query)
        # print(parsed_url)
        # print(query_parameters)
        return parsed_url,query_parameters

    @staticmethod
    def update_url(parsed_url,query_parameters,param_name,new_value):
        temp_query_parameters = deepcopy(query_parameters)
        temp_query_parameters[param_name] = [new_value]
        # 重构 URL
        updated_query = urlencode(temp_query_parameters, doseq=True)
        new_url = parsed_url._replace(query=updated_query).geturl()
        # query_parameters = temp_query_parameters
        # print("0",query_parameters)
        return new_url

    @staticmethod
    def update_url_parameters(parsed_url,query_parameters,new_parameters):
        temp_query_parameters = deepcopy(query_parameters)
        # 更新或添加新参数
        # print(new_parameters.items())
        for param_name, new_value in new_parameters.items():
            # print(param_name,new_value)
            temp_query_parameters[param_name] = [new_value]
            # print(query_parameters)



        # 重构 URL
        updated_query = urlencode(temp_query_parameters, doseq=True)
        new_url = parsed_url._replace(query=updated_query).geturl()
        # print("0", query_parameters)
        # query_parameters = temp_query_parameters
        # print("1",query_parameters)
        return new_url

# 示例用法
if __name__ == "__main__":
    http_tool = HTTPTools()

    url = "http://127.0.0.1/pikachu-master/vul/sqli/sqli_str.php?name=admin&submit=%E6%9F%A5%E8%AF%A2"

    # print(http_tool.send_get_request(url).content)
    # print(http_tool.get_argv(url))
    # print(http_tool.update_url(http_tool.get_argv(url)[0],http_tool.get_argv(url)[1],"name","1"))
    par = {"name":"","submit":"12"}
    print(http_tool.update_url_parameters(http_tool.get_argv(url)[0],http_tool.get_argv(url)[1],par))