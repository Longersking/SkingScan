import nmap
import json
from utils.http_tools import HTTPTools
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class WebsiteInfo:
    def __init__(self, url,urls, host):
        self.url = url
        self.urls = urls
        # self.cms = None
        self.ip_address = None
        self.host = host
        self.ports = None
        self.os = None
        self.scan_result = None  # 新增一个属性来存储扫描结果
        self.name = None
        self.product = None

    def scan_target(self):
        try:
            nm = nmap.PortScanner()
            self.scan_result = nm.scan(self.host, arguments='-T4 -n -Pn -O',ports="20-800")['scan']
            print(self.scan_result)
        except nmap.PortScannerError as e:
            print(f"扫描错误: {e}")


    def get_ip(self):
        if 'ipv4' in self.scan_result[self.host]['addresses']:
            self.ip_address = self.scan_result[self.host]['addresses']['ipv4']
        elif 'ipv6' in self.scan_result[self.host]['addresses']:
            self.ip_address = self.scan_result[self.host]['addresses']['ipv6']
        else:
            print("未检测到对方ip信息")
    def get_open_ports(self):
        self.ports = list(self.product.keys())
        print(self.ports)

    def get_os(self):
        self.os = self.scan_result[self.host]['osmatch'][0]['name']
        # print(self.os)

    def get_product(self):
        self.product = self.scan_result[self.host]['tcp']
        # print(self.product)


    def get_website_info(self):
        self.scan_target()
        self.get_os()
        self.get_product()
        self.get_open_ports()
        self.get_ip()

    def to_json(self):
        return json.dumps({
            "URL": self.url,
            "URLS": self.urls,
            "Ports": self.ports,
            "IP": self.ip_address,
            "HOST": self.host,
            "product": self.product,
            "OS": self.os
        }, indent=4)

# 示例用法
if __name__ == "__main__":
    url = "http://127.0.0.1/DVWA-master/index.php"
    urls = HTTPTools.extract_urls(url)
    host = HTTPTools.extract_domain(url)
    website = WebsiteInfo(url,urls, host)
    website.get_website_info()
    result_json = website.to_json()
    print(result_json)
