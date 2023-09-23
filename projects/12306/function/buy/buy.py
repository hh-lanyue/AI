import json
import sys
from tools import cookie_tool, error_tools, analy_key_tool, post_data_to_url_tool
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.buy_pre_submit_order_data import get_pre_submit_order_data
from domain import buy_pre_get_passenger_info_data as passenger_info_data
from domain import buy_pre_check_order_info_data as order_info_data
from domain import buy_pre_get_queue_count_data as queue_count_data
from domain.buy_pre_buy_select_seat_init_dc_data import buy_pre_buy_select_seat_init_dc_data
from domain.buy_submit_order import buy_submit_order_data
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
        # 判断程序是否继续执行
        self.is_continue= True

    # 判断程序是否继续执行
    def jud_is_continue(self, is_reset=False, is_continue_flag=True):
        if is_reset:
            self.is_continue = is_continue_flag
        if not is_continue_flag or not self.is_continue:
            sys.exit()

    # 预订车票
    def buy_pre_submit_order(self):
        # 将 post 的参数拼接到 url 后面
        format_url = self.buy_pre_submit_order_url + post_data_to_url_tool.post_data_to_url(get_pre_submit_order_data())
        response = session.post(format_url, headers=headers_data)
        # response = session.post(self.buy_pre_submit_order_url, headers=headers_data, data=get_pre_submit_order_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                if res_data['status']:
                    cookie_tool.set_cookie(response)
                    print('开始预订购票成功')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    print('开始预订购票失败--用户登录失效')
                    error_tools.record_error(response.text)
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('开始预订购票失败--网络请求失败')

    # 获取车票信息
    def buy_pre_buy_select_seat_init_dc(self):
        response = session.post(self.buy_pre_buy_select_seat_init_dc_url, headers=headers_data, data=buy_pre_buy_select_seat_init_dc_data)
        if response.status_code == 200:
            cookie_tool.set_cookie(response)
            write_content_to_file(file_path=config_path.file_init_dc, content=response.text, is_cls=True)
            # 解析获取的车票信息
            analy_init_dc()
            if analy_key_tool.analy_global_token_to_obj() != '':
                print('获取车票信息成功')
            else:
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                print('获取车票信息失败-用户登录失效')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('获取车票信息失败-网络请求失败')

    # 获取乘客信息
    def buy_pre_get_passenger_info(self):
        response = session.post(self.buy_pre_get_passenger_info_url, headers=headers_data, data=passenger_info_data.get_passenger_info_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                if res_data['status']:
                    cookie_tool.set_cookie(response)
                    if res_data['data']['isExist']:
                        analy_passenger_key(res_data)
                        print('获取乘客信息成功')
                    else:
                        self.jud_is_continue(is_reset=True, is_continue_flag=False)
                        error_tools.record_error(response.text)
                        print('获取乘客信息失败-用户登录失效')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('获取乘客信息失败-网络请求失败')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('获取乘客信息失败-网络请求失败')

    # 校验订单信息是否有效
    def buy_pre_get_check_order_info(self):
        response = session.post(self.buy_pre_check_order_info_url, headers=headers_data, data=order_info_data.get_order_info_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                if res_data['status']:
                    print('校验订单信息成功')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('校验订单信息失败-用户登录失效')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('校验订单信息失败-网络请求失败')

    # 获取余票信息
    def buy_pre_get_queue_count(self):
        response = session.post(self.buy_pre_get_queue_count_url, headers=headers_data, data=queue_count_data.buy_pre_get_queue_count_data_get())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                if res_data['status']:
                    cookie_tool.set_cookie(response)
                    print('获取余票信息成功')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('获取余票信息失败-用户登录失效')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('获取余票信息失败-网络请求失败')

    # 提交订单
    def submit_order(self):
        response = session.post(self.buy_submit_order_url, headers=headers_data, data=buy_submit_order_data())
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                if res_data['status']:
                    cookie_tool.set_cookie(response)
                    print('提交订单成功')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('提交订单失败-用户登录失效')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('提交订单失败-网络请求失败')

    def init_buy(self):
        self.buy_pre_submit_order()
        self.buy_pre_buy_select_seat_init_dc()
        self.buy_pre_get_passenger_info()
        self.buy_pre_get_check_order_info()
        self.buy_pre_get_queue_count()
        self.submit_order()
