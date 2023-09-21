from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")

# 读取配置文件信息
buy_pre_get_passenger_info_data = {
    '_json_att': '',
    'REPEAT_SUBMIT_TOKEN': '29251232358b23af6f247ffb8ecf9462'
}
