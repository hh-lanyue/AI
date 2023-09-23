from config import config
from root.root_path import root_path
import tools.train_tool as train_tool
from tools.time_tool import curr_date


# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")


def get_pre_submit_order_data():
    # 定义返回参数
    pre_submit_order_data = {}
    # 读取 train_key
    train_key = train_tool.get_train_key()
    pre_submit_order_data['secretStr'] = train_key
    pre_submit_order_data['train_date'] = config_data['custom']['train_date']
    pre_submit_order_data['back_train_date'] = curr_date
    pre_submit_order_data['tour_flag'] = config_data['custom']['tour_flag']
    pre_submit_order_data['purpose_codes'] = config_data['custom']['purpose_codes']
    pre_submit_order_data['query_from_station_name'] = config_data['custom']['query_from_station_name']
    pre_submit_order_data['query_to_station_name'] = config_data['custom']['query_to_station_name']
    pre_submit_order_data['undefined'] = ''
    # 返回数据
    return pre_submit_order_data
