import json, tools.error_tools as error_tools, tools.train_tool as train_tool
from tools.session_tool import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.get_tickets_data import get_tickets_data


class query_tickets:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.query_ticket_url = url_data.get('query_ticket_url')

    # 登录前校验
    def get_tickets(self):
        # 发送登录请求
        response = session.get(self.query_ticket_url, headers=headers_data, params=get_tickets_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('查询异常')
                print(e)
                error_tools.record_error(response.text)
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['status'] and res_data['httpstatus'] == 200:
                    print('查询火车票成功')
                    if res_data['data']['flag'] == '1':
                        train_list = res_data['data']['result']
                        for train_index, train_item in enumerate(train_list):
                            if train_index == 0:
                                train_tool.record_train_list(train_item=train_item, is_cls=True)
                            else:
                                train_tool.record_train_list(train_item=train_item)
                        # 注意放开 BEG
                        for train in res_data['data']['result']:
                            li = list(train.split("|"))
                            if li[3] == 'G654':
                                train_key = li[0]
                                train_tool.record_train_key(train_key)
                        # 注意放开 END
                else:
                    print('查询火车票未成功')
        else:
            print('查询火车票失败')

    def init_query(self):
        self.get_tickets()