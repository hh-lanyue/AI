import json, tools.cookie_tool as cookie_tool, tools.error_tools as error_tools
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
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
        # 发送登录请求
        response = session.post(self.check_url, headers=headers_data, data=pre_login_data)

        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                error_tools.record_error(response.text)
                print(e)
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['result_code'] == 0:
                    cookie_tool.set_cookie(response, is_first=True)
                    print('登录前校验通过')
                else:
                    print('登录前校验未通过：', res_data)
        else:
            print('登录前校验未通过')

    def do_login(self):
        # 发送登录请求
        response = session.post(self.login_url, headers=headers_data, data=login_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('账号异常')
                error_tools.record_error(response.text)
                print(e)
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['result_code'] == 0:
                    print('登录成功')
                    cookie_tool.set_cookie(response)
                else:
                    print('登录失败：', response.text)
        else:
            print('登录失败')

    def user_login(self):
        # 发送登录请求，会引发重定向
        response = session.get(url=self.user_login_url, headers=headers_data)
        # 获取重定向地址
        redirect_url = response.url
        response = session.get(redirect_url, headers=headers_data)
        if response.ok:
            print('登录成功')
            cookie_tool.set_cookie(response)
        else:
            print('登录失败')

    def init_login(self):
        self.pre_login()
        self.do_login()
        self.user_login()