from function.session.session_manger import session
from function.query.query_tickets import query_tickets
import json


url1 = 'https://kyfw.12306.cn/otn/login/checkUser'
url3 = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
url5 = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
url4 = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'

file_cookie_info = open('config/cookie.txt', 'r', encoding="UTF-8")
cookie_info = file_cookie_info.read()
file_cookie_info.close()

file_train_key = open('result/train_key.txt', 'r', encoding="UTF-8")
train_key = file_train_key.read()
file_train_key.close()

headers = {
    'Cookie': cookie_info,
    'Connection' : 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

data3 = {
    'REPEAT_SUBMIT_TOKEN': 'e7bd51edff1029f0b346e2e86953aecd'
}

params5 = {
    'leftTicketDTO.train_date': '2023-09-20',
    'leftTicketDTO.from_station': 'SJP',
    'leftTicketDTO.to_station': 'BXP',
    'purpose_codes': 'ADULT'
}

data4 = {
    'secretStr': train_key,
    'train_date': '2023-09-20',
    'back_train_date': '2023-09-18',
    'tour_flag': 'dc',
    'purpose_codes': 'ADULT',
    'query_from_station_name': '石家庄',
    'query_to_station_name': '北京西'
}



response = session.post(url=url1, headers=headers)
print(response.text)
print('=========================================')

response = session.post(url=url3, headers=headers, data=data3)
print(response.text)
print('=========================================')

response = session.get(url=url5, headers=headers, params=params5)
res_data = json.loads(response.text)
for train in res_data['data']['result']:
    li = list(train.split("|"))
    if li[3] == 'G654':
        train_key = li[0]
        print(train_key)
        file_train_key = open('result/train_key.txt', 'w', encoding='UTF-8')
        file_train_key.write(train_key)
        file_train_key.close()
print('=========================================')

data4['secretStr'] = train_key
print(data4.get('secretStr'))
response = session.post(url=url4, headers=headers, data=data4)
print(response.text)
print('=========================================')
