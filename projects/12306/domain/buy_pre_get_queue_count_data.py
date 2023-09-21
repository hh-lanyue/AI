from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")

# 读取配置文件信息
buy_pre_get_queue_count_data = {
    'train_date': '',
    'train_no': '',
    'stationTrainCode': '',
    'seatType': '',
    'fromStationTelecode': 'dc',
    'toStationTelecode': '',
    'leftTicket': '',
    'purpose_codes': '',
    'train_location': '',
    '_json_att': '',
    'REPEAT_SUBMIT_TOKEN': ''
}