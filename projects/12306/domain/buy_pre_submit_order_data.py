from config import config
from root.root_path import root_path
import tools.train_tool as train_tool

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
# 读取 train_key
train_key = train_tool.get_train_key()

# 读取配置文件信息
buy_pre_submit_order_data = {
    'secretStr': train_key,
    'train_date': config_data['buy']['pre']['train_date'],
    'back_train_date': '2023-09-18',
    'tour_flag': 'dc',
    'purpose_codes': config_data['buy']['pre']['purpose_codes'],
    'query_from_station_name': config_data['buy']['pre']['query_from_station_name'],
    'query_to_station_name': config_data['buy']['pre']['query_to_station_name'],
    'undefined': ''
}