from config import config
from root.root_path import root_path
from tools import analy_key_tool

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")


def buy_pre_get_queue_count_data_get():
    ticket_form = analy_key_tool.analy_ticket_form_to_obj()
    global_token = analy_key_tool.analy_global_token_to_obj()
    queue_count_data = {}
    try:
        queue_count_data['train_date'] = ticket_form['queryLeftTicketRequestDTO']['train_date']
        # queue_count_data['train_date'] = ticket_form['orderRequestDTO']['train_date']
        queue_count_data['train_no'] = ticket_form['queryLeftTicketRequestDTO']['train_no']
        queue_count_data['stationTrainCode'] = ticket_form['queryLeftNewDetailDTO']['station_train_code']
        queue_count_data['fromStationTelecode'] = ticket_form['queryLeftNewDetailDTO']['from_station_telecode']
        queue_count_data['toStationTelecode'] = ticket_form['queryLeftNewDetailDTO']['to_station_telecode']
        queue_count_data['leftTicket'] = ticket_form['leftTicketStr']
        queue_count_data['purpose_codes'] = ticket_form['purpose_codes']
        queue_count_data['train_location'] = ticket_form['train_location']
        queue_count_data['_json_att'] = ''
        queue_count_data['REPEAT_SUBMIT_TOKEN'] = global_token
        queue_count_data['seatType'] = 'O'
    except Exception as e:
        print('解析 车票信息 失败，用户未登录')
        print(e)
    return queue_count_data
