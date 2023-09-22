import json
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.buy_pre_submit_order_data import buy_pre_submit_order_data
from domain import buy_pre_get_passenger_info_data as passenger_info_data
from domain import buy_pre_check_order_info_data as order_info_data
from domain import buy_pre_get_queue_count_data as queue_count_data
from domain.buy_pre_buy_select_seat_init_dc_data import buy_pre_buy_select_seat_init_dc_data
from domain.buy_submit_order import buy_submit_order_data
from tools import post_data_to_url_tool
from tools.file_tool import write_content_to_file
from tools.analy_key_tool import analy_init_dc, analy_passenger_key
from config import config_path


class buy:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.buy_pre_submit_order_url = url_data.get('buy_pre_submit_order_url')
        self.buy_pre_buy_select_seat_init_dc_url = url_data.get('buy_pre_buy_select_seat_init_dc_url')
        self.buy_pre_check_order_info_url = url_data.get('buy_pre_check_order_info_url')
        self.buy_pre_get_passenger_info_url = url_data.get('buy_pre_get_passenger_info_url')
        self.buy_pre_get_queue_count_url = url_data.get('buy_pre_get_queue_count_url')
        self.buy_submit_order_url = url_data.get('buy_submit_order_url')

    # 预订车票
    def pre_buy_submit_order(self):
        # 将 post 的参数拼接到 url 后面
        post_to_get_url = self.buy_pre_submit_order_url + post_data_to_url_tool.post_data_to_url(buy_pre_submit_order_data)
        response = session.post(post_to_get_url, headers=headers_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                file_error.close()
                print(e)
            else:
                if res_data['status']:
                    print('预订票成功')
                else:
                    print('预订票失败')
                    print(res_data)
        else:
            print('预订票失败')

    # 预订选座
    def buy_pre_buy_select_seat_init_dc(self):
        response = session.post(self.buy_pre_buy_select_seat_init_dc_url, headers=headers_data, data=buy_pre_buy_select_seat_init_dc_data)
        if response.status_code == 200:
            if response.ok:
                write_content_to_file(file_path=config_path.file_init_dc, content=response.text, is_cls=True)
                analy_init_dc()
                print('预订选座成功')
        else:
            print('预订选座失败')

    def buy_pre_get_passenger_info(self):
        response = session.post(self.buy_pre_get_passenger_info_url, headers=headers_data, data=passenger_info_data.get_passenger_info_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                file_error.close()
                print(e)
            else:
                if res_data['status']:
                    if res_data['data']['isExist']:
                        analy_passenger_key(res_data)
                        print('获取乘客信息成功')
                    else:
                        print(res_data['data']['exMsg'])
                else:
                    print('获取乘客信息失败')
                    print(res_data)
        else:
            print('预订票失败')

    # 校验订单信息是否有效
    def buy_pre_get_check_order_info(self):
        response = session.post(self.buy_pre_check_order_info_url, headers=headers_data, data=order_info_data.get_order_info_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                file_error.close()
                print(e)
            else:
                if res_data['status']:
                    print('订单信息校验失败')
                else:
                    print('订单信息校验成功')
        else:
            print('订单信息校验失败')

    # 查询余座信息
    def buy_pre_get_queue_count(self):
        response = session.post(self.buy_pre_get_queue_count_url, headers=headers_data, data=queue_count_data.buy_pre_get_queue_count_data_get())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                file_error.close()
                print(e)
            else:
                if res_data['status']:
                    print('查询余座信息成功')
                else:
                    print('查询余座信息失败')
                    print(res_data)
        else:
            print('查询余座信息失败')

    # 提交购票订单
    def submit_order(self):
        response = session.post(self.buy_submit_order_url, headers=headers_data, data=buy_submit_order_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                file_error.close()
                print(e)
            else:
                if res_data['status']:
                    print('查询余座信息成功')
                else:
                    print('查询余座信息失败')
                    print(res_data)
        else:
            print('查询余座信息失败')

    def init_buy(self):
        self.pre_buy_submit_order()
        self.buy_pre_buy_select_seat_init_dc()
        self.buy_pre_get_passenger_info()
        self.buy_pre_get_check_order_info()
        self.buy_pre_get_queue_count()
        self.submit_order()
