from tools import analy_key_tool


def buy_submit_order_data():
    # 请求参数关键信息
    global_token = analy_key_tool.analy_global_token_to_obj()
    passenger_key = analy_key_tool.analy_passenger_key_to_obj()
    ticket_form = analy_key_tool.analy_ticket_form_to_obj()
    submit_order_data = {}
    try:
        # [座位类型]-[0]-[车票类型]-[姓名]-[证件类型]-[证件号码]-[手机号码]-[是否保存为常用联系人]-[联系人秘钥]
        submit_order_data['passengerTicketStr'] = 'M,0,1,' + passenger_key['passenger_name'] + ',' + passenger_key['passenger_type'] + ',' + passenger_key['passenger_id_no'] + ',' + passenger_key['mobile_no'] + ',N' + passenger_key['allEncStr']
        # [乘客名]-[证件类型]-[证件号]-[乘客类型]
        submit_order_data['oldPassengerStr'] = passenger_key['passenger_name'] + ',' + + passenger_key['passenger_type'] + ',' + passenger_key['passenger_id_no'] + ',1_'
        #
        submit_order_data['purpose_codes'] = ticket_form['purpose_codes']
        #
        submit_order_data['key_check_isChange'] = ticket_form['key_check_isChange']
        submit_order_data['leftTicketStr'] = ticket_form['leftTicketStr']
        submit_order_data['train_location'] = ticket_form['train_location']
        submit_order_data['choose_seats'] = ''
        submit_order_data['seatDetailType'] = '000'
        submit_order_data['is_jy'] = 'N'
        submit_order_data['is_cj'] = 'Y'
        submit_order_data['whatsSelect'] = '1'
        submit_order_data['roomType'] = '00'
        submit_order_data['dwAll'] = 'N'
        submit_order_data['_json_att'] = ''
        # token
        submit_order_data['REPEAT_SUBMIT_TOKEN'] = global_token
        # 提交订单需要的秘钥
        submit_order_data['encryptedData'] = ''
    except Exception as e:
        print('提交订单失败，用户未登录')
        print(e)
    return submit_order_data


