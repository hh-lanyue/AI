import json, tools.cookie_tool as cookie_tool, tools.error_tools as error_tools
from tools import global_variable_manger_tool as global_manger
from tools.session_tool import session
from domain.url_data import url_data
from domain.url_data import headers_data
from domain.pre_login_data import pre_login_data
from domain.login_data import login_data


class login:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.check_url = url_data.get('check_url')
        # 登录地址
        self.login_url = url_data.get('login_url')
        # 用户登录地址
        self.user_login_url = url_data.get('user_login_url')

    # 登录前校验
    def pre_login(self):
        global_manger.jud_is_continue()
        # 发送登录请求
        response = session.post(self.check_url, headers=headers_data, data=pre_login_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['result_code'] == 0:
                    cookie_tool.set_cookie(response, is_first=True)
                    print('登录前校验成功')
                else:
                    global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('登录前校验失败-账号密码错误或账号状态异常')
        else:
            global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('登录前校验失败-网络请求失败')

    def do_login(self):
        global_manger.jud_is_continue()
        # 发送登录请求
        response = session.post(self.login_url, headers=headers_data, data=login_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text, e)
                print('账号异常')
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['result_code'] == 0:
                    cookie_tool.set_cookie(response)
                    print('登录成功')
                else:
                    global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
                    error_tools.record_error(response.text)
                    print('登录失败-账号密码错误或账号状态异常')
        else:
            global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('登录失败-网络请求失败')

    def user_login(self):
        global_manger.jud_is_continue()
        # 发送登录请求，会引发重定向
        response = session.get(url=self.user_login_url, headers=headers_data)
        if response.status_code == 200:
            # 获取重定向地址
            redirect_url = response.url
            response = session.get(redirect_url, headers=headers_data)
            if response.status_code == 200:
                cookie_tool.set_cookie(response)
                print('登录成功')
            else:
                global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
                print('登录失败-网络请求失败')
        else:
            global_manger.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('登录失败-网络请求失败')

    def init_login(self):
        self.pre_login()
        self.do_login()
        self.user_login()