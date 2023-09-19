from config import config
from root.root_path import root_path
import tools.cookie_tool as cookie_tool

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
# 读取请求头的 Cookie
cookie_info = cookie_tool.get_cookie()

# 读取配置文件信息
headers_data = {
    'Cookie': cookie_info,
    'Connection': config_data['headers']['Connection'],
    'Content-Type': config_data['headers']['Content-Type'],
    'User-Agent': config_data['headers']['User-Agent']
}