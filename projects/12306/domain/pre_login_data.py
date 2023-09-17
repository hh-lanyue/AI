import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")
# 读取配置文件信息
pre_login_data = {
    'username': data['login']['username'],
    'password': data['login']['password'],
    'appid': data['login']['appid']
}