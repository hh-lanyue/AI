import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")
# 读取配置文件信息
buy_ticket_data = {
    'username': data['login']['self.username'],
    'password': data['login']['self.password'],
    'appid': data['login']['self.appid']
}