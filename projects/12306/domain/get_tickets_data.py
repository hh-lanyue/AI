from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
# 读取配置文件信息
get_tickets_data = {
    'leftTicketDTO.train_date': config_data['query']['train_date'],
    'leftTicketDTO.from_station': config_data['query']['from_station'],
    'leftTicketDTO.to_station': config_data['query']['to_station'],
    'purpose_codes': config_data['query']['purpose_codes']
}
