from config import config
from root.root_path import root_path
import tools.cookie_tool as cookie_tool


# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config_url.yaml")
# 读取请求头的 Cookie
cookie_info = cookie_tool.get_cookie()

# 读取配置文件信息
url_data = {
    'beijing_time_url': config_data['url']['beijing_time_url'],
    'check_url': config_data['url']['check_url'],
    'login_url': config_data['url']['login_url'],
    'user_login_url': config_data['url']['user_login_url'],
    'query_ticket_url': config_data['url']['query_ticket_url'],
    'buy_pre_submit_order_url': config_data['url']['buy_pre_submit_order_url'],
    'buy_pre_buy_select_seat_init_dc_url': config_data['url']['buy_pre_buy_select_seat_init_dc_url'],
    'buy_pre_get_passenger_info_url': config_data['url']['buy_pre_get_passenger_info_url'],
    'buy_pre_check_order_info_url': config_data['url']['buy_pre_check_order_info_url'],
    'buy_pre_get_queue_count_url': config_data['url']['buy_pre_get_queue_count_url'],
    'buy_submit_order_url': config_data['url']['buy_submit_order_url']
}

# 读取配置文件信息
headers_data = {
    'Cookie': cookie_info,
    'Connection': config_data['headers']['Connection'],
    'Content-Type': config_data['headers']['Content-Type'],
    'User-Agent': config_data['headers']['User-Agent']
}