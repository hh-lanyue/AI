import json, tools.error_tools as error_tools, tools.train_tool as train_tool
import sys
from config import config
from root.root_path import root_path
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.get_tickets_data import get_tickets_data


class query_tickets:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.query_ticket_url = url_data.get('query_ticket_url')
        # 判断程序是否继续执行
        self.is_continue = True

    # 判断程序是否继续执行
    def jud_is_continue(self, is_reset=False, is_continue_flag=True):
        if is_reset:
            self.is_continue = is_continue_flag
        else:
            if not is_reset and not self.is_continue:
                sys.exit()

    # 登录前校验
    def get_tickets(self):
        self.jud_is_continue()
        # 发送登录请求
        response = session.get(self.query_ticket_url, headers=headers_data, params=get_tickets_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                self.jud_is_continue(is_reset=True, is_continue_flag=False)
                error_tools.record_error(response.text)
                print('查询火车票失败-用户登录失效', e)
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['status'] and res_data['httpstatus'] == 200:
                    if res_data['data']['flag'] == '1':
                        # 获取到需要购买的车次号
                        config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
                        station_train_code = config_data['custom']['station_train_code']
                        train_list = res_data['data']['result']
                        for train_index, train_item in enumerate(train_list):
                            if train_index == 0:
                                train_tool.record_train_list(train_item=train_item, is_cls=True)
                            else:
                                train_tool.record_train_list(train_item=train_item)
                        # 注意放开 BEG
                        for train in res_data['data']['result']:
                            li = list(train.split("|"))
                            if li[3] == station_train_code:
                                train_key = li[0]
                                train_tool.record_train_key(train_key)
                        # 注意放开 END
                        print('查询火车票成功')
                else:
                    self.jud_is_continue(is_reset=True, is_continue_flag=False)
                    print('查询火车票失败-用户登录失效')
        else:
            self.jud_is_continue(is_reset=True, is_continue_flag=False)
            print('查询火车票失败-网络请求失败')

    def init_query(self):
        self.get_tickets()