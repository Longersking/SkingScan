import urllib.request
import requests
from urllib.parse import urlparse, urlencode, parse_qs
import json
from copy import deepcopy

class HTTPTools:
    def __init__(self):
        pass

    @staticmethod
    def send_get_request(url, params=None, headers=None, data=None,  proxies=None):
        try:
            response = requests.get(url, params=params, headers=headers, data=data, proxies=proxies)
            response.raise_for_status()  # 抛出异常如果请求不成功
            return response
        except requests.exceptions.RequestException as e:
            print(f"get请求error: {e}")
            return None


    @staticmethod
    def send_post_request(url, data=None, json=None, params=None, headers=None,  proxies=None):
        try:
            response = requests.post(url, data=data, json=json, params=params, headers=headers, proxies=proxies)
            response.raise_for_status()  # 抛出异常如果请求不成功
            return response
        except requests.exceptions.RequestException as e:
            print(f"post请求error: {e}")
            return None

    @staticmethod
    def send_http_request(url, request_data=None, headers=None, proxy_method='http',proxies=None,method='GET'):
        if proxies:  # 如果传入了代理地址和端口
            http_proxy_handler = urllib.request.ProxyHandler({proxy_method: proxies})
            opener = urllib.request.build_opener(http_proxy_handler)
        else:  # 如果没有传入代理地址和端口
            opener = urllib.request.build_opener()
        request_data = json.dumps(request_data).encode('utf-8')
        request = urllib.request.Request(url=url, headers=headers, data=request_data,method=method)
        response = opener.open(request)
        print(response.read().decode('utf-8'))



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


    # 更新url
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


    # 修改url的参数
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

    # url = "http://127.0.0.1/pikachu-master/vul/sqli/sqli_str.php?name=admin&submit=%E6%9F%A5%E8%AF%A2"
    #
    # # print(http_tool.send_get_request(url).content)
    # # print(http_tool.get_argv(url))
    # # print(http_tool.update_url(http_tool.get_argv(url)[0],http_tool.get_argv(url)[1],"name","1"))
    # par = {"name":"","submit":"12"}
    # print(http_tool.update_url_parameters(http_tool.get_argv(url)[0],http_tool.get_argv(url)[1],par))
#     host = "192.168.52.128"
#     port = 8080
#     raw_request = """
#         GET /icons/.%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd HTTP/1.1
# Content-Length: 517
# Host: 192.168.52.128:8080
# User-Agent: Mozilla/5.0 (X11; FreeBSD i386 6.73; rv:220.59) Gecko/20100101 Chrome/175.28 OPR/220.59;
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate
# Connection: close
# Upgrade-Insecure-Requests: 1
# If-Modified-Since: Thu, 14 Oct 2021 06:00:45 GMT
# If-None-Match: "29cd-5ce49cca73d40-gzip"
# Cache-Control: max-age=0
#     """
#     print(http_tool.send_http_message(host, port, raw_request))

