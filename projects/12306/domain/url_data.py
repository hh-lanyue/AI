import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")

# 读取配置文件信息
url_data = {
    'check_url': data['url']['check_url'],
    'login_url': data['url']['login_url'],
    'user_login_url': data['url']['user_login_url'],
    'query_ticket_url' : data['url']['query_ticket_url']
}