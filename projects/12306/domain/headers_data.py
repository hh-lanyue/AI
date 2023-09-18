import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")
# 读取请求头的 Cookie
file_cookie = open('config/cookie.txt', 'r', encoding="UTF-8")
cookie_info = file_cookie.read()
file_cookie.close()

# 读取配置文件信息
headers_data = {
    'Cookie': cookie_info,
    'Connection': data['headers']['Connection'],
    'Content-Type': data['headers']['Content-Type'],
    'User-Agent': data['headers']['User-Agent']
}