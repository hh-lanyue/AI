import json, tools.train_tool as train_tool
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.buy_pre_submit_order_data import buy_pre_submit_order_data


class buy:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.buy_pre_submit_order_url = url_data.get('buy_pre_submit_order_url')
        # 读取 Cookie
        self.my_cookie = ''

    # 查询车票详情
    def pre_buy_submit_order(self):
        train_key = train_tool.get_train_key()
        buy_pre_submit_order_data['secretStr'] = train_key
        response = session.post(self.buy_pre_submit_order_url, headers=headers_data, data=buy_pre_submit_order_data)
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
                    print('购票成功')
                else:
                    print('购票失败')
                    print(res_data)
        else:
            print('购票失败')

    def init_buy(self):
        self.pre_buy_submit_order()