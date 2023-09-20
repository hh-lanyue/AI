from config import config
from root.root_path import root_path


# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")

# 读取配置文件信息
url_data = {
    'check_url': config_data['url']['check_url'],
    'login_url': config_data['url']['login_url'],
    'user_login_url': config_data['url']['user_login_url'],
    'query_ticket_url': config_data['url']['query_ticket_url'],
    'buy_pre_submit_order_url': config_data['url']['buy_pre_submit_order_url'],
    'buy_pre_buy_select_seat_init_dc_url': config_data['url']['buy_pre_buy_select_seat_init_dc_url'],
    'buy_pre_get_passenger_info_url': config_data['url']['buy_pre_get_passenger_info_url'],
    'buy_pre_check_order_info_url': config_data['url']['buy_pre_check_order_info_url'],
    'buy_pre_get_queue_count_url': config_data['url']['buy_pre_get_queue_count_url']
}