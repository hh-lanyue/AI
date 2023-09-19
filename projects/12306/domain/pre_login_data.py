from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
# 读取配置文件信息
pre_login_data = {
    'username': config_data['login']['username'],
    'password': config_data['login']['password'],
    'appid': config_data['login']['appid']
}