import json
from config import config
from root.root_path import root_path
from bs4 import BeautifulSoup
from config import config_path
from tools import file_tool
import re


def get_global_repeat_submit_token():
    file_html = open(config_path.file_init_dc, 'r', encoding='utf8')
    contents = file_html.read()
    soup = BeautifulSoup(contents, 'html.parser')
    data_list = soup.findAll('script')
    global_repeat_submit_token = ''
    for item in data_list:
        # 关键字
        key = 'globalRepeatSubmitToken'
        if key in item.text:
            global_repeat_submit_token = re.findall('globalRepeatSubmitToken\\s?=\\s?\'\\w+\'', item.text, 0)[0].split('=')[1].replace('\'', '').strip()
    return global_repeat_submit_token


def get_ticket_info_for_passenger_form():
    file_html = open(config_path.file_init_dc, 'r', encoding='utf8')
    contents = file_html.read()
    soup = BeautifulSoup(contents, 'html.parser')
    data_list = soup.findAll('script', {'xml:space': 'preserve'})
    ticket_info_for_passenger_form = ''
    for item in data_list:
        # 关键字
        key = 'ticketInfoForPassengerForm'
        if key in item.text:
            ticket_info_for_passenger_form = re.findall('ticketInfoForPassengerForm=\\S+', item.text, 0)[0].split('=')[1].replace(';', '').strip()
    return ticket_info_for_passenger_form


def analy_init_dc():
    try:
        file_tool.write_content_to_file(config_path.global_token, get_global_repeat_submit_token(), is_cls=True)
        file_tool.write_content_to_file(config_path.ticket_form, get_ticket_info_for_passenger_form(), is_cls=True)
    except Exception:
        print('解析 init_dc 失败，用户未登录')


def analy_passenger_key(passenger_data):
    try:
        config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
        user_name = config_data['query']['user_name']
        passenger_list_info = passenger_data['data']['normal_passengers']
        for passenger_info in passenger_list_info:
            if passenger_info['passenger_name'] == user_name:
                file_tool.write_content_to_file(config_path.passenger_key, json.dumps(passenger_info), is_cls=True)
    except Exception as e:
        print('解析 乘客密钥 失败，用户未登录')
        print(e)


def analy_passenger_key_to_obj():
    passenger_info = file_tool.read_file(config_path.passenger_key)
    result_data = passenger_info.replace(" ", "").replace("\t", "").replace("\n", "").replace('\'', '\"')
    return json.loads(result_data)


def analy_global_token_to_obj():
    global_token = file_tool.read_file(config_path.global_token)
    return global_token


def analy_ticket_form_to_obj():
    result_data = {}
    ticket_form = file_tool.read_file(config_path.ticket_form)
    json_data = ticket_form.replace(" ", "").replace("\t", "").replace("\n", "").replace('\'', '\"')
    try:
        result_data = json.loads(json_data)
    except Exception as e:
        print('解析 车票信息 失败，用户未登录')
        print(e)
    return result_data
