from config import config
from root.root_path import root_path

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")

# 读取配置文件信息
buy_pre_check_order_info_data = {
    # 固定值
    'cancel_flag': '2',
    # 固定值
    'bed_level_order_num': '000000000000000000000000000000',
    # [座位类型]-[0]-[车票类型]-[姓名]-[证件类型]-[证件号码]-[手机号码]-[是否保存为常用联系人]-[联系人秘钥]
    'passengerTicketStr': 'M,0,1,胡海,1,1422***********838,181****4376,N,bf4b0cf64957ea05d0ca63b55e44a5aa244acee0b3e4ece8119dcc27713e40c4a7efeb46d92af4ee0988cc2b0a8f8cd3c6dac0bd7014fa5817d23a7d2f2ee5a159bb6b574722d3d4071a6a1cd276ae53c97b3d8e9456da0da34a2dff9bf3b3fb',
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
    'scene': 'nc_login',
    #
    'REPEAT_SUBMIT_TOKEN': '1a35ffcafc22ffe4a9ad84d4815b0290'
}
