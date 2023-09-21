from config import config
from root.root_path import root_path
from tools import analy_key_tool

# 设置配置文件路径
config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
# 请求参数关键信息
ticket_form = analy_key_tool.analy_ticket_form_to_obj()
global_token = analy_key_tool.analy_global_token_to_obj()
# 读取配置文件信息
buy_pre_get_queue_count_data = {
    'train_date': ticket_form['queryLeftTicketRequestDTO']['train_date'],
    'train_no': ticket_form['queryLeftTicketRequestDTO']['train_no'],
    'stationTrainCode': ticket_form['queryLeftTicketRequestDTO']['station_train_code'],
    'fromStationTelecode': ticket_form['orderRequestDTO']['from_station_telecode'],
    'toStationTelecode': ticket_form['orderRequestDTO']['to_station_telecode'],
    'leftTicket': ticket_form['leftTicketStr'],
    'purpose_codes': ticket_form['purpose_codes'],
    'train_location': ticket_form['train_location'],
    '_json_att': '',
    'REPEAT_SUBMIT_TOKEN': global_token,
    # M-一等座、O-二等座
    'seatType': 'O',
}
