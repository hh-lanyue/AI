from config import config
from root.root_path import root_path
from tools.analy_key_tool import analy_passenger_key_to_obj, analy_global_token_to_obj

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
global_token = analy_global_token_to_obj()
passenger_key = analy_passenger_key_to_obj()

# 读取配置文件信息
buy_pre_check_order_info_data = {
    # token
    'REPEAT_SUBMIT_TOKEN': global_token,
    # 固定值
    'cancel_flag': '2',
    # 固定值
    'bed_level_order_num': '000000000000000000000000000000',
    # [座位类型]-[0]-[车票类型]-[姓名]-[证件类型]-[证件号码]-[手机号码]-[是否保存为常用联系人]-[联系人秘钥]
    'passengerTicketStr': 'M,0,1,' + passenger_key['passenger_name'] + ',' + passenger_key['passenger_type'] + ',' + passenger_key['passenger_id_no'] + ',' + passenger_key ['mobile_no'] + ',N' + passenger_key['allEncStr'],
    # [乘客名]-[证件类型]-[证件号]-[乘客类型]
    'oldPassengerStr': '胡海,1,1422***********838,1_',
    # dc-单程票
    'tour_flag': 'dc',
    # 固定值
    'whatsSelect': '1',
    # 空
    'sessionId': '',
    # 空
    'sig': '',
    # 空
    'scene': 'nc_login'
}
