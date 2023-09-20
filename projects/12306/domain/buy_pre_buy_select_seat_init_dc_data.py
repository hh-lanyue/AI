from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")

# 读取配置文件信息
buy_pre_buy_select_seat_init_dc_data = {
    # 空值
    '_json_att': ''
}
