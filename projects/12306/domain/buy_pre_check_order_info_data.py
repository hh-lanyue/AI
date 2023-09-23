from tools import analy_key_tool
from config import config
from root.root_path import root_path


config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")


def get_order_info_data():
    # 请求参数关键信息
    #   token
    global_token = analy_key_tool.analy_global_token_to_obj()
    #   乘客信息
    passenger_key = analy_key_tool.analy_passenger_key_to_obj()
    #   座位类型
    set_type = config_data['custom']['seat_type']
    #   车票类型
    ticket_type = config_data['custom']['ticket_type']
    order_info_data = {}
    try:
        # token
        order_info_data['REPEAT_SUBMIT_TOKEN'] = global_token
        # [座位类型]-[0]-[车票类型]-[姓名]-[证件类型]-[证件号码]-[手机号码]-[是否保存为常用联系人]-[联系人秘钥]
        order_info_data['passengerTicketStr'] = set_type + ',0,' + ticket_type + ',' + passenger_key['passenger_name'] + ',' + passenger_key['passenger_type'] + ',' + passenger_key['passenger_id_no'] + ',' + passenger_key['mobile_no'] + ',N,' + passenger_key['allEncStr']
        # [乘客名]-[证件类型]-[证件号]-[乘客类型]
        # order_info_data['oldPassengerStr'] = '胡海,1,1422***********838,1_'
        order_info_data['oldPassengerStr'] = passenger_key['passenger_name'] + ',' + passenger_key['passenger_type'] + ',' + passenger_key['passenger_id_no'] + ',1_'
        # dc-单程票
        order_info_data['tour_flag'] = config_data['custom']['tour_flag']
        # 固定值
        order_info_data['cancel_flag'] = '2'
        # 固定值
        order_info_data['bed_level_order_num'] = '000000000000000000000000000000'
        # 固定值
        order_info_data['whatsSelect'] = '1'
        # 固定值
        order_info_data['scene'] = 'nc_login'
        # 空
        order_info_data['sessionId'] = ''
        # 空
        order_info_data['sig'] = ''
    except Exception as e:
        print('校验 订单信息 失败，用户未登录')
        print(e)
    return order_info_data


